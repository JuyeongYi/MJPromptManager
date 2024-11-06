import json
import mimetypes
from dataclasses import dataclass
from datetime import datetime
from importlib.metadata import metadata
from pathlib import Path
from typing import Optional, Dict, List
from urllib.parse import urlparse, unquote

import requests


@dataclass(frozen=True)
class ImageInfo:
    url: str
    filename: Path
    tags: List[str]
    metadata: Optional[Dict[str, str]] = None

    @classmethod
    def FromJSON(cls, json_path: Path | str) -> 'ImageInfo':
        json_path = Path(json_path)
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            md = data.get('metadata', None)
            return cls(
                url=data['url'],
                filename=Path(data['filename']),
                tags=data['tags'],
                metadata=md
            )

    @property
    def JSON(self) -> Dict:
        data = {
            'url': self.url,
            'filename': str(self.filename),
            'tags': self.tags
        }
        if self.metadata:
            data.update(self.metadata)
        return data

    def Rename(self, new_name: str | Path) -> 'ImageInfo':
        """
        이미지 파일과 관련 JSON 파일의 이름을 변경하고 새로운 ImageInfo 객체 반환
        """
        currImg = self.filename
        currJSON = self.filename.with_suffix('.json')

        resCurrImg = currImg.resolve()
        resCurrJSON = currJSON.resolve()

        if not resCurrImg.exists() or not resCurrJSON.exists():
            raise FileNotFoundError(f"Image or JSON file not found: {resCurrImg}")

        newPath = Path(f"{new_name}{self.filename.suffix}")
        newImg = currImg.parent / newPath
        newJSON = newImg.with_suffix('.json')

        if newImg.exists() or newJSON.exists():
            raise FileExistsError(f"File already exists: {newImg}")

        newImgInfo = ImageInfo(
            url=self.url,
            filename=newImg,
            tags=self.tags.copy(),
            metadata=self.metadata.copy() if self.metadata else None
        )

        try:
            currImg.rename(newImg)
            with open(newJSON, 'w', encoding='utf-8') as f:
                json.dump(newImgInfo.JSON, f, ensure_ascii=False, indent=2)
            currJSON.unlink()
            return newImgInfo

        except Exception as e:
            try:
                if newImg.exists():
                    newImg.rename(currImg)
                if newJSON.exists():
                    newJSON.unlink()
            except Exception as rollback_error:
                raise RuntimeError(f"Failed to rollback after error: {str(rollback_error)}")

            raise RuntimeError(f"Failed to rename files: {str(e)} File Rollback completed.")

    @property
    def JSONPath(self) -> Path:
        return self.filename.with_suffix('.json')


class ImageDownloader:
    def __init__(self, saveDir: Path | str):
        """
        이미지 다운로더 초기화

        Args:
            saveDir (Union[Path, str]): 이미지와 메타데이터를 저장할 디렉토리 경로
        """
        self.saveDir = Path(saveDir)
        self.saveDir.mkdir(parents=True, exist_ok=True)

    def IsURLImage(self, url: str) -> bool:
        """
        URL이 이미지를 가리키는지 확인

        Args:
            url (str): 확인할 URL

        Returns:
            bool: 이미지 URL이면 True, 아니면 False
        """
        try:
            response = requests.head(url, allow_redirects=True)
            content_type = response.headers.get('content-type', '')
            return content_type.startswith('image/')
        except requests.RequestException:
            return False

    def GetFileNameFromURL(self, url: str) -> Path:
        """
        URL에서 파일명 추출

        Args:
            url (str): 이미지 URL

        Returns:
            Path: 파일명을 포함한 Path 객체
        """
        parsed_url = urlparse(url)
        filename = unquote(Path(parsed_url.path).name)

        # 파일명이 없는 경우 타임스탬프로 생성
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            extension = mimetypes.guess_extension(requests.head(url).headers['content-type'])
            filename = f"image_{timestamp}{extension}"

        return Path(filename)

    def DownloadImage(self, url: str, tags: List[str] = None,
                      moreMetadata: Dict = None) -> Optional[ImageInfo]:
        """
        이미지 다운로드 및 메타데이터 저장

        Args:
            url (str): 이미지 URL
            tags (List[str], optional): 이미지 태그 리스트
            moreMetadata (Dict, optional): 추가 메타데이터

        Returns:
            Optional[ImageInfo]: 성공 시 저장된 파일 메타데이터 json 경로, 실패 시 None
        """
        try:
            # URL 유효성 검사
            if not self.IsURLImage(url):
                print(f"Error: {url} is not a valid image URL")
                return None

            # 이미지 다운로드
            response = requests.get(url, stream=True)
            response.raise_for_status()

            # 파일 경로 생성
            filename = self.GetFileNameFromURL(url)
            imagePath = self.saveDir / filename

            # 이미지 저장
            imagePath.write_bytes(response.content)

            # 메타데이터 준비
            metadata = {
                'url': url,
                'filename': str(imagePath),
                'tags': tags or [],
            }

            # 추가 메타데이터 병합
            if moreMetadata:
                metadata["metadata"] = moreMetadata

            # 메타데이터 JSON 파일 저장
            jsonPath = imagePath.with_suffix('.json')
            jsonPath.write_text(
                json.dumps(metadata, ensure_ascii=False, indent=2),
                encoding='utf-8'
            )

            return ImageInfo(url, imagePath, tags, metadata)

        except Exception as e:
            print(f"Error downloading image from {url}: {str(e)}")
            return None

    def GetImageInfos(self) -> List[ImageInfo]:
        """
        다운로드된 모든 이미지와 관련 메타데이터 파일 경로 반환

        Returns:
            List[Dict[str, Path]]: 이미지와 JSON 파일 경로 목록
        """
        toReturn = []
        for js in self.saveDir.glob('*.json'):
            toReturn.append(ImageInfo.FromJSON(js))

        return toReturn


if __name__ == '__main__':
    downloader = ImageDownloader('images')
    urls = ["https://www.dogdrip.net/dvs/d/24/11/06/565f284f923e045aa47be2323f681183.png"]
    for url in urls:
        downloader.DownloadImage(url, tags=['dog', 'cute'], moreMetadata={'source': 'dogdrip'})

    for idx, info in enumerate(downloader.GetImageInfos()):
        info.Rename(f"{idx}")

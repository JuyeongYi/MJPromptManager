import json
import mimetypes
from dataclasses import dataclass
from datetime import datetime
from importlib.metadata import metadata
from pathlib import Path
from typing import Optional, Dict, List
from urllib.parse import urlparse, unquote

import requests


@dataclass
class ImageInfo:
    url: str
    filename: Path
    tags: List[str]

    @classmethod
    def FromJSON(cls, json_path: Path | str) -> 'ImageInfo':
        json_path = Path(json_path)
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return cls(
                url=data['url'],
                filename=Path(data['filename']),
                tags=data['tags']
            )

    @property
    def JSON(self) -> Dict:
        data = {
            'url': self.url,
            'filename': str(self.filename),
            'tags': self.tags
        }
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

        edit = newImg == currImg
        if not edit:
            for newFile in (newImg, newJSON):
                if newFile.exists():
                    newFile.unlink(missing_ok=True)

        newImgInfo = ImageInfo(
            url=self.url,
            filename=newImg,
            tags=self.tags if self.tags else list(),
        )

        try:
            currImg.rename(newImg)
            with open(newJSON, 'w', encoding='utf-8') as f:
                toWrite = newImgInfo.JSON
                json.dump(toWrite, f, ensure_ascii=False, indent=2)
            if not edit:
                currJSON.unlink()
            return newImgInfo

        except Exception as e:
            if not edit:
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
        self.__saveDir = Path(saveDir)
        self.__saveDir.mkdir(parents=True, exist_ok=True)

    @property
    def SaveDir(self):
        return self.__saveDir

    def IsURLImage(self, url: str) -> bool:
        toks = url.rsplit('.', 1)
        suff = toks[-1]
        if '?' in suff:
            suff = suff.split('?')[0]

        if suff not in ("png", "gif", "webp", "jpg", "jpeg"):
            return False
        try:
            response = requests.head(url, allow_redirects=True)
            content_type = response.headers.get('content-type', '')
            if not content_type.startswith('image/'):
                print(
                    f"Warning: {url} content type is not an image, but {content_type}. Could be binary but not image.")
            return True
        except requests.RequestException:
            return False

    def GetFileNameFromURL(self, url: str) -> Path:
        parsed_url = urlparse(url)
        filename = unquote(Path(parsed_url.path).name)

        # 파일명이 없는 경우 타임스탬프로 생성
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            extension = mimetypes.guess_extension(requests.head(url).headers['content-type'])
            filename = f"image_{timestamp}{extension}"

        return Path(filename)

    def DownloadImage(self, url: str, tags: List[str] = None) -> Optional[ImageInfo]:
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
            if url.isnumeric():
                filename = f"style_{url}"
            imagePath = self.__saveDir / filename

            # 이미지 저장
            imagePath.write_bytes(response.content)
            infoTags = tags if tags is not None else list()
            # 메타데이터 준비
            metadata = {
                'url': url,
                'name': filename.stem,
                'filename': str(imagePath),
                'tags': infoTags,
            }

            # 메타데이터 JSON 파일 저장
            jsonPath = imagePath.with_suffix('.json')
            jsonPath.write_text(
                json.dumps(metadata, ensure_ascii=False, indent=2),
                encoding='utf-8'
            )

            return ImageInfo(url, imagePath, infoTags)

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
        for js in self.__saveDir.glob('*.json'):
            toReturn.append(ImageInfo.FromJSON(js))

        return toReturn

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import Qt
import sys


class ImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("URL 이미지 뷰어")
        self.setGeometry(100, 100, 800, 600)

        # 이미지를 표시할 QLabel 생성
        self.image_label = QLabel(self)
        self.setCentralWidget(self.image_label)

        # 네트워크 매니저 설정
        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.handle_network_response)

    def load_image_from_url(self, url):
        # URL로부터 이미지 다운로드 요청
        request = QNetworkRequest(QUrl(url))
        self.network_manager.get(request)

    def handle_network_response(self, reply: QNetworkReply):
        if reply.error() == QNetworkReply.NetworkError.NoError:
            # 데이터를 읽어서 QPixmap으로 변환
            data = reply.readAll()
            pixmap = QPixmap()
            pixmap.loadFromData(data)

            # 이미지 크기를 윈도우에 맞게 조절
            scaled_pixmap = pixmap.scaled(self.image_label.size(),
                                          aspectMode=Qt.AspectRatioMode.KeepAspectRatio)


            # 이미지 표시
            self.image_label.setPixmap(scaled_pixmap)
        else:
            print(f"이미지 로딩 에러: {reply.errorString()}")

        reply.deleteLater()


def main():
    app = QApplication(sys.argv)
    window = ImageWindow()
    window.show()

    # 예시 이미지 URL 로드
    window.load_image_from_url("https://i.imgur.com/YhnkTFs.jpeg")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
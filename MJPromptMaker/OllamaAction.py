from PySide6.QtWidgets import QProgressDialog, QTextEdit
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QThread, Signal
from ollama import Client
import traceback


class OllamaWorker(QThread):
    finished = Signal(str)
    progress = Signal(str)  # 스트리밍 응답을 위한 시그널 추가

    def __init__(self, prompt, model='mistral'):
        super().__init__()
        self.prompt = prompt
        self.model = model
        self.client = Client(host='http://localhost:11434')

    def run(self):
        try:
            # 스트리밍 방식으로 응답 받기
            full_response = []
            for response in self.client.generate(model=self.model, prompt=self.prompt, stream=True):
                chunk = response.get('response', '')
                full_response.append(chunk)
                self.progress.emit(chunk)  # 각 청크마다 진행상황 알림

                # 스레드가 중단되었는지 확인
                if self.isInterruptionRequested():
                    return

            self.finished.emit(''.join(full_response))

        except ConnectionRefusedError:
            error_msg = "Error: Could not connect to Ollama. Please make sure Ollama is running."
            self.finished.emit(error_msg)
        except Exception as e:
            error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
            self.finished.emit(error_msg)


class OllamaAction(QAction):
    def __init__(self, text_edit: QTextEdit, model='llama3.1'):
        super().__init__("Ask Ollama", text_edit)
        self.text_edit = text_edit
        self.model = model
        self.triggered.connect(self.ask_ollama)
        self.progress_dialog = None
        self.worker = None

    def ask_ollama(self):
        current_text = self.text_edit.toPlainText()
        if not current_text.strip():
            return

        # 프로그레스 다이얼로그 생성
        self.progress_dialog = QProgressDialog("Getting response from Ollama...", "Cancel", 0, 0)
        self.progress_dialog.setWindowTitle("Processing")
        self.progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progress_dialog.setMinimumDuration(0)
        self.progress_dialog.setAutoClose(True)
        self.progress_dialog.setAutoReset(True)

        # OllamaWorker 스레드 시작
        self.worker = OllamaWorker(current_text, self.model)
        self.worker.finished.connect(self.OnFinished)
        self.worker.progress.connect(self.DuringProgress)
        self.progress_dialog.canceled.connect(self.OnCancled)
        self.worker.start()

        self.progress_dialog.exec()

    def OnCancled(self):
        if self.worker and self.worker.isRunning():
            self.worker.requestInterruption()
            self.worker.wait()  # 스레드가 완전히 종료될 때까지 대기

    def DuringProgress(self, chunk):
        # 프로그레스 다이얼로그 레이블 업데이트
        if self.progress_dialog and chunk:
            current_text = self.progress_dialog.labelText()
            self.progress_dialog.setLabelText("Receiving response...")

    def OnFinished(self, response):
        if self.progress_dialog:
            self.progress_dialog.close()

        if response.startswith("Error:"):
            self.text_edit.append("\n\n" + response)
        else:
            self.text_edit.setPlainText(response)

# EzSearch.py
import sys
import os
import threading
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel, QProgressBar
)
from PyQt5.QtCore import Qt

class EzSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EzSearch")
        self.setFixedSize(500, 400)
        self.setStyleSheet("background-color: #121212; color: #FFFFFF; font-family: Arial;")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Enter search query:")
        layout.addWidget(self.label)

        self.search_input = QLineEdit()
        self.search_input.setStyleSheet("background-color: #1E1E1E; color: #FFFFFF; padding: 5px;")
        layout.addWidget(self.search_input)

        self.search_button = QPushButton("Search")
        self.search_button.setStyleSheet("background-color: #BB86FC; color: black; padding: 5px;")
        self.search_button.clicked.connect(self.start_search_thread)
        layout.addWidget(self.search_button)

        self.progress = QProgressBar()
        self.progress.setMaximum(0)  # Indeterminate
        self.progress.hide()
        layout.addWidget(self.progress)

        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.result_area.setStyleSheet("background-color: #1E1E1E; color: #FFFFFF;")
        layout.addWidget(self.result_area)

        self.setLayout(layout)

    def start_search_thread(self):
        query = self.search_input.text().strip()
        if not query:
            self.result_area.setText("Please enter a search query.")
            return
        self.progress.show()
        self.result_area.clear()
        thread = threading.Thread(target=self.perform_search, args=(query,))
        thread.start()

    def perform_search(self, query):
        try:
            # Fake search simulation (replace with real search logic)
            import time
            time.sleep(2)  # Simulate search delay
            # Example results
            results = [
                f"Result 1 for '{query}'",
                f"Result 2 for '{query}'",
                f"Result 3 for '{query}'"
            ]
            self.show_results(results)
        except Exception as e:
            self.show_results([f"Error: {str(e)}"])
        finally:
            self.progress.hide()

    def show_results(self, results):
        text = "\n".join(results)
        self.result_area.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EzSearchApp()
    window.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Save-File-Control")
        self.resize(600, 400)
        
        self.games = ["Eldenring", "Dark Souls 1", "Dark Souls 2", "Dark Souls 3", "Dark Souls Remastered"]
        
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        for game in self.games:
            button = QPushButton(game)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button.setStyleSheet(self.get_button_style())
            layout.addWidget(button)

    def get_button_style(self):
        return """
            QPushButton {
                font-size: 22px;
                font-weight: bold;
                padding: 20px;
                border: 3px solid palette(highlight);
                border-radius: 15px;
                background-color: transparent;
                color: palette(window-text);
            }
            QPushButton:hover {
                background-color: palette(highlight);
                color: palette(highlighted-text);
            }
            QPushButton:pressed {
                background-color: palette(dark);
                color: palette(highlighted-text);
            }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
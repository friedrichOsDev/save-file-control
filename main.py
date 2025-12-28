import sys, os, json
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QStackedWidget, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Save-File-Control")
        self.resize(600, 400)
        
        self.games = ["Eldenring", "Dark Souls 1", "Dark Souls 2", "Dark Souls 3", "Dark Souls Remastered"]
        self.game_save_paths = self.get_game_save_paths()
        
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        self.init_ui()

    def init_ui(self):
        self.menu_widget = QWidget()
        layout = QVBoxLayout(self.menu_widget)

        for game in self.games:
            button = QPushButton(game)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button.setStyleSheet(self.get_button_style())
            button.clicked.connect(lambda checked, g=game: self.show_game_view(g)) # checked is always False for QPushButton
            layout.addWidget(button)
            
        self.stack.addWidget(self.menu_widget)

    def show_game_view(self, game_name):
        game_widget = QWidget()
        layout = QVBoxLayout(game_widget)
        
        label = QLabel(f"Menü für: {game_name}")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(self.get_label_style())
        layout.addWidget(label)
        
        back_btn = QPushButton("Zurück")
        back_btn.setStyleSheet(self.get_button_style())
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)
        
        self.stack.addWidget(game_widget)
        self.stack.setCurrentWidget(game_widget)

    def go_back(self):
        current_widget = self.stack.currentWidget()
        self.stack.setCurrentIndex(0)
        if current_widget != self.menu_widget:
            self.stack.removeWidget(current_widget)
            current_widget.deleteLater()

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
    
    def get_label_style(self):
        return """
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: palette(window-text);
                margin: 20px;
            }
        """
        
    def get_game_save_paths(self):
        appdata_path = os.getenv("APPDATA") if os.name == "nt" else None
        documents_path = os.path.join(os.getenv("USERPROFILE"), "Documents", "NBGI") if os.name == "nt" else None
        return {
            "win": {
                "Eldenring": os.path.join(appdata_path, "EldenRing"),
                "Dark Souls 1": os.path.join(documents_path, "DarkSouls"),
                "Dark Souls 2": os.path.join(appdata_path, "DarkSoulsII"),
                "Dark Souls 3": os.path.join(appdata_path, "DarkSoulsIII"),
                "Dark Souls Remastered": os.path.join(documents_path, "DARK SOULS REMASTERED")
            },
            "linux": {
                # linux paths can be added here
            },
            "mac": {
                # mac paths can be added here
            }
        }

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
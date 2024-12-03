from PyQt5.QtWidgets import QMenuBar, QAction, QWidget, QLabel

from passwords_window import PasswordWindow
from filepaths_window import FilepathsWindow

class MenuBar:
    def __init__(self, main_window):
        self.main_window = main_window
        self.menu_bar = self.main_window.menuBar()
        self.create_menu()

    def create_menu(self):
        # Create the Settings menu
        settings_menu = self.menu_bar.addMenu("Settings")

        # Create actions
        passwords_action = QAction("Password(s)", self.main_window)
        filepaths_action = QAction("File Path(s)", self.main_window)

        # Connect actions to methods
        passwords_action.triggered.connect(self.open_passwords_window)
        filepaths_action.triggered.connect(self.open_filepaths_window)

        # Add actions to the menu
        settings_menu.addAction(passwords_action)
        settings_menu.addAction(filepaths_action)

    def open_passwords_window(self):
        print("passwords item clicked")
        self.passwords_window = PasswordWindow()
        self.passwords_window.show()

    def open_filepaths_window(self):
        print("settings item clicked")
        self.filepaths_window = FilepathsWindow()
        self.filepaths_window.show()




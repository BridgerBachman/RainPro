import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Bar Example")
        self.setGeometry(100, 100, 600, 400)

        # Create the menu bar
        menu_bar = self.menuBar()

        # Add "File" menu
        file_menu = menu_bar.addMenu("File")

        # Add "New" action to the File menu
        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        # Add "Open" action to the File menu
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Add a separator
        file_menu.addSeparator()

        # Add "Exit" action to the File menu
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Add "Edit" menu
        edit_menu = menu_bar.addMenu("Edit")

        # Add "Cut" action to the Edit menu
        cut_action = QAction("Cut", self)
        cut_action.triggered.connect(self.cut_text)
        edit_menu.addAction(cut_action)

        # Add "Copy" action to the Edit menu
        copy_action = QAction("Copy", self)
        copy_action.triggered.connect(self.copy_text)
        edit_menu.addAction(copy_action)

        # Add "Paste" action to the Edit menu
        paste_action = QAction("Paste", self)
        paste_action.triggered.connect(self.paste_text)
        edit_menu.addAction(paste_action)

    def new_file(self):
        print("New File Selected")

    def open_file(self):
        print("Open File Selected")

    def cut_text(self):
        print("Cut Selected")

    def copy_text(self):
        print("Copy Selected")

    def paste_text(self):
        print("Paste Selected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

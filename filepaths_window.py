from PyQt5.QtWidgets import QWidget, QLabel

class FilepathsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Filepathsw Window")
        self.setGeometry(200, 200, 300, 200)

        # Label to show in the new window
        label = QLabel("This is a new file paths window!", self)
        label.move(50, 50)
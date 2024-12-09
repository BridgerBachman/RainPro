from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
#This module is in development, passwords must be encyrpted before storing and decrypted when application is loaded, user will be prompted for password 
class PasswordWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Passwords Window")
        self.setGeometry(200, 200, 300, 200)

        # Password field for entering a password
        self.password_field = QLineEdit(self)
        self.password_field.setEchoMode(QLineEdit.Password)  # Hide the text entered

        # Password field for confirming the password
        self.confirm_password_field = QLineEdit(self)
        self.confirm_password_field.setEchoMode(QLineEdit.Password)  # Hide the text entered

        # Save button
        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_password)

        # Layout for the widgets
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Rain Admin:", self))
        layout.addWidget(self.password_field)
        layout.addWidget(QLabel("Google:", self))
        layout.addWidget(self.confirm_password_field)
        layout.addWidget(save_button)

        # Set layout to the window
        self.setLayout(layout)

    def save_password(self):
        # Retrieve the password inputs
        password = self.password_field.text()
        confirm_password = self.confirm_password_field.text()

    def save_to_file(self, password):
        # For example, you can save the password to a text file
        #TODO encrypt passwords before saving using homemade alg fn
        with open("password.txt", "w") as file:
            file.write(password)

# To test the PasswordWindow
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = PasswordWindow()
    window.show()
    sys.exit(app.exec_())

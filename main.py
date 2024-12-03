import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QVBoxLayout, QTextEdit, QAction

from menu_bar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RainPro")
        self.setGeometry(0, 0, 300, 950)

        # Create the central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create the label, input field, and copy button
        crm_label = QLabel("CRM:")
        self.input_field = QLineEdit()
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.copy_to_clipboard)

        # Create the label, input field for name
        name_label = QLabel("Name:")
        self.input_field2 = QLineEdit()

        # Create the label and input field for the Reason
        reason_label = QLabel("Reason:")
        self.reason_input = QTextEdit()  # Make it an instance variable

        # Create the label and input field for the Cause
        cause_label = QLabel("Cause:")
        self.cause_input = QLineEdit()  # Make it an instance variable

        # Resolution
        resolution_label = QLabel("Resolution:")
        self.resolution_input = QTextEdit()  # Make it an instance variable

        # Follow Up Actions
        next_step_label = QLabel("Next Step:")
        self.next_step_input = QLineEdit()  # Make it an instance variable

        # Create the clear all button
        clear_all_fields_button = QPushButton("Clear All")
        clear_all_fields_button.clicked.connect(self.clear_all_fields)  # Pass method reference

        # Adding the name and the input field for customers_name to be horizontal in line with each other
        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(name_label)
        h_layout1.addWidget(self.input_field2)

        # Create the layout for the reason
        v_layout_reason3 = QVBoxLayout()
        v_layout_reason3.addWidget(reason_label)
        v_layout_reason3.addWidget(self.reason_input)

        # Create the layout for the cause
        v_layout_cause4 = QVBoxLayout()
        v_layout_cause4.addWidget(cause_label)
        v_layout_cause4.addWidget(self.cause_input)

        # Resolution layout
        v_layout_resolution5 = QVBoxLayout()
        v_layout_resolution5.addWidget(resolution_label)
        v_layout_resolution5.addWidget(self.resolution_input)

        # Next step layout
        v_layout_next_step6 = QVBoxLayout()
        v_layout_next_step6.addWidget(next_step_label)
        v_layout_next_step6.addWidget(self.next_step_input)

        # Layout for the CRM label, input field, and button
        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(crm_label)
        h_layout2.addWidget(self.input_field)
        h_layout2.addWidget(copy_button)

        #create layout for clear all button
        h_layout_buttons = QHBoxLayout()
        h_layout_buttons.addWidget(clear_all_fields_button)

        # Set the layout to the central widget
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(v_layout_reason3)
        v_layout.addLayout(v_layout_cause4)
        v_layout.addLayout(v_layout_resolution5)
        v_layout.addLayout(v_layout_next_step6)
        v_layout.addLayout(h_layout_buttons)
        central_widget.setLayout(v_layout)

        #menu_bar
        self.menu_bar = MenuBar(self)

    def copy_to_clipboard(self):
        # Copy the text from the input field to the clipboard
        text = self.input_field.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

    def clear_all_fields(self):
        # Clear the name, crm, reason, cause, resolution and next step
        self.input_field.clear()
        self.input_field2.clear()
        self.reason_input.clear()
        self.cause_input.clear()
        self.resolution_input.clear()
        self.next_step_input.clear()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

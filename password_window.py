from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMainWindow, QLineEdit, QApplication,QLabel
from admin_panel import AdWindow


class PWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.a = None
        self.i = 0
        self.setWindowTitle("Password manager")
        self.passowrd = "0000"
        self.setFixedSize(290, 120)
        self.le = QLineEdit()
        self.le.setPlaceholderText("Password")
        self.le.setEchoMode(QLineEdit.Password)
        self.le.setFixedHeight(40)
        btn = QPushButton("OK")
        btn.setFixedHeight(35)
        self.lab = QLabel()
        btn.clicked.connect(self.btn_clicked)
        vl = QVBoxLayout()
        vl.addWidget(self.le)
        vl.addWidget(btn)
        vl.addWidget(self.lab)
        container = QWidget()
        container.setLayout(vl)
        self.setCentralWidget(container)

    def btn_clicked(self):
        print("btn clicked")
        if self.passowrd == self.le.text():
            self.lab.setText("Correct ✅")
            if self.i == 0:
                self.a = AdWindow()
                self.a.show()
                self.i += 1
                # self.hide()
            else:
                print(f"ikkinchi ochilishi")
                # self.a.close()
                # self.a = AdWindow()
                self.a.show()
            self.hide()


        else:
            self.le.clear()
            self.lab.setText("Incorrect ❌")

    def close(self):
        self.le.clear()


# app = QApplication([])
# a = PWindow()
# a.show()
# app.exec()

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMainWindow
from password_window import PWindow
from user_panel import UsrWindow


class MWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.a = None
        self.u = None
        self.i = 0
        self.setWindowTitle("Database")
        admin = QPushButton("Admin")
        user = QPushButton("User")
        admin.setFixedHeight(35)
        user.setFixedHeight(35)
        self.setFixedSize(280, 100)
        admin.clicked.connect(self.admin_clicked)
        user.clicked.connect(self.user_clicked)
        vl = QVBoxLayout()
        vl.addWidget(admin)
        vl.addWidget(user)
        container = QWidget()
        container.setLayout(vl)
        self.setCentralWidget(container)

    def admin_clicked(self):
        self.a = PWindow()
        self.a.show()

        print("Admin clicked")

    def user_clicked(self):
        if self.i == 0:
            self.u = UsrWindow()
            self.i += 1
        self.u.show()

        print("User clicked")

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMainWindow, QLineEdit, QApplication, QLabel
import mysql.connector
from add_panel import AddWindow
conn = mysql.connector.connect(host="localhost",
                               user="root",
                               password="0000",
                               database="bazam")


class AdWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.a = None
        cursor = conn.cursor()
        self.setWindowTitle("Tables")
        self.setFixedSize(300, 300)
        cursor.execute("show tables;")
        result = cursor.fetchall()
        vl = QVBoxLayout()
        self.labs = []
        for row in result:
            btn = QPushButton(f"{row[0].capitalize()}")
            btn.clicked.connect(self.cliks)
            btn.setFixedHeight(int(self.height()/len(result))-5)
            self.labs.append(btn)
            vl.addWidget(btn)
        cursor.close()
        conn.close()
        continer = QWidget()
        continer.setLayout(vl)
        self.setCentralWidget(continer)

    def cliks(self):
        clicked_btn = self.sender().text()
        self.a = AddWindow(clicked_btn)
        self.a.show()
        print(clicked_btn)

    def closeEvent(self, a0):
        self.close()
        self.hide()

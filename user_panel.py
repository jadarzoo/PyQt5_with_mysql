from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMainWindow, QLineEdit, QApplication, QLabel
import mysql.connector
from show_panel import SHowWindow
conn = mysql.connector.connect(host="localhost",
                               user="root",
                               password="0000",
                               database="bazam")


class UsrWindow(QMainWindow):
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
            table_name = row[0]
            btn = QPushButton(f"{table_name.capitalize()}")
            btn.clicked.connect(self.cliks)
            btn.setFixedHeight(int(self.height() / len(result)) - 5)
            self.labs.append((btn, table_name))
            vl.addWidget(btn)
        cursor.close()
        conn.close()
        continer = QWidget()
        continer.setLayout(vl)
        self.setCentralWidget(continer)

    def cliks(self):

        if not self.a is None:
             self.a.close()
        clicked_btn = self.sender()
        print(self.sender())
        for btn, table_name in self.labs:
            if clicked_btn == btn:
                print(clicked_btn)
                self.a = SHowWindow(table_name)
                print(self.a)
                self.a.show()
                print(f"{table_name}")


from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMainWindow, QLineEdit, QApplication, QLabel, \
    QTableWidget, QTextEdit, QTableWidgetItem
import mysql.connector

conn = mysql.connector.connect(host="localhost",
                               user="root",
                               password="0000",
                               database="bazam")


class SHowWindow(QMainWindow):
    def __init__(self, table_name):
        conn = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="0000",
                                       database="bazam")
        super().__init__()
        cursor = conn.cursor()
        self.poin = "*"
        self.table = table_name
        self.setWindowTitle("Result")
        # self.setFixedSize(300, 300)
        cursor.execute(f"select {self.poin} from {self.table};")
        result = cursor.fetchall()
        layout = QVBoxLayout()
        text = ""
        for row in result:
            for el in row:
                text += str(el) + "\t"
            text += "\n"
        print(text)

        self.text_edit = QTextEdit()
        self.setStyleSheet("background-color: blue;")
        self.text_edit.setStyleSheet("color: white;")
        layout.addWidget(self.text_edit)
        self.text_edit.setText(f"{text}")
        self.scrollbar = self.text_edit.verticalScrollBar()

        cursor.close()
        conn.close()
        continer = QWidget()
        continer.setLayout(layout)
        self.setCentralWidget(continer)

    def cliks(self):
        clicked_btn = self.sender()
        print(clicked_btn.text())

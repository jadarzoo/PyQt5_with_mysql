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
        self.setFixedSize(800, 500)
        result = cursor.fetchall()
        layout = QVBoxLayout()
        text = ""
        for row in result:
            for el in row:
                text += str(el) + "\t"
            text += "\n"
        print(text)

        # self.text_edit = QTextEdit()
        # self.setStyleSheet("background-color: blue;")
        # self.text_edit.setStyleSheet("color: white;")
        # layout.addWidget(self.text_edit)
        # self.text_edit.setText(f"{text}")
        # self.scrollbar = self.text_edit.verticalScrollBar()

        w_table = QTableWidget()
        cursor.execute(f"desc {table_name}")
        colum = len(cursor.fetchall())
        w_table.setColumnCount(colum)
        cursor.execute(f"select count(id) from {table_name}")
        rows = cursor.fetchall()
        w_table.setRowCount(rows[0][0])
        print("column", w_table.columnCount(), "row", w_table.rowCount())
        # cursor.execute(f"select {self.poin} from {self.table};")
        cursor.execute(f"DESC {table_name}")
        columns = cursor.fetchall()
        column_names = [col[0] for col in columns]
        w_table.setHorizontalHeaderLabels(column_names)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                w_table.setItem(row_num, col_num, item)

        # w_table.setStyleSheet("background-color: blue;")
        w_table.setStyleSheet("color: red,background-color: blue;")

        layout.addWidget(w_table)

        cursor.close()
        continer = QWidget()
        continer.setLayout(layout)
        self.setCentralWidget(continer)

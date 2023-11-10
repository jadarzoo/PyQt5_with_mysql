import mysqlx
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QLabel, QHBoxLayout, QLineEdit, QPushButton, QMessageBox
import mysql.connector


class AddWindow(QMainWindow):
    def __init__(self, table_name):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000",
            database="bazam"
        )
        super().__init__()
        self.setWindowTitle("Add panel")
        self.cursor = conn.cursor()
        self.table_name = table_name
        amal = f"desc {table_name}"
        self.cursor.execute(amal)
        result = self.cursor.fetchall()
        self.labs = []
        container = QWidget()
        self.setCentralWidget(container)
        main_lay = QVBoxLayout(container)
        layoud = QHBoxLayout()
        main_lay.addLayout(layoud)
        vl = QVBoxLayout()
        layoud.addLayout(vl)
        vl2 = QVBoxLayout()
        layoud.addLayout(vl2)
        for row in result:
            # if row[0] == "id":
            #     continue
            lab = QLabel(str(row[0]).capitalize())
            ledit = QLineEdit()
            ledit.setPlaceholderText(row[1])
            txt = ledit.text()
            print(ledit.text())
            vl2.addWidget(ledit)
            vl.addWidget(lab)
            self.labs.append((lab, ledit))
        print(self.labs)
        self.cursor.close()
        conn.close()
        self.add_btn = QPushButton("Add")
        main_lay.addWidget(self.add_btn)
        self.add_btn.clicked.connect(self.add_click)

    def add_click(self):
        global kursor, konnect
        print("Add button clicked")
        self.add_btn.setStyleSheet("background-color: white;")
        columns = ""
        values = ""
        for labu, leditu in self.labs:
            print(labu.text(), leditu.text())
            txt = leditu.text()
            try:
                columns += labu.text() + ","
                if "varchar" in leditu.placeholderText():
                    txt = "\"" + txt + "\""
                values += txt + ","
            except Exception as e:
                print(f"Istisno: {e}")
        text = f"insert into {self.table_name}({columns[:-1]}) values({values[:-1]});"
        print(text)
        try:
            konnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="0000",
                database="bazam"
            )
            kursor = konnect.cursor()

            kursor.execute(text)
            print("succesfully")
            konnect.commit()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            if kursor:
                kursor.close()
            if konnect:
                konnect.close()

    def xato(self, tex):
        QMessageBox.information(self, 'Information', f"{tex}", QMessageBox.Ok)

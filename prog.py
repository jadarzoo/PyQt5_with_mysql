from PyQt5.QtWidgets import QApplication
from asosiy_window import MWindow
from add_panel import AddWindow
# from password_window import PWindow
import sys
app = QApplication(sys.argv)


window = MWindow()
window.show()
app.exec()

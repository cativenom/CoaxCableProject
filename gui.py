import math

from PySide6.QtWidgets import QApplication, QBoxLayout, QButtonGroup, QFileDialog, QMainWindow, QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView, QLabel, QVBoxLayout, QWidget, QSizePolicy
import sys
import json
from ui_main import Ui_MainWindow
from solver import Solver

MODERN_THEME = """
    QMainWindow { background-color: #1e1e2e; }
    QTabWidget::pane { border: 1px solid #313244; border-radius: 8px; background-color: #1e1e2e; }
    QTabBar::tab { background-color: #181825; color: #cdd6f4; padding: 8px 20px; margin-right: 2px; border-top-left-radius: 8px; border-top-right-radius: 8px; }
    QTabBar::tab:selected { background-color: #313244; font-weight: bold; border-bottom: 2px solid #89b4fa; }
    
    QTableWidget { background-color: #1e1e2e; alternate-background-color: #242436; color: #cdd6f4; gridline-color: #313244; border: none; outline: none; }
    QTableWidget::item:selected { background-color: #89b4fa; color: #11111b; }
    QHeaderView::section { background-color: #313244; color: #cdd6f4; font-weight: bold; padding: 6px; border: none; border-right: 1px solid #45475a; border-bottom: 1px solid #45475a; }
    QHeaderView::section:first { border-top-left-radius: 8px; }
    QHeaderView::section:last { border-top-right-radius: 8px; border-right: none; }


    QPushButton#btn_close_sidebar:hover { background-color: #eba0b3; }

    QLabel { color: #cdd6f4; }
    QLineEdit { background-color: #181825; color: #cdd6f4; border: 1px solid #313244; padding: 8px; border-radius: 4px; }
    QLineEdit:focus { border: 1px solid #89b4fa; }
    QRadioButton { background-color: #89b4fa; color: #11111b; font-weight: bold; padding: 10px; border-radius: 4px; }
    QComboBox { background-color: #89b4fa; color: #11111b; font-weight: bold; padding: 10px; border-radius: 4px; }
    QPushButton { background-color: #89b4fa; color: #11111b; font-weight: bold; padding: 10px; border-radius: 4px; }
    QPushButton:hover { background-color: #74c7ec; }
    QPlainTextEdit { background-color: #11111b; color: #cdd6f4; border: 1px solid #313244; padding: 8px; border-radius: 4px; }
"""

units = ["nm", "mm", "cm", "m",]

class CoaxSolver(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(MODERN_THEME)

        self.ui.solve_btn.clicked.connect(self.solve)


        layout = QVBoxLayout()
        self.setLayout(layout)

        self.buttton_group = QButtonGroup(self)
        self.buttton_group.setExclusive(True)
        self.buttton_group.addButton(self.ui.open_shunt_btn, id=1)
        self.buttton_group.addButton(self.ui.shorted_shunt_btn, id=2)

        with open("data/materials.json", "r") as file:
                data = json.load(file)

        print("-------------- Adding Conductors --------------")
        for conductor in data["conductor"]:
            print(conductor)
            self.ui.conductor_select.addItem(conductor)
            print(data["conductor"][conductor]["sigc"])

        print("-------------- Adding Diaelectics --------------")
        for diaelectric in data["dielectric"]:
            print(diaelectric)
            self.ui.dielectric_select.addItem(diaelectric)

        print("-------------- Adding Units --------------")
        for unit in units:
            print(unit)
            self.ui.a_units.addItem(unit)
            self.ui.b_units.addItem(unit)
            self.ui.c_units.addItem(unit)
            self.ui.length_units.addItem(unit)
        


            
             





    def solve(self):
        conductor=self.ui.conductor_select.currentText()
        diaelectric=self.ui.dielectric_select.currentText()
        solve_type=self.buttton_group.checkedButton().text()
        a=self.ui.a_lineedit.text()
        b=self.ui.b_lineedit.text()
        c=self.ui.c_lineedit.text()
        length=self.ui.l_lineedit.text()
        ReZl=self.ui.real_impedence.text()
        ImZl=self.ui.fake_impedence.text()
        freq=self.ui.freqlineEdit.text()

    
        print("-------------- Solving --------------")
        print(f"{conductor} \n {diaelectric} \n {solve_type} \n {a} \n {b} \n {c} \n {length} \n {ReZl} \n {ImZl} \n {freq}")
        solver = Solver(str(conductor), str(diaelectric), str(solve_type), float(a), float(b), float(b), float(length), float(ReZl), float(ImZl), float(freq))
        Z_o = solver._char_impedance()
        self.ui.fuck.setText(str(truncate(Z_o.imag)))
        self.ui.fuck_2.setText(str(truncate(Z_o.real)))
    





def truncate(num):
    sig_figs = 4
    exponent = math.floor(math.log10(abs(num)))
    places = sig_figs - 1 - exponent
    truncated_num = int(num * (10 ** places)) / (10 ** places)
    return truncated_num

if __name__ == "__main__":
    pyside_app = QApplication(sys.argv)
    window = CoaxSolver()
    window.show()
    sys.exit(pyside_app.exec())
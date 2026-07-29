import math

from PySide6.QtWidgets import QApplication, QBoxLayout, QButtonGroup, QFileDialog, QMainWindow, QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView, QLabel, QVBoxLayout, QWidget, QSizePolicy
import sys
import json
from ui_main import Ui_MainWindow
from solver import Solver
from stubSolver import stubSolver

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

units_meter = ["nm", "mm", "cm", "m",]
units_hz = ["Hz", "kHz", "MHz", "GHz", "THz"]
units_ohm = ["pΩ", "nΩ","muΩ","mΩ", "Ω", "kΩ", "MΩ"]
CONVERT = {
    "nm" : 1e-9, 
    "mm" : 1e-3,
    "cm" : 1e-2,
    "m": 1e1, 
    "Hz" : 1e1,
    "kHz" : 1e3,
    "MHz" : 1e6,
    "GHz" : 1e9,
    "THz" : 1e12, 
    "pΩ" : 1e-12,
    "nΩ" : 1e-9,
    "muΩ": 1e-6,
    "mΩ" : 1e-3,
    "Ω": 1e1,
    "kΩ" : 1e3,
    "MΩ" : 1e6,
}



class CoaxSolver(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(MODERN_THEME)

        self.ui.solve_btn.clicked.connect(self.solve)


        layout = QVBoxLayout()
        self.setLayout(layout)


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
        for unit in units_meter:
            print(unit)
            self.ui.a_units.addItem(unit)
            self.ui.b_units.addItem(unit)
            self.ui.c_units.addItem(unit)
            self.ui.length_units.addItem(unit)
        for unit in units_hz:
            print(unit)
            self.ui.hzUnits.addItem(unit)
        for unit in units_ohm:
            print(unit)
            self.ui.ohmUnits_3.addItem(unit)
            self.ui.ohmUnits.addItem(unit)
        
        

        self.ui.open_shunt_box.addItem("Open")
        self.ui.open_shunt_box.addItem("Shunt")
        self.ui.stub_shunt_box.addItem("Stub")
        self.ui.stub_shunt_box.addItem("Shunt")

        


    def solve(self):
        conductor = self.ui.conductor_select.currentText()
        diaelectric = self.ui.dielectric_select.currentText()
        solve_type = self.ui.open_shunt_box.currentText
        connection_type = self.ui.stub_shunt_box.currentText
        a=self.ui.a_lineedit.text() * CONVERT[self.ui.a_units.text()]
        b=self.ui.b_lineedit.text() * CONVERT[self.ui.b_units.text()]
        c=self.ui.c_lineedit.text() * CONVERT[self.ui.c_units.text()]
        length=self.ui.l_lineedit.text() * CONVERT[self.ui.length_units.text()]
        ReZl=self.ui.real_impedence.text() * CONVERT[self.ui.ohmUnits.text()]
        ImZl=self.ui.fake_impedence.text() * CONVERT[self.ui.ohmUnits.text()]
        freq=self.ui.freqlineEdit.text() * CONVERT[self.ui.hzUnits]
        beta = (2 * math.pi) / float(length)

        checked_id = self.buttton_group.checkedId()
        if checked_id == 2:
            shunt = True 
        elif checked_id == 1:
            shunt = False
        elif checked_id == 3:
            shunt = True
        else:
            shunt = None 

        print("-------------- Solving --------------")
        print(f"{conductor} \n {diaelectric} \n {solve_type} \n {a} \n {b} \n {c} \n {length} \n {ReZl} \n {ImZl} \n {freq}")
        solver = Solver(str(conductor), str(diaelectric), str(solve_type), float(a), float(b), float(c), float(length), float(ReZl), float(ImZl), float(freq))
        Z_o = solver._char_impedance()
        self.ui.char_impedence_fake.setText(str(truncate(Z_o.imag)))
        self.ui.char_impedence_real.setText(str(truncate(Z_o.real)))
        stub = stubSolver(real=float(ReZl), fake=float(ImZl), z0real=Z_o.real, z0fake=Z_o.imag, beta=beta, gamma=1j * beta, length=float(length), short=shunt)

        print(stub.input_impedance())





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
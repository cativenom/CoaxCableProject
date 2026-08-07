import math

from PySide6.QtWidgets import QApplication, QInputDialog, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem, QMessageBox, QWidget
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QBrush, QIcon, QPainterPath, QPen, QColor

import sys
import json
from ui_main import Ui_MainWindow
from solver import Solver
from stubSolver import stubSolver


MODERN_THEME = """
    QMainWindow { background-color: #1e1e2e; }
    
    
    QTableWidget { background-color: #1e1e2e; alternate-background-color: #242436; color: #cdd6f4; gridline-color: #313244; border: none; outline: none; }
    QTableWidget::item:selected { background-color: #89b4fa; color: #11111b; }
    QHeaderView::section { background-color: #313244; color: #cdd6f4; font-weight: bold; padding: 6px; border: none; border-right: 1px solid #45475a; border-bottom: 1px solid #45475a; }
    QHeaderView::section:first { border-top-left-radius: 8px; }
    QHeaderView::section:last { border-top-right-radius: 8px; border-right: none; }
    QInputDialog {background-color: #1e1e2e;}

    
    QMessageBox {background-color: #1e1e2e;}
    QLabel { color: #cdd6f4; }
    QLineEdit { background-color: #181825; color: #cdd6f4; border: 1px solid #313244; padding: 8px; border-radius: 4px; }
    QLineEdit:focus { border: 1px solid #89b4fa; }
    QDoubleSpinBox { background-color: #181825; color: #cdd6f4; border: 1px solid #313244; padding: 8px; border-radius: 4px; }
    QDoubleSpinBox:focus { border: 1px solid #89b4fa; }

    QRadioButton { background-color: #89b4fa; color: #11111b; font-weight: bold; padding: 10px; border-radius: 4px; }
    QComboBox { background-color: #89b4fa; color: #11111b; font-weight: bold; padding: 10px; border-radius: 4px; }
    QPushButton { background-color: #89b4fa; color: #11111b; font-weight: bold; padding: 10px; border-radius: 4px; }
    QPushButton:hover { background-color: #74c7ec; }
    QPlainTextEdit { background-color: #11111b; color: #cdd6f4; border: 1px solid #313244; padding: 8px; border-radius: 4px; }
    QGraphicsView {background-color: #1e1e2e;}
"""

# Written Unit conversion method
units_meter = ["m", "cm", "mm", "µm", "nm"]
units_hz = ["MHz", "Hz", "kHz", "GHz", "THz"]

#Dictionaries were originally only 1 CONVERT dictionary, but were split to simplify scalar conversion when a new scalar of unit was chosen 
CONVERT_M = {"m": 1, "cm" : 1e-2, "mm" : 1e-3, "µm": 1e-6, "nm" : 1e-9, }
CONVERT_Hz = {"Hz" : 1, "kHz" : 1e3, "MHz" : 1e6, "GHz" : 1e9, "THz" : 1e12,}


# CoaxSolver main class
class CoaxSolver(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(MODERN_THEME)

        

        self.scene = QGraphicsScene(self)
        self.wave = QGraphicsScene(self)
        self.circuit = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.wave_view.setScene(self.wave)
        self.ui.circuit_view.setScene(self.circuit)

        for edit in (self.ui.a_lineedit, self.ui.b_lineedit, self.ui.c_lineedit, self.ui.freqlineEdit):
            edit.textChanged.connect(self.update_diagram)
            

        for change in (self.ui.a_units, self.ui.b_units, self.ui.c_units, self.ui.hzUnits):
            # find = lambda i, index =
            change.currentIndexChanged.connect(self.update_diagram)

        for connection_change in (self.ui.termination_box, ):
            connection_change.currentIndexChanged.connect(self.update_diagram)

        self.ui.solve_btn.clicked.connect(self.solve)
        
        # opening relevant json file with needed data
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

        self.ui.conductor_select.currentTextChanged.connect(self.on_conductor_changed)
        self.ui.dielectric_select.currentTextChanged.connect(self.on_diaelectric_changed)

            


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

        #This controls the boxes       
        self.ui.termination_box.addItem("Open")
        self.ui.termination_box.addItem("Shorted")      
            
                
    def update_diagram(self):
        self.wave.clear()
        self.scene.clear()
        self.scene.clear()
        self.circuit.clear()
        self.update_wave()
        self.update_coax()
        self.update_circuit()
        self.update_circuit()


    def update_circuit(self):
        self.draw_circuit()
        pass

    def draw_circuit(self):
        pen = QPen(QColor("#89b4fa"), 2)
        if self.ui.shunt_stub_length.text() != "":
            stub_length = float(self.ui.shunt_stub_length.text())
        else:
            stub_length = 100
        #Horzontal line
        self.circuit.addLine(0, 0, 200, 0, pen=pen)


        self.circuit.addLine(100,0, 100, stub_length, pen=pen)

        #Ground lines
        if self.ui.termination_box.currentText() == "Shorted":
            self.circuit.addLine(95, stub_length+20, 105, stub_length+20, pen=pen)
            self.circuit.addLine(90, stub_length+10, 110, stub_length + 10, pen=pen)
            self.circuit.addLine(80, stub_length, 120, stub_length, pen=pen)

        self.circuit.addRect(200, -12.5, 25, 25, pen)
        self.circuit.addEllipse(-12.5, -12.5, 25, 25, pen=pen)




    def update_wave(self):
        try:
            freq = float(self.ui.freqlineEdit.text()) * CONVERT_Hz[self.ui.hzUnits.currentText()]
        except (ValueError, KeyError):
            print("Error", ValueError, KeyError)
            return 
        print(freq)
        if freq != 0:
            self.draw_wave(freq)


    def draw_wave(self, freq, ampltuide=20, width=200, points=2000):
        print("Drawing Wave")
        path = QPainterPath()
        cycles = max(1, 1 + math.log10(freq/10))
        for i in range(points + 1):
            x = (i/points) * width
            y = ampltuide * math.sin(2*math.pi * cycles * (i/points))
            if i == 0:
                path.moveTo(x,y)
            else:
                path.lineTo(x,y)
        pen = QPen(QColor("#89b4fa"), 2)
        pen.setCosmetic(True)
        self.wave.addPath(path,pen)


        wave_rect = self.wave.itemsBoundingRect()
        self.ui.wave_view.fitInView(wave_rect, Qt.IgnoreAspectRatio)




    def update_coax(self):
        try:
            a = float(self.ui.a_lineedit.text()) * CONVERT_M[self.ui.a_units.currentText()]
            b = float(self.ui.b_lineedit.text()) * CONVERT_M[self.ui.b_units.currentText()]
            c = float(self.ui.c_lineedit.text()) * CONVERT_M[self.ui.b_units.currentText()]   
        except (ValueError, KeyError):
            return 
        self.draw_coax(a, b, c)

    def draw_coax(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return

    
        scale = 200/c #scales to c if was converted it would make the view extremly big
        c = float(self.ui.c_lineedit.text()) * CONVERT_M[self.ui.c_units.currentText()]      

        for radius, fill, edge in ((c, "#B5D4F4", "#185FA5"),(b, "#9FE1CB", "#0F6E56"),(a, "#F5C4B3", "#993C1D")):
            radius_scaled = radius * scale
            self.scene.addEllipse(-radius_scaled, -radius_scaled, 2*radius_scaled, 2* radius_scaled, QPen(QColor(edge), 1), QBrush(QColor(fill)))
        self.ui.graphicsView.fitInView(self.scene.itemsBoundingRect(), Qt.KeepAspectRatio)


    def on_conductor_changed(self, conductor):
        if conductor == "Other":
            sigma_c, ok = QInputDialog.getText(self, "Custom Conductor", "Enter conductor conductivity (σ_c):")

            #ok checks if the user pressed ok (true) or cancel(false) 
            if ok:  
                if sigma_c == "":
                    QMessageBox.warning(self, "Null Error", "No value entered defaulting to known materials")
                    self.ui.conductor_select.setCurrentIndex(0)
                try:
                    self.custom_conductor = float(sigma_c) 
                except ValueError:
                    QMessageBox.warning(self, "NaN Error", "Value entered is not a number defaulting to known materials")
                    self.ui.conductor_select.setCurrentIndex(0)



    def on_diaelectric_changed(self, diaelectric):
        if diaelectric == "Other":
            sigma_d, ok = QInputDialog.getText(self, "Custom Dielectric", "Enter sigma_d:")
            if ok:
                if sigma_d == "":
                    QMessageBox.warning(self, "Null Error", "No value entered defaulting to known materials")
                    self.ui.conductor_select.setCurrentIndex(0) 
                try:
                    self.custom_sigma_d = float(sigma_d)
                except ValueError:
                    QMessageBox.warning(self, "NaN Error", "Value entered is not a number defaulting to known materials")
                    self.ui.dielectric_select.setCurrentIndex(0)
            epsilon_d, ok = QInputDialog.getText(self, "Custom Dielectric", "Enter epsilon_d:")
            if ok:
                if epsilon_d == "":
                    QMessageBox.warning(self, "Null Error", "No value entered defaulting to known materials")
                    self.ui.dielectric_select.setCurrentIndex(0) 
                try:
                    self.custom_epsilon_d = float(epsilon_d)
                except ValueError:
                    QMessageBox.warning(self, "NaN Error", "Value entered is not a number defaulting to known materials")
                    self.ui.dielectric_select.setCurrentIndex(0)
            mu, ok = QInputDialog.getText(self, "Custom Dielectric", "Enter mu:")
            if ok:
                if mu == "":
                    QMessageBox.warning(self, "Null Error", "No value entered defaulting to known materials")
                    self.ui.dielectric_select.setCurrentIndex(0) 
                try:
                    self.custom_mu = float(mu)
                except ValueError:
                    QMessageBox.warning(self, "NaN Error", "Value entered is not a number defaulting to known materials")
                    self.ui.dielectric_select.setCurrentIndex(0)



    #Events fire after an action has occured for example show is when the window becomes visible and resize is when the user resizes the window
    def showEvent(self, event):
        super().showEvent(event)
        self.update_diagram()
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        rect = self.scene.itemsBoundingRect()
        if not rect.isNull():
            self.ui.graphicsView.fitInView(rect, Qt.KeepAspectRatio)

        wave_rect = self.wave.itemsBoundingRect()
        if not wave_rect.isNull():
            self.ui.wave_view.fitInView(wave_rect, Qt.IgnoreAspectRatio)
    


    def solve(self):
        conductor = self.ui.conductor_select.currentText()
        diaelectric = self.ui.dielectric_select.currentText()
        termination_type = self.ui.termination_box.currentText()
        connection_type = "Shunt"


        a=float(self.ui.a_lineedit.text()) 
        if a == 0:
            QMessageBox.warning(self, "Zero Error", "Inner conductor cannot be zero")
            return 0

        a = a * CONVERT_M[self.ui.a_units.currentText()]
        b = float(self.ui.b_lineedit.text()) 
        if b == 0:
            QMessageBox.warning(self, "Zero Error", "Outer conductor cannot be zero")
            return 0
        b = b * CONVERT_M[self.ui.b_units.currentText()]
        c = float(self.ui.c_lineedit.text())
        if c == 0:
            QMessageBox.warning(self, "Zero Error", "C cannot be zero")
            return 0
        c = c * CONVERT_M[self.ui.c_units.currentText()]

        if a >= b:
            QMessageBox.warning(self, "Error", "Inner conductor cannot be larger than outer conductor")
            return 0
        if b >= c:
            QMessageBox.warning(self, "Error", "Outer conductor cannot be larger than C")
            return 0
        if a >= c:
            QMessageBox.warning(self, "Error", "Inner conductor cannot be larger than C")
            return 0
        if a <= 0 or b <= 0 or c <= 0:
            QMessageBox.warning(self, "Error", "All dimensions must be greater than zero")
            return 0

        length=float(self.ui.l_lineedit.text())
        if length <= 0:
            QMessageBox.warning(self, "Zero Error", "Length cannot be zero")
            return 0
        length = length * CONVERT_M[self.ui.length_units.currentText()]
        ReZl=float(self.ui.real_impedence.text()) 
        ImZl=float(self.ui.fake_impedence.text())
        if ReZl == 0 and ImZl == 0:
            QMessageBox.warning(self, "Zero Error", "Impedance cannot be zero")
            return 0
        freq = float(self.ui.freqlineEdit.text()) 
        if freq == 0:
            QMessageBox.warning(self, "Zero Error", "Frequency cannot be zero")
            return 0
        freq = freq* CONVERT_Hz[self.ui.hzUnits.currentText()]

                
        print("-------------- Solving --------------")
        print(f"{conductor} \n {diaelectric} \n {termination_type} \n {a} \n {b} \n {c} \n {length} \n {ReZl} \n {ImZl} \n {freq}")


        if conductor != "Other" and diaelectric != "Other":
            print("Solving with no custom materials")
            solver = Solver(str(conductor), str(diaelectric), str(termination_type), float(a), float(b), float(ReZl), float(ImZl), float(freq))

        elif conductor == "Other" and diaelectric != "Other":
            print("Solving with custom conductor")
            solver = Solver(None, str(diaelectric), str(termination_type), float(a), float(b), float(ReZl), float(ImZl), float(freq), sigc=self.custom_conductor)

        elif conductor != "Other" and diaelectric == "Other":
            print("Solving with custom diaelectric")
            solver = Solver(str(conductor), None, str(termination_type), float(a), float(b), float(ReZl), float(ImZl), float(freq), sigd=self.custom_sigma_d, epd=self.custom_epsilon_d, mur=self.custom_mu)   

        elif conductor == "Other" and diaelectric == "Other":
            print("Solving with custom conductor and dielectric")
            solver = Solver(None, None, str(termination_type), float(a), float(b), float(c), float(ImZl), float(freq), sigc=self.custom_conductor, sigd=self.custom_sigma_d, epd=self.custom_epsilon_d, mur=self.custom_mu)

        solver.solve()
        Z_o = solver.z0

    

        gain = solver._gain()
        reflection = solver._ref_coeff()
        vswr = solver._VSWR()

        self.ui.char_impedence_fake.setText(str(truncate(Z_o.imag)))
        self.ui.char_impedence_real.setText(str(truncate(Z_o.real)))
        self.ui.vswr.setText(str(truncate(vswr)))
        self.ui.reflection.setText(str(complex(truncate(reflection.real), truncate(reflection.imag))))
        self.ui.gain.setText(str(truncate(gain)))

        match termination_type:
            case "Open":
                short = False
            
            case "Shorted":   
                short = True
                
            case _:
                print("No connection type selected")
                QMessageBox.warning(self, "NaN Error", "No connection type selected")
    

        # solving for shunt stub
        stub = stubSolver(real=float(ReZl), fake=float(ImZl), z0real=Z_o.real, z0fake=Z_o.imag,
                                    beta=solver.gamma.imag, alpha=solver.gamma.real, gamma=solver.gamma, length=float(length), short=short)
        z_stub = stub.input_impedance()
        z_l = complex(float(z_stub.real), float(z_stub.imag))
        y_l = 1/z_l
        y_stub_target = complex(0, -y_l.imag)
        print("z_target:" + str(ReZl))
        print("z_target:" + str(ImZl))
        (1.9859807272318277e-07+2.0108028120943912e-07j)
        (0.04008027389358085+31.507488753927568j)
        print("gamma:" + str(solver.gamma))
        print("z_stub:" + str(z_stub))
        print("y_l:" + str(y_l))
        print("z_l:" + str(z_l))
        print("y_stub:" + str(y_stub_target))
        
        if connection_type == "Series":
            z_input = z_l + z_stub
            self.ui.input_impedence_real.setText(str(truncate(z_input.real))) #truncate doesn't work?S
            self.ui.input_impedence_fake.setText(str(truncate(z_input.imag)))
        elif connection_type == "Shunt":
            y_total = (1/z_l) + (1/z_stub)
            z_input = 1/y_total
            self.ui.input_impedence_real.setText(str(truncate(z_input.real)))
            self.ui.input_impedence_fake.setText(str(truncate(z_input.imag)))
            print("z_input:" + str(z_input))
        
        if y_stub_target == 0:
            z_stub_target = None
        else:
            z_stub_target = 1/y_stub_target
        
        if z_stub_target is not None:
            lossy, lossless, delta = stub.required_length(Z_o.imag)
            self.ui.shunt_stub_length.setText(str(lossy))
        else:
            self.ui.shunt_stub_length.setText("0")

        self.update_diagram()


# helper function to truncate ending zeroes to be only a couple decimal points
def truncate(num):
    if num == 0:
        return num
    sig_figs = 4
    exponent = math.floor(math.log10(abs(num)))
    places = sig_figs - 1 - exponent
    # print("NUM: " + str(num))
    # print("PLACES: " + str(places))
    
    # Hey Zack, this is the fixed truncate. It was just an incorrect division/multiplication
    if exponent > 3: 
        truncated_num = int(num / (10))
    elif exponent > -1:
        return int(num)
    else:
        truncated_num = int(num * (10))
    
    # Hey Zack, here's just a simple if case that states that if the real/imaginary
    # is really small in comparison to an exponent to the -9th, it will set it to zero
    # if num < (10 ** -15):
    #     return 0
    
    return truncated_num

if __name__ == "__main__":
    pyside_app = QApplication(sys.argv)
    window = CoaxSolver()
    window.setWindowTitle("Coax Cable Solver")
    window.show()


    #Starter Values so the user sees the diagram
    window.ui.a_lineedit.setValue(1.00)
    window.ui.b_lineedit.setValue(2.00)
    window.ui.c_lineedit.setValue(3.00)
    window.ui.freqlineEdit.setValue(1.00)
    window.ui.fake_impedence.setValue(1.00)
    window.ui.real_impedence.setValue(1.00)
    window.ui.l_lineedit.setValue(1.00)

    sys.exit(pyside_app.exec())

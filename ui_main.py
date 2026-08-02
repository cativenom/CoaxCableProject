# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGraphicsView,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(986, 682)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.freqlineEdit = QDoubleSpinBox(self.centralwidget)
        self.freqlineEdit.setObjectName(u"freqlineEdit")
        self.freqlineEdit.setMinimum(1.000000000000000)
        self.freqlineEdit.setMaximum(100.000000000000000)

        self.horizontalLayout_4.addWidget(self.freqlineEdit)

        self.hzUnits = QComboBox(self.centralwidget)
        self.hzUnits.setObjectName(u"hzUnits")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hzUnits.sizePolicy().hasHeightForWidth())
        self.hzUnits.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.hzUnits)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.conductor_select = QComboBox(self.centralwidget)
        self.conductor_select.setObjectName(u"conductor_select")
        sizePolicy.setHeightForWidth(self.conductor_select.sizePolicy().hasHeightForWidth())
        self.conductor_select.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.conductor_select)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.dielectric_select = QComboBox(self.centralwidget)
        self.dielectric_select.setObjectName(u"dielectric_select")
        sizePolicy.setHeightForWidth(self.dielectric_select.sizePolicy().hasHeightForWidth())
        self.dielectric_select.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.dielectric_select)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.real_impedence = QDoubleSpinBox(self.centralwidget)
        self.real_impedence.setObjectName(u"real_impedence")
        self.real_impedence.setMinimum(-100.000000000000000)
        self.real_impedence.setMaximum(100.000000000000000)

        self.horizontalLayout_3.addWidget(self.real_impedence)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.fake_impedence = QDoubleSpinBox(self.centralwidget)
        self.fake_impedence.setObjectName(u"fake_impedence")
        self.fake_impedence.setMinimum(-100.000000000000000)
        self.fake_impedence.setMaximum(100.000000000000000)

        self.horizontalLayout_3.addWidget(self.fake_impedence)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(98, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_27)

        self.a_lineedit = QDoubleSpinBox(self.centralwidget)
        self.a_lineedit.setObjectName(u"a_lineedit")
        self.a_lineedit.setMinimum(1.000000000000000)
        self.a_lineedit.setMaximum(100.000000000000000)

        self.horizontalLayout_2.addWidget(self.a_lineedit)

        self.a_units = QComboBox(self.centralwidget)
        self.a_units.setObjectName(u"a_units")
        sizePolicy.setHeightForWidth(self.a_units.sizePolicy().hasHeightForWidth())
        self.a_units.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.a_units)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.label_26)

        self.b_lineedit = QDoubleSpinBox(self.centralwidget)
        self.b_lineedit.setObjectName(u"b_lineedit")
        self.b_lineedit.setMinimum(1.000000000000000)
        self.b_lineedit.setMaximum(100.000000000000000)

        self.horizontalLayout_10.addWidget(self.b_lineedit)

        self.b_units = QComboBox(self.centralwidget)
        self.b_units.setObjectName(u"b_units")
        sizePolicy.setHeightForWidth(self.b_units.sizePolicy().hasHeightForWidth())
        self.b_units.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.b_units)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.label_2)

        self.c_lineedit = QDoubleSpinBox(self.centralwidget)
        self.c_lineedit.setObjectName(u"c_lineedit")
        self.c_lineedit.setMinimum(1.000000000000000)
        self.c_lineedit.setMaximum(100.000000000000000)

        self.horizontalLayout_9.addWidget(self.c_lineedit)

        self.c_units = QComboBox(self.centralwidget)
        self.c_units.setObjectName(u"c_units")
        sizePolicy.setHeightForWidth(self.c_units.sizePolicy().hasHeightForWidth())
        self.c_units.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.c_units)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_3)

        self.l_lineedit = QDoubleSpinBox(self.centralwidget)
        self.l_lineedit.setObjectName(u"l_lineedit")
        self.l_lineedit.setMinimum(1.000000000000000)
        self.l_lineedit.setMaximum(100.000000000000000)

        self.horizontalLayout.addWidget(self.l_lineedit)

        self.length_units = QComboBox(self.centralwidget)
        self.length_units.setObjectName(u"length_units")
        sizePolicy.setHeightForWidth(self.length_units.sizePolicy().hasHeightForWidth())
        self.length_units.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.length_units)


        self.horizontalLayout_21.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_21)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.wave_view = QGraphicsView(self.centralwidget)
        self.wave_view.setObjectName(u"wave_view")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wave_view.sizePolicy().hasHeightForWidth())
        self.wave_view.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.wave_view)

        self.circuit_view = QGraphicsView(self.centralwidget)
        self.circuit_view.setObjectName(u"circuit_view")
        sizePolicy1.setHeightForWidth(self.circuit_view.sizePolicy().hasHeightForWidth())
        self.circuit_view.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.circuit_view)


        self.horizontalLayout_22.addLayout(self.verticalLayout_3)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_22.addWidget(self.graphicsView)


        self.verticalLayout_4.addLayout(self.horizontalLayout_22)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.termination_box = QComboBox(self.centralwidget)
        self.termination_box.setObjectName(u"termination_box")

        self.horizontalLayout_6.addWidget(self.termination_box)

        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_6.addWidget(self.label_25)

        self.solve_btn = QPushButton(self.centralwidget)
        self.solve_btn.setObjectName(u"solve_btn")

        self.horizontalLayout_6.addWidget(self.solve_btn)

        self.horizontalSpacer = QSpacerItem(468, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.char_impedence_real = QLineEdit(self.centralwidget)
        self.char_impedence_real.setObjectName(u"char_impedence_real")
        self.char_impedence_real.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.char_impedence_real)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.char_impedence_fake = QLineEdit(self.centralwidget)
        self.char_impedence_fake.setObjectName(u"char_impedence_fake")
        self.char_impedence_fake.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.char_impedence_fake)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.input_impedence_real = QLineEdit(self.centralwidget)
        self.input_impedence_real.setObjectName(u"input_impedence_real")
        self.input_impedence_real.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.input_impedence_real)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)

        self.input_impedence_fake = QLineEdit(self.centralwidget)
        self.input_impedence_fake.setObjectName(u"input_impedence_fake")
        self.input_impedence_fake.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.input_impedence_fake)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.shunt_stub_length = QLineEdit(self.centralwidget)
        self.shunt_stub_length.setObjectName(u"shunt_stub_length")
        self.shunt_stub_length.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.shunt_stub_length)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_13.addWidget(self.label_24)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_17.addWidget(self.label_23)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_15.addWidget(self.label_20)

        self.reflection = QLineEdit(self.centralwidget)
        self.reflection.setObjectName(u"reflection")
        self.reflection.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.reflection)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_16.addWidget(self.label_19)

        self.vswr = QLineEdit(self.centralwidget)
        self.vswr.setObjectName(u"vswr")
        self.vswr.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.vswr)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_14.addWidget(self.label_21)

        self.gain = QLineEdit(self.centralwidget)
        self.gain.setObjectName(u"gain")
        self.gain.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.gain)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_14.addWidget(self.label_22)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 986, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Frequency = ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Conductor", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Dielectric", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Z<sub>L = ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"+ j", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Inner Conductor Radius = ", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Outer Conductor Radius = ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"c = ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Length =", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Solve for", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Shunt", None))
        self.solve_btn.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Z<sub>o = ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"+ j", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Z<sub>in = ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"+ j", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Shunt Stub Length = </p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Unmatched Line:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0393 =</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>VSWR =</p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Gain =</p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"dB", None))
    # retranslateUi


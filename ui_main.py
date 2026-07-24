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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1232, 637)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.freqlineEdit = QLineEdit(self.centralwidget)
        self.freqlineEdit.setObjectName(u"freqlineEdit")

        self.horizontalLayout_4.addWidget(self.freqlineEdit)

        self.hzUnits = QComboBox(self.centralwidget)
        self.hzUnits.setObjectName(u"hzUnits")

        self.horizontalLayout_4.addWidget(self.hzUnits)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.conductor_select = QComboBox(self.centralwidget)
        self.conductor_select.setObjectName(u"conductor_select")

        self.horizontalLayout_7.addWidget(self.conductor_select)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.dielectric_select = QComboBox(self.centralwidget)
        self.dielectric_select.setObjectName(u"dielectric_select")

        self.horizontalLayout_7.addWidget(self.dielectric_select)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.real_impedence = QLineEdit(self.centralwidget)
        self.real_impedence.setObjectName(u"real_impedence")

        self.horizontalLayout_3.addWidget(self.real_impedence)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.fake_impedence = QLineEdit(self.centralwidget)
        self.fake_impedence.setObjectName(u"fake_impedence")

        self.horizontalLayout_3.addWidget(self.fake_impedence)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.a_lineedit = QLineEdit(self.centralwidget)
        self.a_lineedit.setObjectName(u"a_lineedit")

        self.horizontalLayout_2.addWidget(self.a_lineedit)

        self.a_units = QComboBox(self.centralwidget)
        self.a_units.setObjectName(u"a_units")

        self.horizontalLayout_2.addWidget(self.a_units)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.b_lineedit = QLineEdit(self.centralwidget)
        self.b_lineedit.setObjectName(u"b_lineedit")

        self.horizontalLayout_8.addWidget(self.b_lineedit)

        self.b_units = QComboBox(self.centralwidget)
        self.b_units.setObjectName(u"b_units")

        self.horizontalLayout_8.addWidget(self.b_units)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.c_lineedit = QLineEdit(self.centralwidget)
        self.c_lineedit.setObjectName(u"c_lineedit")

        self.horizontalLayout_9.addWidget(self.c_lineedit)

        self.c_units = QComboBox(self.centralwidget)
        self.c_units.setObjectName(u"c_units")

        self.horizontalLayout_9.addWidget(self.c_units)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.l_lineedit = QLineEdit(self.centralwidget)
        self.l_lineedit.setObjectName(u"l_lineedit")

        self.horizontalLayout.addWidget(self.l_lineedit)

        self.length_units = QComboBox(self.centralwidget)
        self.length_units.setObjectName(u"length_units")

        self.horizontalLayout.addWidget(self.length_units)


        self.horizontalLayout_10.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.N = QRadioButton(self.centralwidget)
        self.N.setObjectName(u"N")

        self.horizontalLayout_6.addWidget(self.N)

        self.shorted_shunt_btn = QRadioButton(self.centralwidget)
        self.shorted_shunt_btn.setObjectName(u"shorted_shunt_btn")

        self.horizontalLayout_6.addWidget(self.shorted_shunt_btn)

        self.both_btn = QRadioButton(self.centralwidget)
        self.both_btn.setObjectName(u"both_btn")

        self.horizontalLayout_6.addWidget(self.both_btn)

        self.open_shunt_btn = QRadioButton(self.centralwidget)
        self.open_shunt_btn.setObjectName(u"open_shunt_btn")
        self.open_shunt_btn.setChecked(True)

        self.horizontalLayout_6.addWidget(self.open_shunt_btn)

        self.solve_btn = QPushButton(self.centralwidget)
        self.solve_btn.setObjectName(u"solve_btn")

        self.horizontalLayout_6.addWidget(self.solve_btn)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer = QSpacerItem(258, 22, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

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

        self.ohmUnits = QComboBox(self.centralwidget)
        self.ohmUnits.setObjectName(u"ohmUnits")

        self.horizontalLayout_5.addWidget(self.ohmUnits)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1232, 20))
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
        self.freqlineEdit.setText(QCoreApplication.translate("MainWindow", u"1000000000", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Conductor", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Dielectric", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Z_L = ", None))
        self.real_impedence.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"+ j", None))
        self.fake_impedence.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ohms", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"a = ", None))
        self.a_lineedit.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"b = ", None))
        self.b_lineedit.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"c = ", None))
        self.c_lineedit.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"l = ", None))
        self.l_lineedit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.N.setText(QCoreApplication.translate("MainWindow", u"Neither", None))
        self.shorted_shunt_btn.setText(QCoreApplication.translate("MainWindow", u"Shorted Shunt", None))
        self.both_btn.setText(QCoreApplication.translate("MainWindow", u"Both", None))
        self.open_shunt_btn.setText(QCoreApplication.translate("MainWindow", u"Open Shunt", None))
        self.solve_btn.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Z_o = ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"+ j", None))
    # retranslateUi


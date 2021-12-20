# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ccGUIFBTXkO.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 327)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.vL = QVBoxLayout()
        self.vL.setObjectName(u"vL")
        self.hl1 = QHBoxLayout()
        self.hl1.setObjectName(u"hl1")
        self.l_amount = QLabel(self.centralwidget)
        self.l_amount.setObjectName(u"l_amount")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_amount.sizePolicy().hasHeightForWidth())
        self.l_amount.setSizePolicy(sizePolicy1)

        self.hl1.addWidget(self.l_amount)

        self.dsb_amount = QDoubleSpinBox(self.centralwidget)
        self.dsb_amount.setObjectName(u"dsb_amount")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dsb_amount.sizePolicy().hasHeightForWidth())
        self.dsb_amount.setSizePolicy(sizePolicy2)

        self.hl1.addWidget(self.dsb_amount)

        self.l_from = QLabel(self.centralwidget)
        self.l_from.setObjectName(u"l_from")
        sizePolicy1.setHeightForWidth(self.l_from.sizePolicy().hasHeightForWidth())
        self.l_from.setSizePolicy(sizePolicy1)

        self.hl1.addWidget(self.l_from)

        self.le_from = QLineEdit(self.centralwidget)
        self.le_from.setObjectName(u"le_from")

        self.hl1.addWidget(self.le_from)

        self.l_to = QLabel(self.centralwidget)
        self.l_to.setObjectName(u"l_to")

        self.hl1.addWidget(self.l_to)

        self.le_to = QLineEdit(self.centralwidget)
        self.le_to.setObjectName(u"le_to")

        self.hl1.addWidget(self.le_to)

        self.pb_convert = QPushButton(self.centralwidget)
        self.pb_convert.setObjectName(u"pb_convert")

        self.hl1.addWidget(self.pb_convert)


        self.vL.addLayout(self.hl1)

        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")

        self.vL.addLayout(self.hl2)

        self.te_result = QTextEdit(self.centralwidget)
        self.te_result.setObjectName(u"te_result")

        self.vL.addWidget(self.te_result)

        self.hl3 = QHBoxLayout()
        self.hl3.setObjectName(u"hl3")
        self.pb_exit = QPushButton(self.centralwidget)
        self.pb_exit.setObjectName(u"pb_exit")

        self.hl3.addWidget(self.pb_exit)

        self.pb_reset = QPushButton(self.centralwidget)
        self.pb_reset.setObjectName(u"pb_reset")

        self.hl3.addWidget(self.pb_reset)


        self.vL.addLayout(self.hl3)


        self.gridLayout_2.addLayout(self.vL, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pb_exit.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.l_amount.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.l_from.setText(QCoreApplication.translate("MainWindow", u"Currency From:", None))
        self.l_to.setText(QCoreApplication.translate("MainWindow", u"Currencies To:", None))
        self.pb_convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.pb_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pb_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi


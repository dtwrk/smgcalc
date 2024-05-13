# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'khmt_smg_gui_v2lIKFKN.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(370, 325)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 81, 31))
        self.grid_sred_percent = QGridLayout(self.gridLayoutWidget)
        self.grid_sred_percent.setObjectName(u"grid_sred_percent")
        self.grid_sred_percent.setContentsMargins(0, 0, 0, 0)
        self.label_sred_percent = QLabel(self.gridLayoutWidget)
        self.label_sred_percent.setObjectName(u"label_sred_percent")
        self.label_sred_percent.setFrameShape(QFrame.NoFrame)

        self.grid_sred_percent.addWidget(self.label_sred_percent, 0, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 30, 81, 31))
        self.grid_volume_l = QGridLayout(self.gridLayoutWidget_2)
        self.grid_volume_l.setObjectName(u"grid_volume_l")
        self.grid_volume_l.setContentsMargins(0, 0, 0, 0)
        self.label_volume_l = QLabel(self.gridLayoutWidget_2)
        self.label_volume_l.setObjectName(u"label_volume_l")

        self.grid_volume_l.addWidget(self.label_volume_l, 0, 0, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 60, 81, 31))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 90, 81, 31))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.gridLayoutWidget_5 = QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 120, 81, 31))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.gridLayoutWidget_6 = QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 150, 81, 31))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.gridLayoutWidget_7 = QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(80, 0, 61, 31))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_left_value_perc = QLabel(self.gridLayoutWidget_7)
        self.label_left_value_perc.setObjectName(u"label_left_value_perc")

        self.gridLayout_5.addWidget(self.label_left_value_perc, 0, 0, 1, 1)

        self.gridLayoutWidget_8 = QWidget(self.centralwidget)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(80, 30, 61, 31))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_left_value_l = QLabel(self.gridLayoutWidget_8)
        self.label_left_value_l.setObjectName(u"label_left_value_l")

        self.gridLayout_6.addWidget(self.label_left_value_l, 0, 0, 1, 1)

        self.gridLayoutWidget_9 = QWidget(self.centralwidget)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(80, 60, 61, 31))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.entry_bank1_perc = QLineEdit(self.gridLayoutWidget_9)
        self.entry_bank1_perc.setObjectName(u"entry_bank1_perc")

        self.gridLayout_7.addWidget(self.entry_bank1_perc, 0, 0, 1, 1)

        self.gridLayoutWidget_10 = QWidget(self.centralwidget)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(80, 90, 61, 31))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.entry_bank1_l = QLineEdit(self.gridLayoutWidget_10)
        self.entry_bank1_l.setObjectName(u"entry_bank1_l")

        self.gridLayout_8.addWidget(self.entry_bank1_l, 0, 0, 1, 1)

        self.gridLayoutWidget_11 = QWidget(self.centralwidget)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(80, 120, 61, 31))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.entry_bank2_perc = QLineEdit(self.gridLayoutWidget_11)
        self.entry_bank2_perc.setObjectName(u"entry_bank2_perc")

        self.gridLayout_9.addWidget(self.entry_bank2_perc, 0, 0, 1, 1)

        self.gridLayoutWidget_12 = QWidget(self.centralwidget)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(80, 150, 61, 31))
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.entry_bank2_l = QLineEdit(self.gridLayoutWidget_12)
        self.entry_bank2_l.setObjectName(u"entry_bank2_l")

        self.gridLayout_10.addWidget(self.entry_bank2_l, 0, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(140, 0, 16, 181))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_13 = QWidget(self.centralwidget)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(159, 0, 141, 31))
        self.gridLayout_11 = QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget_13)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1)

        self.gridLayoutWidget_14 = QWidget(self.centralwidget)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(160, 30, 141, 31))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget_14)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        self.label_7.setFont(font1)

        self.gridLayout_12.addWidget(self.label_7, 0, 0, 1, 1)

        self.gridLayoutWidget_15 = QWidget(self.centralwidget)
        self.gridLayoutWidget_15.setObjectName(u"gridLayoutWidget_15")
        self.gridLayoutWidget_15.setGeometry(QRect(160, 60, 201, 31))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_15)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_16 = QWidget(self.centralwidget)
        self.gridLayoutWidget_16.setObjectName(u"gridLayoutWidget_16")
        self.gridLayoutWidget_16.setGeometry(QRect(160, 90, 140, 31))
        self.gridLayout_14 = QGridLayout(self.gridLayoutWidget_16)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget_16)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_14.addWidget(self.label_8, 0, 0, 1, 1)

        self.gridLayoutWidget_17 = QWidget(self.centralwidget)
        self.gridLayoutWidget_17.setObjectName(u"gridLayoutWidget_17")
        self.gridLayoutWidget_17.setGeometry(QRect(160, 120, 141, 31))
        self.gridLayout_15 = QGridLayout(self.gridLayoutWidget_17)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.gridLayoutWidget_17)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_15.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 160, 121, 17))
        self.gridLayoutWidget_18 = QWidget(self.centralwidget)
        self.gridLayoutWidget_18.setObjectName(u"gridLayoutWidget_18")
        self.gridLayoutWidget_18.setGeometry(QRect(160, 150, 141, 31))
        self.gridLayout_16 = QGridLayout(self.gridLayoutWidget_18)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_19 = QWidget(self.centralwidget)
        self.gridLayoutWidget_19.setObjectName(u"gridLayoutWidget_19")
        self.gridLayoutWidget_19.setGeometry(QRect(300, 0, 61, 31))
        self.gridLayout_17 = QGridLayout(self.gridLayoutWidget_19)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.entry_value_perc = QLineEdit(self.gridLayoutWidget_19)
        self.entry_value_perc.setObjectName(u"entry_value_perc")

        self.gridLayout_17.addWidget(self.entry_value_perc, 0, 0, 1, 1)

        self.gridLayoutWidget_20 = QWidget(self.centralwidget)
        self.gridLayoutWidget_20.setObjectName(u"gridLayoutWidget_20")
        self.gridLayoutWidget_20.setGeometry(QRect(300, 30, 61, 31))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget_20)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.entry_value_l = QLineEdit(self.gridLayoutWidget_20)
        self.entry_value_l.setObjectName(u"entry_value_l")

        self.gridLayout_18.addWidget(self.entry_value_l, 0, 0, 1, 1)

        self.gridLayoutWidget_21 = QWidget(self.centralwidget)
        self.gridLayoutWidget_21.setObjectName(u"gridLayoutWidget_21")
        self.gridLayoutWidget_21.setGeometry(QRect(300, 90, 61, 31))
        self.gridLayout_19 = QGridLayout(self.gridLayoutWidget_21)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_value_abssp_l = QLabel(self.gridLayoutWidget_21)
        self.label_value_abssp_l.setObjectName(u"label_value_abssp_l")

        self.gridLayout_19.addWidget(self.label_value_abssp_l, 0, 0, 1, 1)

        self.gridLayoutWidget_22 = QWidget(self.centralwidget)
        self.gridLayoutWidget_22.setObjectName(u"gridLayoutWidget_22")
        self.gridLayoutWidget_22.setGeometry(QRect(300, 120, 61, 31))
        self.gridLayout_20 = QGridLayout(self.gridLayoutWidget_22)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_value_addwater_l = QLabel(self.gridLayoutWidget_22)
        self.label_value_addwater_l.setObjectName(u"label_value_addwater_l")

        self.gridLayout_20.addWidget(self.label_value_addwater_l, 0, 0, 1, 1)

        self.gridLayoutWidget_23 = QWidget(self.centralwidget)
        self.gridLayoutWidget_23.setObjectName(u"gridLayoutWidget_23")
        self.gridLayoutWidget_23.setGeometry(QRect(300, 150, 61, 31))
        self.gridLayout_21 = QGridLayout(self.gridLayoutWidget_23)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_all_in_tank = QLabel(self.gridLayoutWidget_23)
        self.label_all_in_tank.setObjectName(u"label_all_in_tank")

        self.gridLayout_21.addWidget(self.label_all_in_tank, 0, 0, 1, 1)

        self.gridLayoutWidget_24 = QWidget(self.centralwidget)
        self.gridLayoutWidget_24.setObjectName(u"gridLayoutWidget_24")
        self.gridLayoutWidget_24.setGeometry(QRect(0, 180, 141, 31))
        self.gridLayout_22 = QGridLayout(self.gridLayoutWidget_24)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.pushButton_mix = QPushButton(self.gridLayoutWidget_24)
        self.pushButton_mix.setObjectName(u"pushButton_mix")

        self.gridLayout_22.addWidget(self.pushButton_mix, 0, 0, 1, 1)

        self.gridLayoutWidget_25 = QWidget(self.centralwidget)
        self.gridLayoutWidget_25.setObjectName(u"gridLayoutWidget_25")
        self.gridLayoutWidget_25.setGeometry(QRect(160, 180, 201, 31))
        self.gridLayout_23 = QGridLayout(self.gridLayoutWidget_25)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pushButton_calculate = QPushButton(self.gridLayoutWidget_25)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")

        self.gridLayout_23.addWidget(self.pushButton_calculate, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 370, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440 \u0441\u0430\u043c\u043e\u0433\u043e\u043d\u0449\u0438\u043a\u0430 v 0.2 \u043e\u0442 KhMt", None))
        self.label_sred_percent.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439, %:", None))
        self.label_volume_l.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u043c, \u043b:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043d\u043a\u0430 1, %:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043d\u043a\u0430 1, \u043b:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043d\u043a\u0430 2, %:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043d\u043a\u0430 2, \u043b:", None))
        self.label_left_value_perc.setText("")
        self.label_left_value_l.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439, %:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u043c, \u043b:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0431\u0441\u043e\u043b\u044e\u0442\u043d\u043e\u0433\u043e \u0441\u043f\u0438\u0440\u0442\u0430, \u043b:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u043e\u0434\u044b, \u043b:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e \u0432 \u0431\u0430\u043a\u0435 20%, \u043b:", None))
        self.label_value_abssp_l.setText("")
        self.label_value_addwater_l.setText("")
        self.label_all_in_tank.setText("")
        self.pushButton_mix.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0448\u0430\u0442\u044c ->", None))
        self.pushButton_calculate.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
    # retranslateUi


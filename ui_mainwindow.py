# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(350, 500)
        MainWindow.setMinimumSize(QSize(350, 500))
        MainWindow.setMaximumSize(QSize(350, 500))
        self.actiondddd = QAction(MainWindow)
        self.actiondddd.setObjectName(u"actiondddd")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QSize(350, 500))
        self.widget.setMaximumSize(QSize(350, 500))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.memoryLayout = QHBoxLayout()
        self.memoryLayout.setObjectName(u"memoryLayout")
        self.memoryLayout.setContentsMargins(-1, 10, -1, 10)
        self.mcPushButton = QPushButton(self.widget)
        self.memoryButtonGroup = QButtonGroup(MainWindow)
        self.memoryButtonGroup.setObjectName(u"memoryButtonGroup")
        self.memoryButtonGroup.addButton(self.mcPushButton)
        self.mcPushButton.setObjectName(u"mcPushButton")

        self.memoryLayout.addWidget(self.mcPushButton)

        self.mrPushButton = QPushButton(self.widget)
        self.memoryButtonGroup.addButton(self.mrPushButton)
        self.mrPushButton.setObjectName(u"mrPushButton")

        self.memoryLayout.addWidget(self.mrPushButton)

        self.mplusPushButton = QPushButton(self.widget)
        self.memoryButtonGroup.addButton(self.mplusPushButton)
        self.mplusPushButton.setObjectName(u"mplusPushButton")

        self.memoryLayout.addWidget(self.mplusPushButton)

        self.mminusPushButton = QPushButton(self.widget)
        self.memoryButtonGroup.addButton(self.mminusPushButton)
        self.mminusPushButton.setObjectName(u"mminusPushButton")

        self.memoryLayout.addWidget(self.mminusPushButton)

        self.msPushButton = QPushButton(self.widget)
        self.memoryButtonGroup.addButton(self.msPushButton)
        self.msPushButton.setObjectName(u"msPushButton")

        self.memoryLayout.addWidget(self.msPushButton)

        self.mhistoryPushButton = QPushButton(self.widget)
        self.memoryButtonGroup.addButton(self.mhistoryPushButton)
        self.mhistoryPushButton.setObjectName(u"mhistoryPushButton")

        self.memoryLayout.addWidget(self.mhistoryPushButton)


        self.gridLayout.addLayout(self.memoryLayout, 2, 0, 1, 1)

        self.numberEditor = QTextEdit(self.widget)
        self.numberEditor.setObjectName(u"numberEditor")
        self.numberEditor.setStyleSheet(u"color: black;\n"
"font-size: 30px;")

        self.gridLayout.addWidget(self.numberEditor, 1, 0, 1, 1)

        self.buttonGridLayout = QGridLayout()
        self.buttonGridLayout.setObjectName(u"buttonGridLayout")
        self.buttonGridLayout.setContentsMargins(-1, 0, -1, -1)
        self.equalPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup = QButtonGroup(MainWindow)
        self.calculatorButtonGroup.setObjectName(u"calculatorButtonGroup")
        self.calculatorButtonGroup.setExclusive(True)
        self.calculatorButtonGroup.addButton(self.equalPushButton)
        self.equalPushButton.setObjectName(u"equalPushButton")
        self.equalPushButton.setMinimumSize(QSize(0, 35))
        self.equalPushButton.setMaximumSize(QSize(200, 35))
        self.equalPushButton.setSizeIncrement(QSize(0, 0))
        self.equalPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.equalPushButton, 5, 3, 1, 1)

        self.plusPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.plusPushButton)
        self.plusPushButton.setObjectName(u"plusPushButton")
        self.plusPushButton.setMinimumSize(QSize(0, 35))
        self.plusPushButton.setMaximumSize(QSize(200, 35))
        self.plusPushButton.setSizeIncrement(QSize(0, 0))
        self.plusPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.plusPushButton, 4, 3, 1, 1)

        self.onePushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.onePushButton)
        self.onePushButton.setObjectName(u"onePushButton")
        self.onePushButton.setMinimumSize(QSize(0, 35))
        self.onePushButton.setMaximumSize(QSize(200, 35))
        self.onePushButton.setSizeIncrement(QSize(0, 0))
        self.onePushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.onePushButton, 4, 0, 1, 1)

        self.cePushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.cePushButton)
        self.cePushButton.setObjectName(u"cePushButton")
        self.cePushButton.setMinimumSize(QSize(0, 35))
        self.cePushButton.setMaximumSize(QSize(200, 35))
        self.cePushButton.setSizeIncrement(QSize(0, 0))
        self.cePushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.cePushButton, 0, 1, 1, 1)

        self.minusPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.minusPushButton)
        self.minusPushButton.setObjectName(u"minusPushButton")
        self.minusPushButton.setMinimumSize(QSize(0, 35))
        self.minusPushButton.setMaximumSize(QSize(200, 35))
        self.minusPushButton.setSizeIncrement(QSize(0, 0))
        self.minusPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.minusPushButton, 3, 3, 1, 1)

        self.sixPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.sixPushButton)
        self.sixPushButton.setObjectName(u"sixPushButton")
        self.sixPushButton.setMinimumSize(QSize(0, 35))
        self.sixPushButton.setMaximumSize(QSize(200, 35))
        self.sixPushButton.setSizeIncrement(QSize(0, 0))
        self.sixPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.sixPushButton, 3, 2, 1, 1)

        self.dividePushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.dividePushButton)
        self.dividePushButton.setObjectName(u"dividePushButton")
        self.dividePushButton.setMinimumSize(QSize(0, 35))
        self.dividePushButton.setMaximumSize(QSize(200, 35))
        self.dividePushButton.setSizeIncrement(QSize(0, 0))
        self.dividePushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.dividePushButton, 1, 3, 1, 1)

        self.twoPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.twoPushButton)
        self.twoPushButton.setObjectName(u"twoPushButton")
        self.twoPushButton.setMinimumSize(QSize(0, 35))
        self.twoPushButton.setMaximumSize(QSize(200, 35))
        self.twoPushButton.setSizeIncrement(QSize(0, 0))
        self.twoPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.twoPushButton, 4, 1, 1, 1)

        self.fourPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.fourPushButton)
        self.fourPushButton.setObjectName(u"fourPushButton")
        self.fourPushButton.setMinimumSize(QSize(0, 35))
        self.fourPushButton.setMaximumSize(QSize(200, 35))
        self.fourPushButton.setSizeIncrement(QSize(0, 0))
        self.fourPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.fourPushButton, 3, 0, 1, 1)

        self.multiplyPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.multiplyPushButton)
        self.multiplyPushButton.setObjectName(u"multiplyPushButton")
        self.multiplyPushButton.setMinimumSize(QSize(0, 35))
        self.multiplyPushButton.setMaximumSize(QSize(200, 35))
        self.multiplyPushButton.setSizeIncrement(QSize(0, 0))
        self.multiplyPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.multiplyPushButton, 2, 3, 1, 1)

        self.threePushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.threePushButton)
        self.threePushButton.setObjectName(u"threePushButton")
        self.threePushButton.setMinimumSize(QSize(0, 35))
        self.threePushButton.setMaximumSize(QSize(200, 35))
        self.threePushButton.setSizeIncrement(QSize(0, 0))
        self.threePushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.threePushButton, 4, 2, 1, 1)

        self.rootXPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.rootXPushButton)
        self.rootXPushButton.setObjectName(u"rootXPushButton")
        self.rootXPushButton.setMinimumSize(QSize(0, 35))
        self.rootXPushButton.setMaximumSize(QSize(200, 35))
        self.rootXPushButton.setSizeIncrement(QSize(0, 0))
        self.rootXPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.rootXPushButton, 1, 2, 1, 1)

        self.dotPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.dotPushButton)
        self.dotPushButton.setObjectName(u"dotPushButton")
        self.dotPushButton.setMinimumSize(QSize(0, 35))
        self.dotPushButton.setMaximumSize(QSize(200, 35))
        self.dotPushButton.setSizeIncrement(QSize(0, 0))
        self.dotPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.dotPushButton, 5, 2, 1, 1)

        self.ninePushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.ninePushButton)
        self.ninePushButton.setObjectName(u"ninePushButton")
        self.ninePushButton.setMinimumSize(QSize(0, 35))
        self.ninePushButton.setMaximumSize(QSize(200, 35))
        self.ninePushButton.setSizeIncrement(QSize(0, 0))
        self.ninePushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.ninePushButton, 2, 2, 1, 1)

        self.changeSighnPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.changeSighnPushButton)
        self.changeSighnPushButton.setObjectName(u"changeSighnPushButton")
        self.changeSighnPushButton.setMinimumSize(QSize(0, 35))
        self.changeSighnPushButton.setMaximumSize(QSize(200, 35))
        self.changeSighnPushButton.setSizeIncrement(QSize(0, 0))
        self.changeSighnPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.changeSighnPushButton, 5, 0, 1, 1)

        self.backspacePushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.backspacePushButton)
        self.backspacePushButton.setObjectName(u"backspacePushButton")
        self.backspacePushButton.setMinimumSize(QSize(0, 35))
        self.backspacePushButton.setMaximumSize(QSize(200, 35))
        self.backspacePushButton.setSizeIncrement(QSize(0, 0))
        self.backspacePushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.backspacePushButton, 0, 3, 1, 1)

        self.cPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.cPushButton)
        self.cPushButton.setObjectName(u"cPushButton")
        self.cPushButton.setMinimumSize(QSize(0, 35))
        self.cPushButton.setMaximumSize(QSize(200, 35))
        self.cPushButton.setSizeIncrement(QSize(0, 0))
        self.cPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.cPushButton, 0, 2, 1, 1)

        self.powerOfXPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.powerOfXPushButton)
        self.powerOfXPushButton.setObjectName(u"powerOfXPushButton")
        self.powerOfXPushButton.setMinimumSize(QSize(0, 35))
        self.powerOfXPushButton.setMaximumSize(QSize(200, 35))
        self.powerOfXPushButton.setSizeIncrement(QSize(0, 0))
        self.powerOfXPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.powerOfXPushButton, 1, 1, 1, 1)

        self.divideByXPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.divideByXPushButton)
        self.divideByXPushButton.setObjectName(u"divideByXPushButton")
        self.divideByXPushButton.setMinimumSize(QSize(0, 35))
        self.divideByXPushButton.setMaximumSize(QSize(200, 35))
        self.divideByXPushButton.setSizeIncrement(QSize(0, 0))
        self.divideByXPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.divideByXPushButton, 1, 0, 1, 1)

        self.fivePushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.fivePushButton)
        self.fivePushButton.setObjectName(u"fivePushButton")
        self.fivePushButton.setMinimumSize(QSize(0, 35))
        self.fivePushButton.setMaximumSize(QSize(200, 35))
        self.fivePushButton.setSizeIncrement(QSize(0, 0))
        self.fivePushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.fivePushButton, 3, 1, 1, 1)

        self.percentPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.percentPushButton)
        self.percentPushButton.setObjectName(u"percentPushButton")
        self.percentPushButton.setMinimumSize(QSize(0, 35))
        self.percentPushButton.setMaximumSize(QSize(200, 35))
        self.percentPushButton.setSizeIncrement(QSize(0, 0))
        self.percentPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.percentPushButton, 0, 0, 1, 1)

        self.sevenPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.sevenPushButton)
        self.sevenPushButton.setObjectName(u"sevenPushButton")
        self.sevenPushButton.setMinimumSize(QSize(0, 35))
        self.sevenPushButton.setMaximumSize(QSize(200, 35))
        self.sevenPushButton.setSizeIncrement(QSize(0, 0))
        self.sevenPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.sevenPushButton, 2, 0, 1, 1)

        self.zeroPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.zeroPushButton)
        self.zeroPushButton.setObjectName(u"zeroPushButton")
        self.zeroPushButton.setMinimumSize(QSize(0, 35))
        self.zeroPushButton.setMaximumSize(QSize(200, 35))
        self.zeroPushButton.setSizeIncrement(QSize(0, 0))
        self.zeroPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.zeroPushButton, 5, 1, 1, 1)

        self.eightPushButton = QPushButton(self.widget)
        self.calculatorButtonGroup.addButton(self.eightPushButton)
        self.eightPushButton.setObjectName(u"eightPushButton")
        self.eightPushButton.setMinimumSize(QSize(0, 35))
        self.eightPushButton.setMaximumSize(QSize(200, 35))
        self.eightPushButton.setSizeIncrement(QSize(0, 0))
        self.eightPushButton.setBaseSize(QSize(0, 0))

        self.buttonGridLayout.addWidget(self.eightPushButton, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.buttonGridLayout, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiondddd.setText(QCoreApplication.translate("MainWindow", u"dddd", None))
        self.mcPushButton.setText(QCoreApplication.translate("MainWindow", u"MC", None))
        self.mrPushButton.setText(QCoreApplication.translate("MainWindow", u"MR", None))
        self.mplusPushButton.setText(QCoreApplication.translate("MainWindow", u"M+", None))
        self.mminusPushButton.setText(QCoreApplication.translate("MainWindow", u"M-", None))
        self.msPushButton.setText(QCoreApplication.translate("MainWindow", u"MS", None))
        self.mhistoryPushButton.setText(QCoreApplication.translate("MainWindow", u"M^", None))
        self.numberEditor.setMarkdown(QCoreApplication.translate("MainWindow", u"1241234123\n"
"\n"
"", None))
        self.numberEditor.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:30px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1241234123</p></body></html>", None))
        self.equalPushButton.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.plusPushButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.onePushButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.cePushButton.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.minusPushButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.sixPushButton.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.dividePushButton.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.twoPushButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.fourPushButton.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.multiplyPushButton.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.threePushButton.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.rootXPushButton.setText(QCoreApplication.translate("MainWindow", u"2/x", None))
        self.dotPushButton.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.ninePushButton.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.changeSighnPushButton.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.backspacePushButton.setText(QCoreApplication.translate("MainWindow", u"<-x", None))
        self.cPushButton.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.powerOfXPushButton.setText(QCoreApplication.translate("MainWindow", u"x^2", None))
        self.divideByXPushButton.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.fivePushButton.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.percentPushButton.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.sevenPushButton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.zeroPushButton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.eightPushButton.setText(QCoreApplication.translate("MainWindow", u"8", None))
    # retranslateUi


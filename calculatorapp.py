from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

import sys

class Ui_calculator(object):
    def setupUi(self, calculator):
        if not calculator.objectName():
            calculator.setObjectName(u"calculator")
        calculator.resize(300, 300)
        calculator.setMinimumSize(QSize(100, 100))
        calculator.setMaximumSize(QSize(300, 300))
        self.output = QLabel(calculator)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(10, 220, 280, 50))
        font = QFont()
        font.setPointSize(20)
        self.output.setFont(font)
        self.output.setFrameShape(QFrame.Box)
        self.output.setFrameShadow(QFrame.Sunken)
        self.output.setMargin(10)
        self.plus = QPushButton(calculator)
        self.plus.setObjectName(u"plus")
        self.plus.setGeometry(QRect(120, 80, 51, 41))
        font1 = QFont()
        font1.setPointSize(17)
        self.plus.setFont(font1)
        # plus
        self.plus.clicked.connect(self.performAddition)  # add event handler?.name of function

        self.minus = QPushButton(calculator)
        self.minus.setObjectName(u"minus")
        self.minus.setGeometry(QRect(120, 160, 51, 41))
        self.minus.setFont(font1)
        # minus
        self.minus.clicked.connect(self.performSubtract)

        self.multiply = QPushButton(calculator)
        self.multiply.setObjectName(u"multiply")
        self.multiply.setGeometry(QRect(70, 120, 51, 41))
        self.multiply.setFont(font1)
        # multiply
        self.multiply.clicked.connect(self.performMultiply)

        self.divide = QPushButton(calculator)
        self.divide.setObjectName(u"divide")
        self.divide.setGeometry(QRect(170, 120, 51, 41))
        self.divide.setFont(font1)
        # divide
        self.divide.clicked.connect(self.performDivide)

        self.label1 = QLabel(calculator)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(40, 10, 49, 16))
        self.label2 = QLabel(calculator)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(40, 40, 49, 16))
        self.input1 = QLineEdit(calculator)
        self.input1.setObjectName(u"input1")
        self.input1.setGeometry(QRect(100, 10, 113, 21))
        self.input2 = QLineEdit(calculator)
        self.input2.setObjectName(u"input2")
        self.input2.setGeometry(QRect(100, 40, 113, 21))
        self.retranslateUi(calculator)
        QMetaObject.connectSlotsByName(calculator)
    # setupUi

    def retranslateUi(self, calculator):
        calculator.setWindowTitle(QCoreApplication.translate("calculator", u"Calculator", None))
        self.output.setText(QCoreApplication.translate("calculator", u"0", None))
        self.plus.setText(QCoreApplication.translate("calculator", u"+", None))
        self.minus.setText(QCoreApplication.translate("calculator", u"-", None))
        self.multiply.setText(QCoreApplication.translate("calculator", u"*", None))
        self.divide.setText(QCoreApplication.translate("calculator", u"/", None))
        self.label1.setText(QCoreApplication.translate("calculator", u"Input 1", None))
        self.label2.setText(QCoreApplication.translate("calculator", u"Input 2", None))
    # retranslateUi

#functions
    def performAddition(self):
        #get text from input1
        i1 = self.input1.text()
        #get text from input2
        i2 = self.input2.text()
        #add them
        result = float(i1) + float(i2)
        #set the label
        self.output.setText(str(result))

    def performSubtract(self):
        i1 = self.input1.text()
        i2 = self.input2.text()
        result = float(i1) - float(i2)
        self.output.setText(str(result))

    def performMultiply(self):
        i1 = self.input1.text()
        i2 = self.input2.text()
        result = float(i1) * float(i2)
        self.output.setText(str(result))

    def performDivide(self):
        i1 = self.input1.text()
        i2 = self.input2.text()
        result = float(i1) / float(i2)
        self.output.setText(str(result))

app = QApplication([]) #makes program run
widget = QWidget()
form = Ui_calculator()
form.setupUi(widget)
widget.show()
sys.exit(app.exec())
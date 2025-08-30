# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject,QRect,QSize,Qt)
from PySide6.QtGui import (QColor,QFont)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,QTableWidget, QTableWidgetItem, QWidget, QAbstractScrollArea,QFrame)

# --- Custom Header for Word Wrap and Orange Background ---
class WordWrapHeader(QHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.setMinimumHeight(50)

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        painter.fillRect(rect, QColor(255, 147, 0))  # Orange background
        text = self.model().headerData(logicalIndex, self.orientation(), Qt.DisplayRole)
        painter.drawText(rect, Qt.AlignCenter | Qt.TextWordWrap, str(text))
        painter.restore()

class Ui_Credit_Note_CREATING(object):
    def setupUi(self, Credit_Note_CREATING):
        if not Credit_Note_CREATING.objectName():
            Credit_Note_CREATING.setObjectName(u"Credit_Note_CREATING")
        Credit_Note_CREATING.resize(800, 600)
        Credit_Note_CREATING.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(Credit_Note_CREATING)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 141, 21))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 30, 113, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 30, 81, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(400, 30, 113, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(530, 30, 81, 21))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(630, 30, 113, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 70, 101, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 70, 101, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 70, 111, 21))
        self.label_6.setWordWrap(False)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(400, 70, 113, 21))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(530, 70, 81, 21))
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(630, 70, 111, 25))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 110, 101, 21))
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(400, 110, 113, 21))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(530, 110, 81, 21))
        self.dateEdit_2 = QDateEdit(self.centralwidget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(630, 110, 111, 25))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 140, 121, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10.setWordWrap(True)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(150, 150, 131, 32))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(280, 150, 121, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(13)
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setWordWrap(False)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(400, 150, 131, 32))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(530, 150, 91, 31))
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_12.setWordWrap(False)
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(630, 150, 113, 21))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(530, 200, 61, 31))
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_13.setWordWrap(False)
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(630, 200, 113, 21))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setBold(True)
        for col in range(6):
            item = QTableWidgetItem()
            item.setFont(font2)
            item.setBackground(QColor(255, 147, 0))
            self.tableWidget.setHorizontalHeaderItem(col, item)
        # Make all rows blank
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(row, col, QTableWidgetItem(""))
        # Set "Total" in last row, first column (Description column)
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Total"))
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 250, 761, 192))
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.NoPen)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.verticalHeader().setVisible(False)

        # --- Use custom header for word wrap and orange background ---
        header = WordWrapHeader(Qt.Horizontal, self.tableWidget)
        self.tableWidget.setHorizontalHeader(header)
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setMinimumHeight(50)

        # --- Set alignment for table items except Description column (column 0) ---
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    if col == 0:
                        item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    else:
                        item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 470, 100, 32))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(610, 470, 100, 32))
        Credit_Note_CREATING.setCentralWidget(self.centralwidget)

        self.retranslateUi(Credit_Note_CREATING)

        self.pushButton.setDefault(True)
        self.pushButton_2.setDefault(True)

        QMetaObject.connectSlotsByName(Credit_Note_CREATING)
    # setupUi

    def retranslateUi(self, Credit_Note_CREATING):
        Credit_Note_CREATING.setWindowTitle(QCoreApplication.translate("Credit_Note_CREATING", u"Credit_Note_CREATING", None))
        self.label.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Buyer Registration No.", None))
        self.lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Buyer Name:", None))
        self.lineEdit_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Buyer Address:", None))
        self.lineEdit_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Credit_Note_CREATING", u"invoice Type", None))
        self.label_5.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Credit Type", None))
        self.label_6.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Credit Note Num.", None))
        self.lineEdit_4.setText("")
        self.label_7.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Date", None))
        self.label_8.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Invoice No.", None))
        self.lineEdit_5.setText("")
        self.label_9.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Invoice Date", None))
        self.label_10.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Sale Origination Province of Supplier", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Credit_Note_CREATING", u"Select", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Credit_Note_CREATING", u"Azad Jammu & Kashmir", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Credit_Note_CREATING", u"Balochistan", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Credit_Note_CREATING", u"Capital Territory", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Credit_Note_CREATING", u"FATA/PATA", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Credit_Note_CREATING", u"Gilgit Baltistan", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Credit_Note_CREATING", u"Punjab", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Credit_Note_CREATING", u"Sindh", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Credit_Note_CREATING", u"Khaiber Pakhtunkhawa", None))

        self.label_11.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Destination of Supply", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Credit_Note_CREATING", u"Select", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Credit_Note_CREATING", u"Azad Jammu & Kashmir", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Credit_Note_CREATING", u"Balochistan", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Credit_Note_CREATING", u"Capital Territory", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Credit_Note_CREATING", u"FATA/PATA", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Credit_Note_CREATING", u"Gilgit Baltistan", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("Credit_Note_CREATING", u"Punjab", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("Credit_Note_CREATING", u"Sindh", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("Credit_Note_CREATING", u"Khaiber Pakhtunkhawa", None))

        self.label_12.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Sales Tax Rate", None))
        self.lineEdit_6.setText("")
        self.label_13.setText(QCoreApplication.translate("Credit_Note_CREATING", u"UOM", None))
        self.lineEdit_7.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Description", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Quantity", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Rate", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Value Excluding Sales Tax", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Sales Tax @ 18", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Value including Sales Tax", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Credit_Note_CREATING", u"ABC", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Credit_Note_CREATING", u"10", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Credit_Note_CREATING", u"10,000", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Credit_Note_CREATING", u"100,000", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Credit_Note_CREATING", u"18,000", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Credit_Note_CREATING", u"118,000", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Credit_Note_CREATING", u"10,000", None));
        ___qtablewidgetitem15 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Credit_Note_CREATING", u"100,000", None));
        ___qtablewidgetitem16 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Credit_Note_CREATING", u"18,000", None));
        ___qtablewidgetitem17 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Credit_Note_CREATING", u"118,000", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("Credit_Note_CREATING", u"Submit", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    Credit_Note_CREATING = QMainWindow()
    ui = Ui_Credit_Note_CREATING()
    ui.setupUi(Credit_Note_CREATING)
    Credit_Note_CREATING.show()
    sys.exit(app.exec())
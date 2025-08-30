# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject, QRect,QSize,Qt)
from PySide6.QtGui import (QColor,QFont)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QTableWidget,QTableWidgetItem, QWidget)

# --- Custom Header for Word Wrap ---
class WordWrapHeader(QHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.setMinimumHeight(50)

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
          # Set orange background
        painter.fillRect(rect, QColor(255, 147, 0))
        text = self.model().headerData(logicalIndex, self.orientation(), Qt.DisplayRole)
        painter.drawText(rect, Qt.AlignCenter | Qt.TextWordWrap, str(text))
        painter.restore()

class Ui_Invoice_Creating(object):
    def setupUi(self, Invoice_Creating):
        if not Invoice_Creating.objectName():
            Invoice_Creating.setObjectName(u"Invoice_Creating")
        Invoice_Creating.resize(800, 600)
        Invoice_Creating.setMaximumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        Invoice_Creating.setFont(font)
        self.centralwidget = QWidget(Invoice_Creating)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 141, 31))
        self.label.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 70, 113, 30))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 70, 101, 31))
        self.label_2.setFont(font)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(400, 70, 113, 30))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 70, 101, 31))
        self.label_3.setFont(font)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(650, 70, 113, 30))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 101, 31))
        self.label_4.setFont(font)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(150, 140, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(13)
        self.comboBox.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 140, 81, 31))
        self.label_5.setFont(font)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(400, 140, 113, 30))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(540, 140, 81, 31))
        self.label_6.setFont(font)
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(649, 140, 121, 30))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 210, 111, 31))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setWordWrap(True)
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
        self.comboBox_2.setGeometry(QRect(150, 210, 141, 41))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 210, 111, 31))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(True)
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(390, 210, 141, 41))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(540, 210, 101, 31))
        self.label_9.setFont(font)
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(650, 210, 113, 30))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(540, 290, 81, 31))
        self.label_10.setFont(font)
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(650, 280, 113, 30))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Total"))
        self.tableWidget.setItem(1, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(1, 5, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(10, 380, 750, 111))  # Set width to 780px
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
        self.tableWidget.setRowCount(2)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 540, 100, 32))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(660, 540, 100, 32))
        Invoice_Creating.setCentralWidget(self.centralwidget)

        self.retranslateUi(Invoice_Creating)

        self.pushButton.setDefault(True)
        self.pushButton_2.setDefault(True)
        self.tableWidget.verticalHeader().setVisible(False)
        # --- Use custom header for word wrap ---
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
        QMetaObject.connectSlotsByName(Invoice_Creating)
    # setupUi

    def retranslateUi(self, Invoice_Creating):
        Invoice_Creating.setWindowTitle(QCoreApplication.translate("Invoice_Creating", u"Invoice_Creating", None))
        self.label.setText(QCoreApplication.translate("Invoice_Creating", u"Buyer Registration No.", None))
        self.label_2.setText(QCoreApplication.translate("Invoice_Creating", u"Buyer Name:", None))
        self.label_3.setText(QCoreApplication.translate("Invoice_Creating", u"Buyer Address:", None))
        self.label_4.setText(QCoreApplication.translate("Invoice_Creating", u"Invoice Type", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Invoice_Creating", u"Select type", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Invoice_Creating", u"Sales Tax Invoice", None))

        self.label_5.setText(QCoreApplication.translate("Invoice_Creating", u"Invoice No.", None))
        self.label_6.setText(QCoreApplication.translate("Invoice_Creating", u"Invoice Date.", None))
        self.label_7.setText(QCoreApplication.translate("Invoice_Creating", u"Sale organization Provience of Supplier", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Invoice_Creating", u"Select", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Invoice_Creating", u"Azad Jammu & Kashmir", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Invoice_Creating", u"Balochistan", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Invoice_Creating", u"Capital Territory", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Invoice_Creating", u"FATA/PATA", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Invoice_Creating", u"Gilgit Baltistan", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("Invoice_Creating", u"Punjab", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("Invoice_Creating", u"Sindh", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("Invoice_Creating", u"Khaiber Pakhtunkhawa", None))

        self.label_8.setText(QCoreApplication.translate("Invoice_Creating", u"Destination of Supply", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Invoice_Creating", u"Select", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Invoice_Creating", u"Azad Jammu & Kashmir", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Invoice_Creating", u"Balochistan", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Invoice_Creating", u"Capital Territory", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Invoice_Creating", u"FATA/PATA", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("Invoice_Creating", u"Gilgit Baltistan", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("Invoice_Creating", u"Punjab", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("Invoice_Creating", u"Sindh", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("Invoice_Creating", u"Khaiber Pakhtunkhawa", None))

        self.label_9.setText(QCoreApplication.translate("Invoice_Creating", u"Sales Tax Rate", None))
        self.label_10.setText(QCoreApplication.translate("Invoice_Creating", u"UOM", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Invoice_Creating", u"Description", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Invoice_Creating", u"Quantity", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Invoice_Creating", u"Rate", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Invoice_Creating", u"value Excluding Sales tax", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Invoice_Creating", u"Sales Tax @18%", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Invoice_Creating", u"Value including Sales Tax", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Invoice_Creating", u"Detail", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Invoice_Creating", u"Total", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Invoice_Creating", u"item", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Invoice_Creating", u"10", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Invoice_Creating", u"10,000", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Invoice_Creating", u"100,000", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Invoice_Creating", u"18,000", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Invoice_Creating", u"118,000", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Invoice_Creating", u"10,000", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Invoice_Creating", u"100,00", None));
        ___qtablewidgetitem16 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Invoice_Creating", u"18,000", None));
        ___qtablewidgetitem17 = self.tableWidget.item(1, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Invoice_Creating", u"118,000", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("Invoice_Creating", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("Invoice_Creating", u"Submit", None))

    # retranslateUi

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    Invoice_Creating = QMainWindow()
    ui = Ui_Invoice_Creating()
    ui.setupUi(Invoice_Creating)
    Invoice_Creating.show()
    sys.exit(app.exec())
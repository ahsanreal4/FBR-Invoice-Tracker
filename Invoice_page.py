# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject,QRect,QSize,Qt)
from PySide6.QtGui import (QColor, QFont,)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QTableWidget, QTableWidgetItem,
    QWidget,QAbstractScrollArea)

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

class Ui_Invoice_page(object):
    def setupUi(self, Invoice_page):
        if not Invoice_page.objectName():
            Invoice_page.setObjectName(u"Invoice_page")
        Invoice_page.resize(800, 600)
        Invoice_page.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(Invoice_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(800, 600))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(550, 20, 211, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(550, 60, 211, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(550, 90, 191, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 90, 211, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 120, 211, 21))
        self.label_5.setWordWrap(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 140, 171, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 170, 91, 31))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 200, 181, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 220, 211, 31))
        self.label_9.setWordWrap(True)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 240, 171, 31))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        __qtablewidgetitem1.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        __qtablewidgetitem3.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        __qtablewidgetitem4.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        __qtablewidgetitem5.setBackground(QColor(255, 147, 0));
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(1, 5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(2, 5, __qtablewidgetitem24)
        # Set "Total" in last row, first column (Description column)
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Total"))
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 270, 771, 141))
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
        self.tableWidget.setRowCount(3)
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

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 430, 751, 31))
        self.label_11.setWordWrap(True)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 460, 751, 31))
        self.label_12.setWordWrap(True)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 500, 181, 16))
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(220, 530, 381, 20))
        Invoice_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Invoice_page)

        QMetaObject.connectSlotsByName(Invoice_page)
    # setupUi

    def retranslateUi(self, Invoice_page):
        Invoice_page.setWindowTitle(QCoreApplication.translate("Invoice_page", u"Invoice_page", None))
        self.label.setText(QCoreApplication.translate("Invoice_page", u"Sales Tax invoice", None))
        self.label_2.setText(QCoreApplication.translate("Invoice_page", u"Invoice # ABC/XYZ/07-2025/001", None))
        self.label_3.setText(QCoreApplication.translate("Invoice_page", u"Date: July 1, 2025", None))
        self.label_4.setText(QCoreApplication.translate("Invoice_page", u"ABC (Private) Limited", None))
        self.label_5.setText(QCoreApplication.translate("Invoice_page", u"Address:ABCDEFGH,Lahore", None))
        self.label_6.setText(QCoreApplication.translate("Invoice_page", u"NTN:123456-8", None))
        self.label_7.setText(QCoreApplication.translate("Invoice_page", u"Bill To", None))
        self.label_8.setText(QCoreApplication.translate("Invoice_page", u"M/S XYZ (Private) Limited", None))
        self.label_9.setText(QCoreApplication.translate("Invoice_page", u"Address:ABCDEFGH,Lahore", None))
        self.label_10.setText(QCoreApplication.translate("Invoice_page", u"NTN:123456-8", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Invoice_page", u"Description", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Invoice_page", u"Quantity", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Invoice_page", u"Rate", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Invoice_page", u"Value Excluding Sales Tax", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Invoice_page", u"Sales Tax @ 18%", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Invoice_page", u"Value Including Sales Tax", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Invoice_page", u"Details", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Invoice_page", u"Details", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Invoice_page", u"Total", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Invoice_page", u"ABC Item", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Invoice_page", u"10", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Invoice_page", u"10,000", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Invoice_page", u"100,000", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Invoice_page", u"18,000", None));
        ___qtablewidgetitem14 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Invoice_page", u"118,000", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Invoice_page", u"XYZ Item", None));
        ___qtablewidgetitem16 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Invoice_page", u"20", None));
        ___qtablewidgetitem17 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Invoice_page", u"20,000", None));
        ___qtablewidgetitem18 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Invoice_page", u"400,000", None));
        ___qtablewidgetitem19 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Invoice_page", u"72,000", None));
        ___qtablewidgetitem20 = self.tableWidget.item(1, 5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Invoice_page", u"472,000", None));
        ___qtablewidgetitem21 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Invoice_page", u"30,000", None));
        ___qtablewidgetitem22 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Invoice_page", u"500,000", None));
        ___qtablewidgetitem23 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Invoice_page", u"90,000", None));
        ___qtablewidgetitem24 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Invoice_page", u"590,000", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_11.setText(QCoreApplication.translate("Invoice_page", u"Payment would be made through Cross Cheque, Pay Order, Demand Draft or any banking instruments in favour of ABC (Private) Limited. Cash is not acceptable ", None))
        self.label_12.setText(QCoreApplication.translate("Invoice_page", u"If you have any further queries you may contact us and we shall remain obliged to assist you to the best of our capabilities.", None))
        self.label_13.setText(QCoreApplication.translate("Invoice_page", u"Thank you for your business!", None))
        self.label_14.setText(QCoreApplication.translate("Invoice_page", u"This is a computer generated invoice, no signature is required.", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    Invoice_page = QMainWindow()
    ui = Ui_Invoice_page()
    ui.setupUi(Invoice_page)
    Invoice_page.show()
    sys.exit(app.exec())
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect,
    QSize, Qt, Signal)
from PySide6.QtGui import (
    QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QFileDialog)

class ClickableLabel(QLabel):
    clicked = Signal()
    def mousePressEvent(self, event):
        self.clicked.emit()

class Ui_Profile_page(object):
    def setupUi(self, Profile_page):
        if not Profile_page.objectName():        
            Profile_page.setObjectName(u"Profile_page")
        Profile_page.resize(800, 600)
        Profile_page.setMaximumSize(QSize(800, 600))
        self.label = QLabel(Profile_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 80, 101, 31))
        self.label.setMaximumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.lineEdit = QLineEdit(Profile_page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(200, 80, 141, 25))
        
        # Make label_2 clickable for logo upload
        self.label_2 = ClickableLabel(Profile_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 140, 300, 200))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QFrame.Shape.Box)
        self.label_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.clicked.connect(self.upload_logo)
        
        self.label_3 = QLabel(Profile_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 220, 101, 31))
        self.label_3.setMaximumSize(QSize(800, 600))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Profile_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 250, 101, 31))
        self.label_4.setMaximumSize(QSize(800, 600))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Profile_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 280, 101, 31))
        self.label_5.setMaximumSize(QSize(800, 600))
        self.label_5.setFont(font)
        self.label_6 = QLabel(Profile_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 310, 101, 31))
        self.label_6.setMaximumSize(QSize(800, 600))
        self.label_6.setFont(font)
        self.label_7 = QLabel(Profile_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 340, 101, 31))
        self.label_7.setMaximumSize(QSize(800, 600))
        self.label_7.setFont(font)
        self.label_8 = QLabel(Profile_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 370, 101, 31))
        self.label_8.setMaximumSize(QSize(800, 600))
        self.label_8.setFont(font)
        self.lineEdit_2 = QLineEdit(Profile_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(200, 220, 141, 25))
        self.lineEdit_3 = QLineEdit(Profile_page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(200, 250, 141, 25))
        self.lineEdit_4 = QLineEdit(Profile_page)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(200, 280, 141, 25))
        self.lineEdit_5 = QLineEdit(Profile_page)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(200, 310, 141, 25))
        self.lineEdit_6 = QLineEdit(Profile_page)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(200, 340, 141, 25))
        self.lineEdit_7 = QLineEdit(Profile_page)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(200, 370, 141, 25))
        self.lineEdit_7.setMaxLength(32767)
        self.pushButton = QPushButton(Profile_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 460, 100, 32))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.pushButton.setFont(font1)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton_2 = QPushButton(Profile_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(500, 460, 100, 32))
        self.pushButton_2.setFont(font)

        self.retranslateUi(Profile_page)

        self.pushButton.setDefault(True)
        self.pushButton_2.setDefault(True)

        QMetaObject.connectSlotsByName(Profile_page)
    # setupUi

    def retranslateUi(self, Profile_page):
        Profile_page.setWindowTitle(QCoreApplication.translate("Profile_page", u"Profile_page", None))
        self.label.setText(QCoreApplication.translate("Profile_page", u"Registration No.", None))
        self.lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("Profile_page", u"Add Logo picture optional", None))
        self.label_3.setText(QCoreApplication.translate("Profile_page", u"NTN", None))
        self.label_4.setText(QCoreApplication.translate("Profile_page", u"FBR Reg No", None))
        self.label_5.setText(QCoreApplication.translate("Profile_page", u"Name", None))
        self.label_6.setText(QCoreApplication.translate("Profile_page", u"Address", None))
        self.label_7.setText(QCoreApplication.translate("Profile_page", u"Tell", None))
        self.label_8.setText(QCoreApplication.translate("Profile_page", u"Email", None))
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.pushButton.setText(QCoreApplication.translate("Profile_page", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("Profile_page", u"Submit", None))
    # retranslateUi
    def upload_logo(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Select Logo", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            pixmap = QPixmap(file_path)
            # Use the actual label size for scaling
            label_size = self.label_2.size()
            scaled_pixmap = pixmap.scaled(
                label_size,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.label_2.setPixmap(scaled_pixmap)
            self.label_2.setText("")  # Remove text after image is set
            self.label_2.setStyleSheet("border: 2px dashed #aaa;")
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    Profile_page = QMainWindow()
    ui = Ui_Profile_page()
    ui.setupUi(Profile_page)
    Profile_page.show()
    sys.exit(app.exec())
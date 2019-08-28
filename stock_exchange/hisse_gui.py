# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hisse_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import Qt
########################### SCRIPT #########################################
import requests
import datetime

from bs4 import BeautifulSoup

################################GUI#########################################
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(585, 466)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 97, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 146, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 121, 181))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 97, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 176, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 97, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 146, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 121, 181))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 97, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 176, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 97, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 146, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 121, 181))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 97, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 97, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 97, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Form.setPalette(palette)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 60, 161, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 30, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 180, 561, 261))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.pushButton.clicked.connect(self.s_eps)

    def hisse_fiyat(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        self.a = self.lineEdit.text()

        url_akbank = "https://yatirim.akbank.com/tr-tr/hisse-senedi/Sayfalar/hisse-senet-detay.aspx?hisse={}".format(
            self.a.upper())

        response_akbank = requests.get(url_akbank)
        html_icerigi_akbank = response_akbank.content
        self.soup_akbank = BeautifulSoup(html_icerigi_akbank, "html.parser")

        year = datetime.datetime.now()
        year1 = year.year - 1
        year2 = year.year - 2

        url = "http://finans.mynet.com/borsa/hisseler/"
        url_ce = "http://finans.mynet.com/borsa/hisseler/c-e/"
        url_fj = "http://finans.mynet.com/borsa/hisseler/f-j/"
        url_kq = "http://finans.mynet.com/borsa/hisseler/k-q/"
        url_rz = "http://finans.mynet.com/borsa/hisseler/r-z/"

        response = requests.get(url)
        response_ce = requests.get(url_ce)
        response_fj = requests.get(url_fj)
        response_kq = requests.get(url_kq)
        response_rz = requests.get(url_rz)

        html_icerigi_ce = response_ce.content
        html_icerigi_fj = response_fj.content
        html_icerigi_kq = response_kq.content
        html_icerigi_rz = response_rz.content
        html_icerigi = response.content

        soup_ce = BeautifulSoup(html_icerigi_ce, "html.parser")
        soup_fj = BeautifulSoup(html_icerigi_fj, "html.parser")
        soup_kq = BeautifulSoup(html_icerigi_kq, "html.parser")
        soup_rz = BeautifulSoup(html_icerigi_rz, "html.parser")

        soup = BeautifulSoup(html_icerigi, "html.parser")
        links = []
        links_ce = []
        links_fj = []
        links_kq = []
        links_rz = []

        for tag in soup.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag.find_all('a'):
                links.append(anchor['href'])

        for tag_ce in soup_ce.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag_ce.find_all('a'):
                links_ce.append(anchor['href'])

        for tag_fj in soup_fj.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag_fj.find_all('a'):
                links_fj.append(anchor['href'])

        for tag_kq in soup_kq.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag_kq.find_all('a'):
                links_kq.append(anchor['href'])

        for tag_rz in soup_rz.find_all('td', {'class': 'ndt-leftText ndt-noBorderRight'}):
            for anchor in tag_rz.find_all('a'):
                links_rz.append(anchor['href'])

        for h in links:
            url_fiyat = "http://finans.mynet.com/" + h
            self.url_fiyat_gwrate = url_fiyat + "bilanco" + "/" + str(year1) + "-12" + "/" + "0"
            self.url_fiyat_gwrate2 = url_fiyat + "bilanco" + "/" + str(year2) + "-12" + "/" + "0"
            if self.a in url_fiyat:
                response_fiyat = requests.get(url_fiyat)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                my_string = hisse_fiyati
                commas_removed = my_string.replace(',', '.')  # remove comma separation
                self.my_float = float(commas_removed)  # turn from string to float.
                self.plainTextEdit.setPlainText(str(self.my_float))
                QApplication.restoreOverrideCursor()

        for h_ce in links_ce:
            url_fiyat_ce = "http://finans.mynet.com/" + h_ce
            self.url_fiyat_gwrate = url_fiyat_ce + "bilanco" + "/" + str(year1) + "-12" + "/" + "0"
            self.url_fiyat_gwrate2 = url_fiyat_ce + "bilanco" + "/" + str(year2) + "-12" + "/" + "0"

            if self.a in url_fiyat_ce:
                response_fiyat = requests.get(url_fiyat_ce)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                my_string = hisse_fiyati
                commas_removed = my_string.replace(',', '.')  # remove comma separation
                self.my_float = float(commas_removed)  # turn from string to float.
                self.plainTextEdit.setPlainText(str(self.my_float))
                QApplication.restoreOverrideCursor()

        for h_fj in links_fj:
            url_fiyat_fj = "http://finans.mynet.com/" + h_fj
            self.url_fiyat_gwrate = url_fiyat_fj + "bilanco" + "/" + str(year1) + "-12" + "/" + "0"
            self.url_fiyat_gwrate2 = url_fiyat_fj + "bilanco" + "/" + str(year2) + "-12" + "/" + "0"
            if self.a in url_fiyat_fj:
                response_fiyat = requests.get(url_fiyat_fj)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")
                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                my_string = hisse_fiyati
                commas_removed = my_string.replace(',', '.')  # remove comma separation
                self.my_float = float(commas_removed)  # turn from string to float.

                self.plainTextEdit.setPlainText(str(self.my_float))
                QApplication.restoreOverrideCursor()

        for h_kq in links_kq:
            url_fiyat_kq = "http://finans.mynet.com/" + h_kq
            self.url_fiyat_gwrate = url_fiyat_kq + "bilanco" + "/" + str(year1) + "-12" + "/" + "0"
            self.url_fiyat_gwrate2 = url_fiyat_kq + "bilanco" + "/" + str(year2) + "-12" + "/" + "0"
            if self.a in url_fiyat_kq:
                response_fiyat = requests.get(url_fiyat_kq)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                my_string = hisse_fiyati
                commas_removed = my_string.replace(',', '.')  # remove comma separation
                self.my_float = float(commas_removed)  # turn from string to float.

                self.plainTextEdit.setPlainText(str(self.my_float))
                QApplication.restoreOverrideCursor()

        for h_rz in links_rz:
            url_fiyat_rz = "http://finans.mynet.com/" + h_rz
            self.url_fiyat_gwrate = url_fiyat_rz + "bilanco" + "/" + str(year1) + "-12" + "/" + "0"
            self.url_fiyat_gwrate2 = url_fiyat_rz + "bilanco" + "/" + str(year2) + "-12" + "/" + "0"
            if self.a in url_fiyat_rz:
                response_fiyat = requests.get(url_fiyat_rz)

                html_fiyat_icerigi = response_fiyat.content
                soup_fiyat = BeautifulSoup(html_fiyat_icerigi, "html.parser")

                hisse_fiyati = soup_fiyat.find_all("span", {"class": "dtColTwo"})

                hisse_fiyati = hisse_fiyati[0].text
                my_string = hisse_fiyati
                commas_removed = my_string.replace(',', '.')  # remove comma separation
                self.my_float = float(commas_removed)  # turn from string to float.

                self.plainTextEdit.setPlainText(str(self.my_float))
                QApplication.restoreOverrideCursor()



    def s_eps(self):
        main.hisse()
        self.plainTextEdit.setPlainText(str(self.hisse_eps))
        QApplication.restoreOverrideCursor()






    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hisse Fiyat Hesaplayıcı"))
        self.label.setText(_translate("Form", "Hisse Adı Giriniz:"))
        self.pushButton.setText(_translate("Form", "Ara"))
        self.pushButton_2.setText(_translate("Form", "Temizle"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
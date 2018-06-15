from PyQt5 import QtWidgets, QtGui
import sys

def dlg():
    #a=QtWidgets.QApplication(sys.argv)
    dlg=QtWidgets.QDialog()
    dlg.setGeometry(100, 100, 300, 300)
    dlg.setWindowIcon(QtGui.QIcon('ico//smart.ico'))
    dlg.setWindowTitle('Smart Editor 2017')

    lbl=QtWidgets.QLabel(dlg)
    px=QtGui.QPixmap('ico//smart.ico')
    new_px=px.scaled(100, 100)
    lbl.setPixmap(new_px)
    lbl.move(100, 90)
    lbl0=QtWidgets.QLabel('<b>Smart Editor 2017</b>', dlg)
    lbl0.move(100, 200)
    lbl1=QtWidgets.QLabel('<b>A product of Clone Softwares</b>', dlg)
    lbl1.move(70, 220)
    dlg.exec_()

import webbrowser
from PyQt5 import QtWidgets
import sys


def errorDlg():
    a=QtWidgets.QApplication(sys.argv)
    dlg=QtWidgets.QDialog()
    dlg.setGeometry(100, 100, 300, 100)
    lbl=QtWidgets.QLabel('Error: Failed to access Clone Store!', dlg)
    lbl.move(60, 10)
    dlg.show()
    a.exec_()
    
url='http://localhost/dashboard/'

def open_product_page():
    try:
        webbrowser.open_new_tab(url)
    except webbrowser.Error:
        errorDlg()

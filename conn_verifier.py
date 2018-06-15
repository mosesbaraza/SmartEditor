from PyQt5 import QtWidgets, QtGui
import requests
import sys

test_url='http://localhost/dashboard/main.xml'

def internet_conn_dlg():
    a=QtWidgets.QApplication(sys.argv)
    dlg=QtWidgets.QDialog()
    dlg.setGeometry(100, 100, 300, 100)
    dlg.setWindowIcon(QtGui.QIcon('ico//smart.ico'))
    dlg.setWindowTitle('Smart Updater')
    lbl=QtWidgets.QLabel('Connecting to Server..', dlg)
    lbl.move(80, 10)
    try:
        r=requests.get(test_url)
        print(r.text)
        l=QtWidgets.QLabel(dlg)
        px=QtGui.QPixmap("F:\\ico\\success.ico")
        t=px.scaled(50, 50)
        l.setPixmap(t)
        l.move(10, 10)
        lbl.setText('Connected to Server!')
        ##xml parsing##
    except requests.ConnectionError:
        lbl.setText('Failed: No internet connection!')
        
    dlg.show()
    a.exec_()
internet_conn_dlg()



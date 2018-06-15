from PyQt5 import QtWidgets, QtGui, QtCore
import sys, os
import products
#import conn_verifier
import about

class SmartUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(SmartUI, self).__init__()
        self.__ui()

    def __ui(self):
        ###widgets###

        ##tab
        self.mainTab=QtWidgets.QTabWidget(self)
        self.mainTab.setTabsClosable(True)
        self.mainTab.setMovable(True)
        self.mainTab.setTabShape(self.mainTab.Triangular)
        ##
        self.text=QtWidgets.QTextEdit(self)
        self.text.textChanged.connect(self.statusVerifier)
        self.text.cursorPositionChanged.connect(self.cursor_detector)
        self.mainTab.addTab(self.text, "untitled")
        self.mainTab.tabBarDoubleClicked.connect(self.addNewTab)
        self.mainTab.tabCloseRequested.connect(self.closeTab)
        
        ###file actions###
        new=QtWidgets.QAction('New', self)
        new.setShortcut('Ctrl+N')
        openfile=QtWidgets.QAction('Open', self)
        openfile.setShortcut('Ctrl+O')
        openfile.triggered.connect(self.openFile)
        save=QtWidgets.QAction('Save', self)
        save.triggered.connect(self.saveFile)
        save.setShortcut('Ctrl+S')
        saveas=QtWidgets.QAction('Save As', self)
        saveas.setShortcut('Ctrl+Shift+S')
        saveas.triggered.connect(self.saveFileAs)
        exitapp=QtWidgets.QAction('Exit', self)
        exitapp.triggered.connect(self.closeEvent)
        ###edit actions###
        undo=QtWidgets.QAction('Undo', self)
        undo.setShortcut('Ctrl+U')
        undo.triggered.connect(self.onUndo)
        redo=QtWidgets.QAction('Redo', self)
        redo.setShortcut('Ctrl+R')
        redo.triggered.connect(self.onRedo)
        select=QtWidgets.QAction('Select All', self)
        select.setShortcut('Ctrl+A')
        select.triggered.connect(self.onSelectAll)
        copy=QtWidgets.QAction('Copy', self)
        copy.setShortcut('Ctrl+C')
        copy.triggered.connect(self.onCopy)
        paste=QtWidgets.QAction('Paste', self)
        paste.setShortcut('Ctrl+V')
        paste.triggered.connect(self.onPaste)
        cut=QtWidgets.QAction('Cut', self)
        cut.setShortcut('Ctrl+X')
        cut.triggered.connect(self.onCut)
        ###view actions###
        cur1=QtWidgets.QAction('Wide', self)
        cur1.triggered.connect(self.wideCur)
        cur2=QtWidgets.QAction('Narrow', self)
        cur2.triggered.connect(self.narrowCur)
        zoom1=QtWidgets.QAction('Zoom In', self)
        zoom1.triggered.connect(self.zoom_in)
        zoom1.setShortcut('Ctrl+=')
        zoom2=QtWidgets.QAction('Zoom Out', self)
        zoom2.triggered.connect(self.zoom_out)
        zoom2.setShortcut('Ctrl+-')
        ##help actions##
        about=QtWidgets.QAction('About', self)
        about.triggered.connect(self.aboutInfo)
        update=QtWidgets.QAction('Get updates..', self)
        update.triggered.connect(self.getAppUpdate)
        stores=QtWidgets.QAction('More Products', self)
        stores.triggered.connect(self.getMoreProducts)

        ###file_menu##
        self.file=self.menuBar()
        
        f=self.file.addMenu('File')
        f.addAction(new)
        f.addAction(openfile)
        f.addAction(save)
        f.addAction(saveas)
        f.addAction(exitapp)
        
        e=self.file.addMenu('Edit')
        e.addAction(undo)
        e.addAction(redo)
        e.addAction(select)
        e.addAction(copy)
        e.addAction(paste)
        e.addAction(cut)
        v=self.file.addMenu('View')
        c=v.addMenu('Cursor Width')
        z=v.addMenu('Zoom')
        z.addAction(zoom1)
        z.addAction(zoom2)
        c.addAction(cur1)
        c.addAction(cur2)
        h=self.file.addMenu('Help')
        h.addAction(about)
        h.addAction(update)
        h.addAction(stores)

        self.status=self.statusBar()
        self.status_label=QtWidgets.QLabel(self)
        self.status.addPermanentWidget(self.status_label)
        self.cursor=self.text.textCursor()
        self.status_label.setText("ln: {0} col: {1}".format(self.cursor.blockNumber()+1, self.cursor.columnNumber()))
        
        
        self.setGeometry(200, 100, 800, 700)
        self.setWindowIcon(QtGui.QIcon('ico//smart.ico'))
        self.setWindowTitle('Smart Editor')
        self.setCentralWidget(self.mainTab)
        self.show()

        self.saved=False
        self.titled=False

    def addNewTab(self):
        self.text=QtWidgets.QTextEdit(self)
        self.mainTab.addTab(self.text, "untitled")

    def closeTab(self):
        self.mainTab.removeTab(self.mainTab.currentIndex())
        

    def cursor_detector(self):
        cur=self.text.textCursor()
        self.status_label.setText("ln: {0} col: {1}".format(cur.blockNumber()+1, cur.columnNumber()))

    def statusVerifier(self):
        if self.titled==False:
            self.setWindowTitle('*Untitled* - Smart Editor')
        else:
            file_name=os.path.basename(self.file)
            self.setWindowTitle('*{0}* - Smart Editor'.format(file_name))

    def openFile(self):
        self.file, self.ext=QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', "*.txt")
        if self.file:
            myFile=open(self.file, 'r')
            self.text.setText(myFile.read())
            myFile.close()
            file_name=os.path.basename(self.file)
            self.setWindowTitle('{0} - Smart Editor'.format(file_name))
            self.titled=True
            self.saved=True
        else:
            pass


    def saveFileAs(self):
        self.file, self.ext=QtWidgets.QFileDialog.getSaveFileName(self, 'Save File As', '*.txt')
        if self.file:
            myFile=open(self.file, "w")
            myFile.write(self.text.toPlainText())
            myFile.close()
            file_name=os.path.basename(self.file)
            self.setWindowTitle('{0} - Smart Editor'.format(file_name))
            self.saved=True
            self.titled=True
        else:
            pass

    def saveFile(self):
        if self.saved==False:
            self.file, self.ext=QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '*.txt')
            if self.file:
                myFile=open(self.file, "w")
                myFile.write(self.text.toPlainText())
                myFile.close()
                file_name=os.path.basename(self.file)
                self.setWindowTitle('{0} - Smart Editor'.format(file_name))
                self.saved=True
                self.titled=True
            else:
                pass
        else:
            myFile=open(self.file, 'w')
            x=open(self.file, 'w')
            x.flush()
            myFile.write(self.text.toPlainText())
            x.close()
            myFile.close()
            file_name=os.path.basename(self.file)
            self.setWindowTitle('{0} - Smart Editor'.format(file_name))
            self.saved=True
            self.titled=True

    def onUndo(self):
        self.text.undo()
    def onRedo(self):
        self.text.redo()
    def onCut(self):
        self.text.cut()
    def onSelectAll(self):
        self.text.selectAll()
    def onPaste(self):
        self.text.paste()
    def onCopy(self):
        self.text.copy()
    def wideCur(self):
        self.text.setCursorWidth(3)
    def narrowCur(self):
        self.text.setCursorWidth(1)
    def zoom_in(self):
        self.text.zoomIn()
    def zoom_out(self):
        self.text.zoomOut()
    def getMoreProducts(self):
        products.open_product_page()
    def getAppUpdate(self):
        conn_verifier.internet_conn_dlg()
    def aboutInfo(self):
        about.dlg()
    def closeEvent(self, event): #dialog to verify saved work
        if self.saved==True:
            QtWidgets.qApp.quit()
        else:
            reply=QtWidgets.QMessageBox.question(self, 'Exit', 'Save changes on exiting?', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply==QtWidgets.QMessageBox.Yes:
                self.saveFile()
                QtWidgets.qApp.quit()
            elif reply==QtWidgets.QMessageBox.No:
                QtWidgets.qApp.quit()

def main():
    app=QtWidgets.QApplication(sys.argv)
    x=SmartUI()
    app.exec_()

main()

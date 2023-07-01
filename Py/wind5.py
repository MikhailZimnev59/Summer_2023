# MDI

from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit, QMessageBox, QDialogButtonBox
from PyQt6.QtGui import QAction, QIcon
import sys


class MDIWindow(QMainWindow):
    count = 0

    def __init__(self):
        super().__init__()

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("Файл")
        file.addAction("New")
        file.addSeparator()
        file.addAction("Cascade")
        file.addSeparator()
        file.addAction("Tiled")

        editFindAction = QAction(QIcon('t2.png'), 'Find', self)
        editFindAction.triggered.connect(self.clickFind)
        editCopyAction = QAction(QIcon('t4.png'), 'Copy', self)
        editCopyAction.triggered.connect(self.clickCopy)

        edit = bar.addMenu("Edit")
        edit.addAction(editFindAction)
        edit.addAction(editCopyAction)
        edit.addAction("Paste")

        exitAction = QAction(QIcon('t1.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        fileMenu = bar.addMenu('&Exit')
        fileMenu.addAction(exitAction)

        file.triggered[QAction].connect(self.WindowTrig)
        self.setWindowTitle("MDI Application")

    def clickFind(self):
        QMessageBox.about(self, "Find", "Message")

    def clickCopy(self):
        QMessageBox.about(self, "Copy", "Message")
        #buttons = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        #self.buttonBox = QDialogButtonBox(buttons)
        #self.buttonBox.accepted.connect(self.accept)
        #self.buttonBox.rejected.connect(self.reject)
        #QDialogButtonBox(buttons)

    def WindowTrig(self, p):
        if p.text() == "New":
            MDIWindow.count = MDIWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            #self.text_output = sub.setWidget.QTextEdit()
            sub.setWindowTitle("Sub" + str(MDIWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        if p.text() == "Cascade":
            self.mdi.cascadeSubWindows()
        if p.text() == "Tiled":
            self.mdi.tileSubWindows()


app = QApplication(sys.argv)
mdiwindow = MDIWindow()
mdiwindow.show()
app.exec()

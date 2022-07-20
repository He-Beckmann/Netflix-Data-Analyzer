import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel, QFileDialog)

class NetflixAnalyzer:

    def __init__(self):

        app = QApplication(sys.argv)
        self.widget = QWidget()
        self.widget.resize(300,300)
        self.widget.setWindowTitle("Netflix Analyzer")
        
        self.displayFolderInputScreen()
        
        self.widget.show()
        sys.exit(app.exec_())


    def displayFolderInputScreen(self):
        
        label = QLabel(self.widget)
        label.setText("Behold the Guru, Guru99")
        label.move(100,130)
        label.show()

        btn = QPushButton(self.widget)
        btn.setText('Select Folder')
        btn.move(110,150)
        btn.show()
        text = btn.clicked.connect(self.selectFolder)
        print(text)




        # text = QFileDialog.getExistingDirectory(w, 'Select Folder')
    def selectFolder(self):
        text = QFileDialog.getExistingDirectory(self.widget, 'Select Folder')
        # print(text)
        return False



if __name__ == '__main__':
    app = NetflixAnalyzer()


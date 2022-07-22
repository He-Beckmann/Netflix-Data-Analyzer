import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel, QFileDialog)

class NetflixAnalyzer:

    def __init__(self):
        self.folderPath = ''
        app = QApplication(sys.argv)
        self.widget = QWidget()
        self.widget.setFixedWidth(400)
        self.widget.setFixedHeight(200)
        self.widget.setWindowTitle("Netflix Analyzer")
        
        self.displayFolderInputScreen()

        self.widget.show()
        sys.exit(app.exec_())


    def displayFolderInputScreen(self):
        
        lineHeight = 80
        
        nameLabel = QLabel(self.widget)
        nameLabel.setText('Name:')
        self.line = QLineEdit(self.widget)

        self.line.move(80, lineHeight)
        self.line.resize(200, 20)
        self.line.returnPressed.connect(self.selectFolder)
        # line.setReadOnly(True)
        nameLabel.move(20, lineHeight)

        btn = QPushButton(self.widget)
        btn.setText('Select Folder')
        btn.move(300, lineHeight)
        btn.show()
        btn.clicked.connect(self.selectFolder)
        
        btn = QPushButton(self.widget)
        btn.setText('Analyze Netflix Account')
        btn.move(150, 120)
        btn.show()
        btn.clicked.connect(self.selectFolder)
        
        self.line.setText(self.folderPath)


        # text = QFileDialog.getExistingDirectory(w, 'Select Folder')
    def selectFolder(self):
        self.folderPath = QFileDialog.getExistingDirectory(self.widget, 'Select Folder')
        self.line.setText(self.folderPath)
        return self.folderPath


if __name__ == '__main__':
    app = NetflixAnalyzer()


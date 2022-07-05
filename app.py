from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os
import library
from ast import For
from PIL import Image

from nft_generator import arrayAppendLink

class MainRsa(QMainWindow):
    def __init__(self):
        super(MainRsa, self).__init__()
        self.main = library.Ui_MainWindow()
        self.main.setupUi(self)
        self.show()
        self.main.calculaterNft.clicked.connect(self.replayTest)
        self.main.generatorNgt.clicked.connect(self.generatorNft)
    linkArray = []
    arrayLink = []
    linkOneArray = []
    linkTwoArray = []
    linkFinal = ''
    x = 0
    def arrayAppendLink(self, linkArray):
        self.linkArray = []
        for root, dirs, files in os.walk(linkArray):
            for file in files:
                self.linkArray.append(os.path.join(root,file))
        return self.linkArray

    def replayTest(self):
        linkOne = self.main.linkOne.text()
        linkOne = linkOne.replace('\\', '/')
        print('linkOne' + linkOne)
        linkTwo = self.main.linkTwo.text()
        linkTwo = linkTwo.replace('\\', '/')
        print('linkTwo' + linkTwo)
        linkFinal = self.main.linkFinal.text()
        self.linkFinal = linkFinal.replace('\\', '/')
        self.linkOneArray = self.arrayAppendLink(linkOne)
        print('self.linkOneArray' ,  self.linkOneArray )
        self.linkTwoArray = self.arrayAppendLink(linkTwo)
        print('self.linkTwoArray', self.linkTwoArray )

        
    def generatorNft(self):
        for linkOneArrayFor in self.linkOneArray:
            linkOneArrayFor = Image.open(linkOneArrayFor)
            for	linkTwoArrayFor in self.linkTwoArray:
                linkTwoArrayFor = Image.open(linkTwoArrayFor)
                linkTwoArrayFor.paste(linkOneArrayFor, (0,0),  linkOneArrayFor)
                linkTwoArrayFor.save(self.linkFinal + "/" + str(self.x) + ".png")
                self.main.consoleTxt.setText(str(self.x))
                self.x = self.x + 1
        self.main.consoleTxt.setText('Завершено')
    
        






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainRsa()
    sys.exit(app.exec_())
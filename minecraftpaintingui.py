import sys, os
from PIL import Image
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from PySide6.QtCore import *

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)

        
        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        
        '''
        listofImages = [self.photoViewer for i in range(10)]
        for obj in listofImages:
            mainLayout.addWidget(obj)
        '''
        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            #print(file_path)
            #pImage = Image.open(file_path)
            #pImage = pImage.resize((50, 50), Image.ANTIALIAS)
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))

#app = QApplication(sys.argv)
#demo = AppDemo()
#demo.show()
#sys.exit(app.exec())
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Interactive Minecraft Paintings")
 
        # setting geometry
        self.setGeometry(0, 0, 800, 800)
        
        
        
        self.backgroundLabel = QLabel(self)
        self.backgroundPixMap = QPixmap('image-collage/kz.png')
        self.backgroundLabel.setPixmap(self.backgroundPixMap.scaled(self.width(), self.height()))
        self.backgroundLabel.setMinimumSize(1, 1)
        self.setCentralWidget(self.backgroundLabel) 
 
       # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()


    def resizeEvent(self, event):
        self.backgroundLabel.setPixmap(self.backgroundPixMap.scaled(self.width(), self.height()))

 
    # method for components
    def UiComponents(self):
        '''

        win = QWidget()
        grid = QGridLayout(self)
	
        for i in range(0,16):
            for j in range(1,16):
                grid.addWidget(AppDemo())
			
        win.setLayout(grid)
        win.show()

        '''
        # creating dock widget
        dock = QDockWidget(self)
 
        # setting title to the doc widget
        dock.setWindowTitle("GfG ")
 
        # creating a QWidget object
        widget = QWidget(self)
 
        # creating a vertical box layout
        layout = QGridLayout(self)
 
        # push button 1
        #push1 = AppDemo()
 
        # push button 2
        #push2 = AppDemo()
 
        # push button 3
        #push3 = AppDemo()

        for i in range(1,17):
            for j in range(1,17):
                layout.addWidget(AppDemo(),i,j)
 
        # adding these buttons to the layout
        #layout.addWidget(push1)
        #layout.addWidget(push2)
        #layout.addWidget(push3)
 
        # setting the layout to the widget
        widget.setLayout(layout)
 
        # adding widget to the layout
        dock.setWidget(widget)
 
 
        # setting geometry tot he dock widget
        dock.setGeometry(100, 0, 200, 30)
        
 
 
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())
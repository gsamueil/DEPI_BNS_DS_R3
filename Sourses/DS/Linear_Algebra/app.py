import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog , QMainWindow,QUndoView,QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMessageBox
# import cv2
import numpy as np
from PyQt5 import Qt, uic, QtWidgets
from skimage.io import imshow,imread,imsave


class Image_Viewer(QMainWindow):
    def __init__(self):
        super(Image_Viewer, self).__init__()
        uic.loadUi('D:/Depi_DS_BS/DEPI_BNS_DS_R3/Sourses/DS/Linear_Algebra/form.ui', self)
        self.layout = QVBoxLayout()
        
        
        self.btn_browser.clicked.connect(self.open_file)

    def open_file(self):
        options =QFileDialog.options()
        fileName, _ = QFileDialog.getOpenFileName(self, "open image file",","",images(*..png)",options= options)
        if fileName:
            # self.img = cv2.imread(fileName)
            self.displayImage(self.img, self.originview)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = Image_Viewer()
    viewer.show()
    sys.exit(app.exec_())
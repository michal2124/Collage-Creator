from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from pathlib import Path, PurePath
import cv2

from Functions import *

class Ui_CollageCreator(QDialog):
    def setupUi(self, CollageCreator):
        CollageCreator.setObjectName("CollageCreator")
        CollageCreator.resize(615, 445)
        CollageCreator.setMinimumSize(QtCore.QSize(615, 445))
        CollageCreator.setMaximumSize(QtCore.QSize(615, 445))
        CollageCreator.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(CollageCreator)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 180, 526, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 0, 20, 0)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.radio_optimized = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio_optimized.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_optimized.setFont(font)
        self.radio_optimized.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.radio_optimized.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radio_optimized.setChecked(True)
        self.radio_optimized.setObjectName("radio_optimized")
        self.gridLayout.addWidget(self.radio_optimized, 1, 1, 1, 1)
        self.frame_size = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame_size.setFont(font)
        self.frame_size.setObjectName("frame_size")
        self.frame_size.addItem("")
        self.frame_size.addItems(['9x13', '10x15', '13x18'])
        self.gridLayout.addWidget(self.frame_size, 6, 1, 1, 1)
        self.label_frame = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_frame.setFont(font)
        self.label_frame.setObjectName("label_frame")
        self.gridLayout.addWidget(self.label_frame, 6, 0, 1, 1)
        self.radio_manual = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_manual.setFont(font)
        self.radio_manual.setObjectName("radio_manual")
        self.gridLayout.addWidget(self.radio_manual, 1, 2, 1, 1)
        self.label_arrangement = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_arrangement.setFont(font)
        self.label_arrangement.setObjectName("label_arrangement")
        self.gridLayout.addWidget(self.label_arrangement, 1, 0, 1, 1)
        self.collection_cut = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.collection_cut.setObjectName("collection_cut")
        self.gridLayout.addWidget(self.collection_cut, 2, 2, 1, 1)
        self.label_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_scale.setFont(font)
        self.label_scale.setObjectName("label_scale")
        self.gridLayout.addWidget(self.label_scale, 7, 0, 1, 1)
        self.val_scale = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.val_scale.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.val_scale.setFont(font)
        self.val_scale.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.val_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_scale.setMaximum(5.0)
        self.val_scale.setSingleStep(0.1)
        self.val_scale.setProperty("value", 1.0)
        self.val_scale.setObjectName("val_scale")
        self.gridLayout.addWidget(self.val_scale, 7, 1, 1, 1)
        self.label_collection = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_collection.setFont(font)
        self.label_collection.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_collection.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_collection.setObjectName("label_collection")
        self.gridLayout.addWidget(self.label_collection, 2, 0, 1, 1)
        self.collage_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.collage_name.setFont(font)
        self.collage_name.setAlignment(QtCore.Qt.AlignCenter)
        self.collage_name.setObjectName("collage_name")
        self.gridLayout.addWidget(self.collage_name, 3, 1, 1, 1)
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 3, 0, 1, 1)
        self.select_picture = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.select_picture.setFont(font)
        self.select_picture.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.select_picture.setObjectName("select_picture")
        self.gridLayout.addWidget(self.select_picture, 3, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 380, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.decription = QtWidgets.QLabel(self.centralwidget)
        self.decription.setGeometry(QtCore.QRect(10, 10, 561, 141))
        self.decription.setTextFormat(QtCore.Qt.MarkdownText)
        self.decription.setWordWrap(True)
        self.decription.setObjectName("decription")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 65, 595, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 150, 595, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        CollageCreator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CollageCreator)
        self.statusbar.setObjectName("statusbar")
        CollageCreator.setStatusBar(self.statusbar)
        self.pushButton.setDefault(True)

        self.retranslateUi(CollageCreator)
        QtCore.QMetaObject.connectSlotsByName(CollageCreator)
        
        self.select_picture.clicked.connect(self.browse_files)
        self.pushButton.clicked.connect(self.validate_file_input)      

    def retranslateUi(self, CollageCreator):
        _translate = QtCore.QCoreApplication.translate
        CollageCreator.setWindowTitle(_translate("CollageCreator", "Collage Creator"))
        self.radio_optimized.setText(_translate("CollageCreator", "Optimized"))
        self.frame_size.setItemText(0, _translate("CollageCreator", "15x20"))
        self.label_frame.setText(_translate("CollageCreator", "Frame size:"))
        self.radio_manual.setText(_translate("CollageCreator", "Manual"))
        self.label_arrangement.setText(_translate("CollageCreator", "Arrangement:"))
        self.collection_cut.setText(_translate("CollageCreator", "Cut out from collection"))
        self.label_scale.setText(_translate("CollageCreator", "Scale selected image:"))
        self.label_collection.setText(_translate("CollageCreator", "Segment cutting out functionality:"))
        self.collage_name.setText(_translate("CollageCreator", "collage_name"))
        self.label_name.setText(_translate("CollageCreator", "Input your collage name:"))
        self.select_picture.setText(_translate("CollageCreator", "Select picture / collection"))
        self.pushButton.setText(_translate("CollageCreator", "Create Collage"))
        self.decription.setText(_translate("CollageCreator", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Collage Creator is the programme to input picture and its copies into a selected frame.</span></p><p><span style=\" font-size:medium; font-weight:700;\"><br/>Arrangement</span><span style=\" font-size:medium;\"> of copies inside a frame may be selected manually or be optimized by the programme to fit maximum quantity of pictures into the frame.<br/></span><span style=\" font-size:medium; font-weight:700;\">Functionality of segment cutting</span><span style=\" font-size:medium;\"> out allows to crop desired picture from the collection to put it into the frame. </span></p></body></html>"))
    
    def browse_files(self):
        mypath = Path().absolute()
        filePath = mypath / r'Desktop\GIT\CollageCreator\Pictures'
        
        global picture_file
        picture_file = QFileDialog.getOpenFileName(self, 'Open file', str(filePath), 'Images (*.png, *.xmp *.jpg)')
    
    def validate_file_input(self):
        try:
            picture_file[0]
        except:
            self.show_message('File not found ','No picture was selected.\nPlease select picture or collection.', 'warning')
            return
        if not picture_file[0].lower().endswith((".jpg", ".jpeg", ".png")):
            self.show_message('Invalid file format',"File with invaid extension was selected.\nPlease select .jpg .jpeg .png image.", 'warning')
            return
        filename = self.collage_name.text()
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            self.show_filename_pop_up("Excessive file name","Your file will be saved as .jpg.\nYou shouldn't specify extension in your collage's name.\nDo you like to correct name?" )
        else:
            self.check_mode()
              
    def check_mode(self):        
        if self.collection_cut.isChecked():
            if self.radio_optimized.isChecked():
                self.qx, self.qy, self.qxr, self.qyr, self.rot = [None]*5
                self.open_segment_form()
            else:
                self.open_segment_form()    
        else:
            if self.radio_optimized.isChecked():
                self.y, self.x, self.h, self.w, self.qx, self.qy, self.qxr, self.qyr, self.rot = [None]*9
                self.generate_collage()
            else:
                self.y, self.x, self.h, self.w = [None]*4
                self.open_arrangement_form()
    
    def generate_collage(self):
        collection = self.collection_cut.isChecked()
        manual = self.radio_manual.isChecked()
        source = picture_file[0]
        photo = self.frame_size.currentText()
        scale = round(self.val_scale.value(),2)
        name = self.collage_name.text()
        name = str(PurePath(source).parent / name )
        
        create_collage(collection, manual, source, photo, scale, name, 1, self.y, self.x, self.h, self.w, self.qx, self.qy, self.qxr, self.qyr, self.rot)

    def open_arrangement_form(self):
        self.arrangement_form = QtWidgets.QWidget()
        self.ui_arrangement = Ui_arrangementForm()
        self.ui_arrangement.setupUi(self.arrangement_form)
        self.arrangement_form.show()
    
    def open_segment_form(self):
        self.segment_form = QtWidgets.QWidget()
        self.ui_segment = Ui_segmentForm()
        self.ui_segment.setupUi(self.segment_form)
        self.segment_form.show()
            
    def show_message(self, title, message, level="warning"):
        if level == "info":
            QMessageBox.information(self, title, message)
        elif level == "warning":
            QMessageBox.warning(self, title, message)
        
    def show_filename_pop_up(self, title, message):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)        
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Yes)
        result = msg.exec_()
        
        if result == QMessageBox.Yes:
            msg.close()
        elif result == QMessageBox.Ignore:
            self.check_mode()
    
class Ui_arrangementForm(QDialog):
    def setupUi(self, arrangementForm):
        arrangementForm.setObjectName("arrangementForm")
        arrangementForm.resize(415, 255)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arrangementForm.sizePolicy().hasHeightForWidth())
        arrangementForm.setSizePolicy(sizePolicy)
        arrangementForm.setMinimumSize(QtCore.QSize(415, 255))
        arrangementForm.setMaximumSize(QtCore.QSize(415, 255))
        self.instruction = QtWidgets.QLabel(arrangementForm)
        self.instruction.setGeometry(QtCore.QRect(10, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instruction.setFont(font)
        self.instruction.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.instruction.setWordWrap(True)
        self.instruction.setObjectName("instruction")
        self.gridLayoutWidget = QtWidgets.QWidget(arrangementForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 334, 143))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_qxr = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_qxr.setFont(font)
        self.label_qxr.setObjectName("label_qxr")
        self.gridLayout.addWidget(self.label_qxr, 2, 0, 1, 1)
        self.label_qyr = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_qyr.setFont(font)
        self.label_qyr.setObjectName("label_qyr")
        self.gridLayout.addWidget(self.label_qyr, 3, 0, 1, 1)
        self.label_qy = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_qy.setFont(font)
        self.label_qy.setObjectName("label_qy")
        self.gridLayout.addWidget(self.label_qy, 1, 0, 1, 1)
        self.label_qx = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_qx.setFont(font)
        self.label_qx.setObjectName("label_qx")
        self.gridLayout.addWidget(self.label_qx, 0, 0, 1, 1)
        self.val_qx = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.val_qx.setObjectName("val_qx")
        self.gridLayout.addWidget(self.val_qx, 0, 1, 1, 1)
        self.val_qy = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.val_qy.setObjectName("val_qy")
        self.gridLayout.addWidget(self.val_qy, 1, 1, 1, 1)
        self.val_qxr = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.val_qxr.setObjectName("val_qxr")
        self.gridLayout.addWidget(self.val_qxr, 2, 1, 1, 1)
        self.val_qyr = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.val_qyr.setObjectName("val_qyr")
        self.gridLayout.addWidget(self.val_qyr, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(arrangementForm)
        self.pushButton.setGeometry(QtCore.QRect(320, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.rotation = QtWidgets.QCheckBox(arrangementForm)
        self.rotation.setGeometry(QtCore.QRect(30, 210, 141, 21))
        self.rotation.setObjectName("rotation")
        self.pushButton.setDefault(True)

        self.retranslateUi(arrangementForm)
        QtCore.QMetaObject.connectSlotsByName(arrangementForm)
        
        self.pushButton.clicked.connect(lambda: self.get_values(arrangementForm))

    def retranslateUi(self, arrangementForm):
        _translate = QtCore.QCoreApplication.translate
        arrangementForm.setWindowTitle(_translate("arrangementForm", "Arrangement Form"))
        self.instruction.setText(_translate("arrangementForm", "Input pictures arrangement in frame. Set quantity of rows and columns."))
        self.label_qxr.setText(_translate("arrangementForm", "Columns of side-oriented pictures"))
        self.label_qyr.setText(_translate("arrangementForm", "Rows of side-oriented pictures"))
        self.label_qy.setText(_translate("arrangementForm", "Rows of normal-oriented pictures"))
        self.label_qx.setText(_translate("arrangementForm", "Columns of normal-oriented pictures"))
        self.pushButton.setText(_translate("arrangementForm", "Ok"))
        self.rotation.setText(_translate("arrangementForm", "Rotate initial picture"))

    def get_values(self, arrangementForm):
        ui_main.qx = self.val_qx.value()
        ui_main.qy = self.val_qy.value()
        ui_main.qxr = self.val_qxr.value()
        ui_main.qyr = self.val_qyr.value()
        ui_main.rot = self.rotation.isChecked()
        
        self.validate_arrangement_input(arrangementForm)
        
    def validate_arrangement_input(self, arrangementForm):
        try:
            ui_main.generate_collage()
            arrangementForm.hide()
        except ValueError as e:
            if 'Image larger than frame' in str(e):
                self.show_message('Invalid input ','Image larger than frame.\nTry to change scale.')
            elif 'Arrangement exceeds frame width and height' in str(e):
                self.show_message('Invalid input ','Arrangement exceeds frame width and height.\nTry to change quantity of rows and columns.')
            elif 'Arrangement exceeds frame width' in str(e):
                self.show_message('Invalid input ','Arrangement exceeds frame width.\nTry to change quantity of columns.')
            elif 'Arrangement exceeds frame height' in str(e):
                self.show_message('Invalid input ','Arrangement exceeds frame height.\nTry to change quantity of rows.')
            return

    def show_message(self, title, message, level="warning"):
        if level == "info":
            QMessageBox.information(self, title, message)
        elif level == "warning":
            QMessageBox.warning(self, title, message)  
        
class Ui_segmentForm(QDialog):
    def setupUi(self, segmentForm):
        segmentForm.setObjectName("segmentForm")
        segmentForm.resize(285, 245)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(segmentForm.sizePolicy().hasHeightForWidth())
        segmentForm.setSizePolicy(sizePolicy)
        segmentForm.setMinimumSize(QtCore.QSize(285, 245))
        segmentForm.setMaximumSize(QtCore.QSize(285, 245))
        self.instruction = QtWidgets.QLabel(segmentForm)
        self.instruction.setGeometry(QtCore.QRect(10, 10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instruction.setFont(font)
        self.instruction.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.instruction.setWordWrap(True)
        self.instruction.setObjectName("instruction")
        self.gridLayoutWidget = QtWidgets.QWidget(segmentForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 222, 134))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_y = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_y.setFont(font)
        self.label_y.setObjectName("label_y")
        self.gridLayout.addWidget(self.label_y, 1, 0, 1, 1)
        self.label_h = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_h.setFont(font)
        self.label_h.setObjectName("label_h")
        self.gridLayout.addWidget(self.label_h, 3, 0, 1, 1)
        self.val_x = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.val_x.setMaximumSize(QtCore.QSize(60, 16777215))
        self.val_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_x.setObjectName("val_x")
        self.val_y = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.val_y.setMinimumSize(QtCore.QSize(0, 0))
        self.val_y.setMaximumSize(QtCore.QSize(60, 16777215))
        self.val_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_y.setObjectName("val_y")
        self.gridLayout.addWidget(self.val_y, 1, 1, 1, 1)
        self.val_w = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.val_w.setMaximumSize(QtCore.QSize(60, 16777215))
        self.val_w.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_w.setObjectName("val_w")
        self.gridLayout.addWidget(self.val_w, 2, 1, 1, 1)
        self.val_h = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.val_h.setMaximumSize(QtCore.QSize(60, 16777215))
        self.val_h.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_h.setObjectName("val_h")
        self.gridLayout.addWidget(self.val_h, 3, 1, 1, 1)
        self.label_x = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_x.setFont(font)
        self.label_x.setObjectName("label_x")
        self.gridLayout.addWidget(self.label_x, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.val_x, 0, 1, 1, 1)
        self.label_w = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_w.setFont(font)
        self.label_w.setObjectName("label_w")
        self.gridLayout.addWidget(self.label_w, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(segmentForm)
        self.pushButton.setGeometry(QtCore.QRect(190, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setDefault(True)

        self.retranslateUi(segmentForm)
        QtCore.QMetaObject.connectSlotsByName(segmentForm)
        
        self.pushButton.clicked.connect(lambda: self.get_values(segmentForm))

    def retranslateUi(self, segmentForm):
        _translate = QtCore.QCoreApplication.translate
        segmentForm.setWindowTitle(_translate("segmentForm", "Segment Form"))
        self.instruction.setText(_translate("segmentForm", "Input parameters to cut out segment from frame."))
        self.val_w.setText(_translate("segmentForm", "w"))
        self.label_y.setText(_translate("segmentForm", "Frame height location:"))
        self.label_h.setText(_translate("segmentForm", "Segment height:"))
        self.val_h.setText(_translate("segmentForm", "h"))
        self.val_y.setText(_translate("segmentForm", "y"))
        self.label_x.setText(_translate("segmentForm", "Frame width location:"))
        self.val_x.setText(_translate("segmentForm", "x"))
        self.label_w.setText(_translate("segmentForm", "Segment width:"))
        self.pushButton.setText(_translate("segmentForm", "Ok"))
        
    def get_values(self, segmentForm):
        try:
            ui_main.x = int(self.val_x.text())
            ui_main.y = int(self.val_y.text())
            ui_main.w = int(self.val_w.text())
            ui_main.h = int(self.val_h.text())
        except ValueError:
            self.show_message('Invalid input ','Input values are in an invalid format.\nPlease enter numeric values.')
            return
        try:
            self.validate_segment_input()
        except ValueError:
            self.show_message('Invalid input ','Cropping out of frame.\nPlease change x, y parameters.')
            return
        
        segmentForm.hide()
        if ui_main.radio_optimized.isChecked():
           ui_main.generate_collage()
        else:
           ui_main.open_arrangement_form()
              
    def validate_segment_input(self):
        source = picture_file[0]
        img = cv2.imread(source, 1)
        ih, iw, _ = img.shape
        if ui_main.y > ih or ui_main.x > iw:
            raise ValueError("Cropping out of frame.")
            
    def show_message(self, title, message, level="warning"):
        if level == "info":
            QMessageBox.information(self, title, message)
        elif level == "warning":
            QMessageBox.warning(self, title, message)
                                       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_main = Ui_CollageCreator()
    ui_main.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sam\.qgis2\python\plugins\Figure_Builder\forms\ui_Figure_Builder_dialog.ui'
#
# Created: Sat Jan 20 16:33:13 2018
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Figure_BuilderDialogBase(object):
    def setupUi(self, Figure_BuilderDialogBase):
        Figure_BuilderDialogBase.setObjectName(_fromUtf8("Figure_BuilderDialogBase"))
        Figure_BuilderDialogBase.resize(953, 765)
        self.Master_Buttons = QtGui.QDialogButtonBox(Figure_BuilderDialogBase)
        self.Master_Buttons.setGeometry(QtCore.QRect(730, 680, 161, 32))
        self.Master_Buttons.setOrientation(QtCore.Qt.Horizontal)
        self.Master_Buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.Master_Buttons.setObjectName(_fromUtf8("Master_Buttons"))
        self.Figure_List_BOX = QtGui.QListView(Figure_BuilderDialogBase)
        self.Figure_List_BOX.setGeometry(QtCore.QRect(10, 73, 301, 551))
        self.Figure_List_BOX.setObjectName(_fromUtf8("Figure_List_BOX"))
        self.Figure_Caption_Top_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Figure_Caption_Top_CAPTION.setGeometry(QtCore.QRect(340, 130, 281, 16))
        self.Figure_Caption_Top_CAPTION.setObjectName(_fromUtf8("Figure_Caption_Top_CAPTION"))
        self.Fig_Num_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Fig_Num_CAPTION.setGeometry(QtCore.QRect(340, 210, 281, 16))
        self.Fig_Num_CAPTION.setObjectName(_fromUtf8("Fig_Num_CAPTION"))
        self.Figure_Title_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Figure_Title_CAPTION.setGeometry(QtCore.QRect(340, 90, 281, 16))
        self.Figure_Title_CAPTION.setObjectName(_fromUtf8("Figure_Title_CAPTION"))
        self.Figure_list_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Figure_list_CAPTION.setGeometry(QtCore.QRect(10, 53, 281, 16))
        self.Figure_list_CAPTION.setObjectName(_fromUtf8("Figure_list_CAPTION"))
        self.Figure_Control_Path_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Figure_Control_Path_CAPTION.setGeometry(QtCore.QRect(10, 0, 291, 16))
        self.Figure_Control_Path_CAPTION.setObjectName(_fromUtf8("Figure_Control_Path_CAPTION"))
        self.Control_Ref_Search_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Control_Ref_Search_BUTTON.setGeometry(QtCore.QRect(254, 20, 51, 21))
        self.Control_Ref_Search_BUTTON.setObjectName(_fromUtf8("Control_Ref_Search_BUTTON"))
        self.Page_Layout_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Page_Layout_CAPTION.setGeometry(QtCore.QRect(670, 50, 121, 16))
        self.Page_Layout_CAPTION.setObjectName(_fromUtf8("Page_Layout_CAPTION"))
        self.Page_Layout_COMBO = QtGui.QComboBox(Figure_BuilderDialogBase)
        self.Page_Layout_COMBO.setGeometry(QtCore.QRect(670, 70, 271, 22))
        self.Page_Layout_COMBO.setObjectName(_fromUtf8("Page_Layout_COMBO"))
        self.Page_Layout_COMBO.addItem(_fromUtf8(""))
        self.Page_Layout_COMBO.addItem(_fromUtf8(""))
        self.Page_Layout_COMBO.addItem(_fromUtf8(""))
        self.Page_Layout_COMBO.addItem(_fromUtf8(""))
        self.Layer_Search_BUTTON_ = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Layer_Search_BUTTON_.setGeometry(QtCore.QRect(600, 540, 51, 21))
        self.Layer_Search_BUTTON_.setObjectName(_fromUtf8("Layer_Search_BUTTON_"))
        self.Shift_Down_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Shift_Down_BUTTON.setGeometry(QtCore.QRect(580, 460, 41, 23))
        self.Shift_Down_BUTTON.setObjectName(_fromUtf8("Shift_Down_BUTTON"))
        self.Shift_up_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Shift_up_BUTTON.setGeometry(QtCore.QRect(540, 460, 31, 23))
        self.Shift_up_BUTTON.setObjectName(_fromUtf8("Shift_up_BUTTON"))
        self.Layer_List_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Layer_List_CAPTION.setGeometry(QtCore.QRect(340, 260, 281, 16))
        self.Layer_List_CAPTION.setObjectName(_fromUtf8("Layer_List_CAPTION"))
        self.Layer_Search_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Layer_Search_BOX.setGeometry(QtCore.QRect(340, 540, 261, 21))
        self.Layer_Search_BOX.setObjectName(_fromUtf8("Layer_Search_BOX"))
        self.Remove_Layer_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Remove_Layer_BUTTON.setGeometry(QtCore.QRect(340, 490, 81, 23))
        self.Remove_Layer_BUTTON.setObjectName(_fromUtf8("Remove_Layer_BUTTON"))
        self.Add_Layer_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Add_Layer_BUTTON.setGeometry(QtCore.QRect(340, 460, 81, 23))
        self.Add_Layer_BUTTON.setObjectName(_fromUtf8("Add_Layer_BUTTON"))
        self.Populate_View_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Populate_View_BUTTON.setGeometry(QtCore.QRect(670, 230, 151, 31))
        self.Populate_View_BUTTON.setObjectName(_fromUtf8("Populate_View_BUTTON"))
        self.Centroid_Y_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Centroid_Y_CAPTION.setGeometry(QtCore.QRect(830, 130, 121, 16))
        self.Centroid_Y_CAPTION.setObjectName(_fromUtf8("Centroid_Y_CAPTION"))
        self.Centroid_Y_Coord_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Centroid_Y_Coord_BOX.setGeometry(QtCore.QRect(822, 150, 121, 20))
        self.Centroid_Y_Coord_BOX.setObjectName(_fromUtf8("Centroid_Y_Coord_BOX"))
        self.Centroid_X_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Centroid_X_CAPTION.setGeometry(QtCore.QRect(670, 130, 121, 16))
        self.Centroid_X_CAPTION.setObjectName(_fromUtf8("Centroid_X_CAPTION"))
        self.Figure_Zoom_Centroid_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Figure_Zoom_Centroid_CAPTION.setGeometry(QtCore.QRect(670, 107, 81, 16))
        self.Figure_Zoom_Centroid_CAPTION.setObjectName(_fromUtf8("Figure_Zoom_Centroid_CAPTION"))
        self.Centroid_X_Coord_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Centroid_X_Coord_BOX.setGeometry(QtCore.QRect(670, 150, 121, 20))
        self.Centroid_X_Coord_BOX.setObjectName(_fromUtf8("Centroid_X_Coord_BOX"))
        self.Zoom_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Zoom_CAPTION.setGeometry(QtCore.QRect(670, 180, 261, 16))
        self.Zoom_CAPTION.setObjectName(_fromUtf8("Zoom_CAPTION"))
        self.Zoom_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Zoom_BOX.setGeometry(QtCore.QRect(670, 200, 271, 20))
        self.Zoom_BOX.setObjectName(_fromUtf8("Zoom_BOX"))
        self.Control_Ref_Search_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Control_Ref_Search_BOX.setGeometry(QtCore.QRect(10, 20, 241, 21))
        self.Control_Ref_Search_BOX.setObjectName(_fromUtf8("Control_Ref_Search_BOX"))
        self.Figure_Title_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Figure_Title_BOX.setGeometry(QtCore.QRect(340, 110, 311, 21))
        self.Figure_Title_BOX.setObjectName(_fromUtf8("Figure_Title_BOX"))
        self.Figure_Caption_Top_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Figure_Caption_Top_BOX.setGeometry(QtCore.QRect(340, 150, 311, 21))
        self.Figure_Caption_Top_BOX.setObjectName(_fromUtf8("Figure_Caption_Top_BOX"))
        self.Figure_Number_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Figure_Number_BOX.setGeometry(QtCore.QRect(340, 230, 311, 21))
        self.Figure_Number_BOX.setObjectName(_fromUtf8("Figure_Number_BOX"))
        self.Style_Directory_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Style_Directory_CAPTION.setGeometry(QtCore.QRect(340, 0, 221, 16))
        self.Style_Directory_CAPTION.setObjectName(_fromUtf8("Style_Directory_CAPTION"))
        self.Style_Dir_Search_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Style_Dir_Search_BUTTON.setGeometry(QtCore.QRect(600, 20, 51, 21))
        self.Style_Dir_Search_BUTTON.setObjectName(_fromUtf8("Style_Dir_Search_BUTTON"))
        self.Style_Dir_Search_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Style_Dir_Search_BOX.setGeometry(QtCore.QRect(340, 20, 261, 21))
        self.Style_Dir_Search_BOX.setObjectName(_fromUtf8("Style_Dir_Search_BOX"))
        self.Load_Style_Dir_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Load_Style_Dir_BUTTON.setGeometry(QtCore.QRect(600, 0, 51, 21))
        self.Load_Style_Dir_BUTTON.setObjectName(_fromUtf8("Load_Style_Dir_BUTTON"))
        self.Style_Select_COMBO = QtGui.QComboBox(Figure_BuilderDialogBase)
        self.Style_Select_COMBO.setGeometry(QtCore.QRect(340, 640, 311, 22))
        self.Style_Select_COMBO.setObjectName(_fromUtf8("Style_Select_COMBO"))
        self.New_Figure_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.New_Figure_BUTTON.setGeometry(QtCore.QRect(10, 630, 51, 23))
        self.New_Figure_BUTTON.setObjectName(_fromUtf8("New_Figure_BUTTON"))
        self.Duplicate_Figure_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Duplicate_Figure_BUTTON.setGeometry(QtCore.QRect(70, 630, 61, 23))
        self.Duplicate_Figure_BUTTON.setObjectName(_fromUtf8("Duplicate_Figure_BUTTON"))
        self.Remove_Figure_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Remove_Figure_BUTTON.setGeometry(QtCore.QRect(140, 630, 61, 23))
        self.Remove_Figure_BUTTON.setObjectName(_fromUtf8("Remove_Figure_BUTTON"))
        self.Figure_Name_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Figure_Name_CAPTION.setGeometry(QtCore.QRect(340, 50, 281, 16))
        self.Figure_Name_CAPTION.setObjectName(_fromUtf8("Figure_Name_CAPTION"))
        self.Figure_Name_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Figure_Name_BOX.setGeometry(QtCore.QRect(340, 70, 311, 21))
        self.Figure_Name_BOX.setObjectName(_fromUtf8("Figure_Name_BOX"))
        self.Save_Figure_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Save_Figure_BUTTON.setGeometry(QtCore.QRect(210, 630, 61, 23))
        self.Save_Figure_BUTTON.setObjectName(_fromUtf8("Save_Figure_BUTTON"))
        self.CRS_Search_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.CRS_Search_BUTTON.setGeometry(QtCore.QRect(890, 20, 51, 21))
        self.CRS_Search_BUTTON.setObjectName(_fromUtf8("CRS_Search_BUTTON"))
        self.CRS_Search_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.CRS_Search_BOX.setGeometry(QtCore.QRect(670, 20, 221, 21))
        self.CRS_Search_BOX.setObjectName(_fromUtf8("CRS_Search_BOX"))
        self.CRS_Caption = QtGui.QLabel(Figure_BuilderDialogBase)
        self.CRS_Caption.setGeometry(QtCore.QRect(670, 0, 411, 16))
        self.CRS_Caption.setObjectName(_fromUtf8("CRS_Caption"))
        self.Add_All_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Add_All_BUTTON.setGeometry(QtCore.QRect(430, 460, 91, 23))
        self.Add_All_BUTTON.setObjectName(_fromUtf8("Add_All_BUTTON"))
        self.Legend_Entry_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Legend_Entry_BOX.setGeometry(QtCore.QRect(340, 590, 311, 21))
        self.Legend_Entry_BOX.setObjectName(_fromUtf8("Legend_Entry_BOX"))
        self.Layer_Loc_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Layer_Loc_CAPTION.setGeometry(QtCore.QRect(340, 520, 281, 16))
        self.Layer_Loc_CAPTION.setObjectName(_fromUtf8("Layer_Loc_CAPTION"))
        self.Legend_Entry_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Legend_Entry_CAPTION.setGeometry(QtCore.QRect(340, 570, 281, 16))
        self.Legend_Entry_CAPTION.setObjectName(_fromUtf8("Legend_Entry_CAPTION"))
        self.VCP_Selection_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.VCP_Selection_CAPTION.setGeometry(QtCore.QRect(340, 620, 281, 16))
        self.VCP_Selection_CAPTION.setObjectName(_fromUtf8("VCP_Selection_CAPTION"))
        self.Change_All_View_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Change_All_View_BUTTON.setGeometry(QtCore.QRect(840, 230, 101, 31))
        self.Change_All_View_BUTTON.setObjectName(_fromUtf8("Change_All_View_BUTTON"))
        self.Remove_Layer_All_BUTTON = QtGui.QPushButton(Figure_BuilderDialogBase)
        self.Remove_Layer_All_BUTTON.setGeometry(QtCore.QRect(430, 490, 91, 23))
        self.Remove_Layer_All_BUTTON.setObjectName(_fromUtf8("Remove_Layer_All_BUTTON"))
        self.Layer_List_TABLE = QtGui.QTableWidget(Figure_BuilderDialogBase)
        self.Layer_List_TABLE.setGeometry(QtCore.QRect(340, 280, 311, 171))
        self.Layer_List_TABLE.setObjectName(_fromUtf8("Layer_List_TABLE"))
        self.Layer_List_TABLE.setColumnCount(3)
        self.Layer_List_TABLE.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.Layer_List_TABLE.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.Layer_List_TABLE.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.Layer_List_TABLE.setHorizontalHeaderItem(2, item)
        self.Figure_Caption_Bot_CAPTION = QtGui.QLabel(Figure_BuilderDialogBase)
        self.Figure_Caption_Bot_CAPTION.setGeometry(QtCore.QRect(340, 170, 281, 16))
        self.Figure_Caption_Bot_CAPTION.setObjectName(_fromUtf8("Figure_Caption_Bot_CAPTION"))
        self.Figure_Caption_Bot_BOX = QtGui.QLineEdit(Figure_BuilderDialogBase)
        self.Figure_Caption_Bot_BOX.setGeometry(QtCore.QRect(340, 190, 311, 21))
        self.Figure_Caption_Bot_BOX.setObjectName(_fromUtf8("Figure_Caption_Bot_BOX"))

        self.retranslateUi(Figure_BuilderDialogBase)
        QtCore.QObject.connect(self.Master_Buttons, QtCore.SIGNAL(_fromUtf8("accepted()")), Figure_BuilderDialogBase.accept)
        QtCore.QObject.connect(self.Master_Buttons, QtCore.SIGNAL(_fromUtf8("rejected()")), Figure_BuilderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(Figure_BuilderDialogBase)

    def retranslateUi(self, Figure_BuilderDialogBase):
        Figure_BuilderDialogBase.setWindowTitle(_translate("Figure_BuilderDialogBase", "Figure_Builder", None))
        self.Figure_Caption_Top_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Figure Caption Top Line", None))
        self.Fig_Num_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Figure Number", None))
        self.Figure_Title_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Figure Title", None))
        self.Figure_list_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Figure List", None))
        self.Figure_Control_Path_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Figure Control File ", None))
        self.Control_Ref_Search_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Search", None))
        self.Page_Layout_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Page Layout", None))
        self.Page_Layout_COMBO.setItemText(0, _translate("Figure_BuilderDialogBase", "A4 Portrait", None))
        self.Page_Layout_COMBO.setItemText(1, _translate("Figure_BuilderDialogBase", "A4 Landscape", None))
        self.Page_Layout_COMBO.setItemText(2, _translate("Figure_BuilderDialogBase", "A3 Portrait", None))
        self.Page_Layout_COMBO.setItemText(3, _translate("Figure_BuilderDialogBase", "A3 Landscape", None))
        self.Layer_Search_BUTTON_.setText(_translate("Figure_BuilderDialogBase", "Search", None))
        self.Shift_Down_BUTTON.setText(_translate("Figure_BuilderDialogBase", "DOWN", None))
        self.Shift_up_BUTTON.setText(_translate("Figure_BuilderDialogBase", "UP", None))
        self.Layer_List_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Layer List", None))
        self.Remove_Layer_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Remove Layer", None))
        self.Add_Layer_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Add Layer", None))
        self.Populate_View_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Populate Using Current View", None))
        self.Centroid_Y_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Centroid Y-Coordinate", None))
        self.Centroid_X_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Centroid X-Coordinate", None))
        self.Figure_Zoom_Centroid_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Set Figure Area", None))
        self.Zoom_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Figure Zoom/Scale (e.g 1000 for 1cm:1000m)", None))
        self.Style_Directory_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Style Control Directory", None))
        self.Style_Dir_Search_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Search", None))
        self.Load_Style_Dir_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Load", None))
        self.New_Figure_BUTTON.setText(_translate("Figure_BuilderDialogBase", "New", None))
        self.Duplicate_Figure_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Duplicate", None))
        self.Remove_Figure_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Remove", None))
        self.Figure_Name_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Figure Save Name", None))
        self.Save_Figure_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Save", None))
        self.CRS_Search_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Search", None))
        self.CRS_Caption.setText(_translate("Figure_BuilderDialogBase", "Set Project CRS", None))
        self.Add_All_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Add to All", None))
        self.Layer_Loc_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Layer Location", None))
        self.Legend_Entry_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Legend Entry", None))
        self.VCP_Selection_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Colour Profile (Define Category Legend Entires in Style)", None))
        self.Change_All_View_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Change All View", None))
        self.Remove_Layer_All_BUTTON.setText(_translate("Figure_BuilderDialogBase", "Remove from All", None))
        item = self.Layer_List_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("Figure_BuilderDialogBase", "Location", None))
        item = self.Layer_List_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("Figure_BuilderDialogBase", "Colour", None))
        item = self.Layer_List_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("Figure_BuilderDialogBase", "Legend Entry", None))
        self.Figure_Caption_Bot_CAPTION.setText(_translate("Figure_BuilderDialogBase", "Figure Caption Bottom Line", None))


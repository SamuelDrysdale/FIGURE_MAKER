# -*- coding: utf-8 -*-
"""
/***************************************************************************
 tuflowqgis_menuDialog
                                 A QGIS plugin
 Initialises the TUFLOW menu system
                             -------------------
        begin                : 2013-08-27
        copyright            : (C) 2013 by Phillip Ryan
        email                : support@tuflow.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

#import csv

import operator
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import pickle
import glob
from figure_builder_library import *
from functools import partial
from qgis.core import QgsApplication;
from qgis.gui import QgsMapCanvas;
from qgis.gui import QgsGenericProjectionSelector
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/forms")

# ----------------------------------------------------------
#    new project
# ----------------------------------------------------------
from ui_New_Project_dialog import *
from tuflowqgis_settings import TF_Settings
class New_Project_dialog(QDialog, Ui_Ui_New_ProjectDialogBase):
	def __init__(self, iface, project):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		self.tfsettings = TF_Settings()

		# load stored settings
		self.last_chk_folder = self.tfsettings.get_last_chk_folder()
		error, message = self.tfsettings.Load() #exe, tuflow dircetory and projection
		if error:
			QMessageBox.information( self.iface.mainWindow(),"Error", "Error Loading Settings: "+message)

# ---------------------------------------------------------------------------------------------------------------------------------------			
		QObject.connect(self.Control_Ref_Search_BUTTON, SIGNAL("clicked()"), self.browse_control_ref)
		QObject.connect(self.Style_Dir_Search_BUTTON, SIGNAL("clicked()"), self.browse_stlye_control)
		QObject.connect(self.Layer_Search_BUTTON, SIGNAL("clicked()"), self.browse_layers)
		QObject.connect(self.CRS_Search_BUTTON, SIGNAL("clicked()"), self.browse_CRS)
		QObject.connect(self.Load_Style_Dir_BUTTON, SIGNAL("clicked()"), self.load_styles)
		QObject.connect(self.Populate_View_BUTTON, SIGNAL("clicked()"), partial(self.populate_view, iface))
		QObject.connect(self.Add_Layer_BUTTON, SIGNAL("clicked()"), self.add_layer)
		QObject.connect(self.Remove_Layer_BUTTON, SIGNAL("clicked()"), self.remove_layer)
		QObject.connect(self.Shift_up_BUTTON, SIGNAL("clicked()"), self.shift_up)
		QObject.connect(self.Shift_Down_BUTTON, SIGNAL("clicked()"), self.shift_down)
		
		QObject.connect(self.Level_Res1_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_level1)
		QObject.connect(self.Level_Res2_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_level2)
		QObject.connect(self.Level_Res3_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_level3)
		QObject.connect(self.Level_Res4_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_level4)
		
		QObject.connect(self.Depth_Res1_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_depth1)
		QObject.connect(self.Depth_Res2_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_depth2)
		QObject.connect(self.Depth_Res3_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_depth3)
		QObject.connect(self.Depth_Res4_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_depth4)
		
		QObject.connect(self.Velocity_Res1_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_velocity1)
		QObject.connect(self.Velocity_Res2_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_velocity2)
		QObject.connect(self.Velocity_Res3_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_velocity3)
		QObject.connect(self.Velocity_Res4_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_velocity4)
		
		QObject.connect(self.Z0_Res1_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Z01)
		QObject.connect(self.Z0_Res2_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Z02)
		QObject.connect(self.Z0_Res3_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Z03)
		QObject.connect(self.Z0_Res4_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Z04)
		
		QObject.connect(self.Z1_Res1_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Z11)
		QObject.connect(self.Z1_Res2_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Z12)
		QObject.connect(self.Z1_Res3_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Z13)
		QObject.connect(self.Z1_Res4_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Z14)
		
		QObject.connect(self.HydCat_Res1_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_HydCat1)
		QObject.connect(self.HydCat_Res2_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_HydCat2)
		QObject.connect(self.HydCat_Res3_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_HydCat3)
		QObject.connect(self.HydCat_Res4_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_HydCat4)
		
		QObject.connect(self.Risk_Precincts_Res1_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Risk_Precincts1)
		QObject.connect(self.Risk_Precincts_Res2_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Risk_Precincts2)
		QObject.connect(self.Risk_Precincts_Res3_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Risk_Precincts3)
		QObject.connect(self.Risk_Precincts_Res4_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Risk_Precincts4)
		
		QObject.connect(self.Level_Impact_Res1_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Level_Impact1)
		QObject.connect(self.Level_Impact_Res2_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Level_Impact2)
		QObject.connect(self.Level_Impact_Res3_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Level_Impact3)
		QObject.connect(self.Level_Impact_Res4_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Level_Impact4)
		
		QObject.connect(self.Velocity_Impact_Res1_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Velocity_Impact1)
		QObject.connect(self.Velocity_Impact_Res2_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Velocity_Impact2)
		QObject.connect(self.Velocity_Impact_Res3_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Velocity_Impact3)
		QObject.connect(self.Velocity_Impact_Res4_Loc_Search_BUTTON, SIGNAL("clicked()"), self.browse_Velocity_Impact4)

# ---------------------------------------------------------------------------------------------------------------------------------------	
	def browse_control_ref(self):
		newname = QFileDialog.getOpenFileName(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Control_Ref_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Control_Ref_Search_BOX.setText("Problem Saving Settings")
	
	def browse_stlye_control(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Style_Dir_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Style_Dir_Search_BOX.setText("Problem Saving Settings")
	
	def browse_layers(self):
		newname = QFileDialog.getOpenFileName(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Layer_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Layer_Search_BOX.setText("Problem Saving Settings")

	def browse_CRS(self):
		projSelector = QgsGenericProjectionSelector()
		projSelector.exec_()
		CRSName = projSelector.selectedCrsId()
		CRSName = str(CRSName)
		if CRSName != None:
			self.CRS_Search_BOX.setText(CRSName)


# ---------------------------------------------------------------------------------------------------------------------------------------					
	def populate_view(self,iface):
		self.canvas = self.iface.mapCanvas()

		Zoom_Value = self.iface.mapCanvas().scale()
		Zoom_Value = str(Zoom_Value)

		e = self.canvas.extent()

		XCoord = (e.xMaximum()-e.xMinimum())/2+e.xMinimum()
		YCoord = (e.yMaximum()-e.yMinimum())/2+e.yMinimum()

		XCoord = str(XCoord)
		YCoord = str(YCoord)

		self.Centroid_X_Coord_BOX.setText(XCoord)
		self.Centroid_Y_Coord_BOX.setText(YCoord)
		self.Zoom_BOX.setText(Zoom_Value)

# ---------------------------------------------------------------------------------------------------------------------------------------
	def load_styles(self):
		stylepath = self.Style_Dir_Search_BOX.text()
		stylepath = str(stylepath)
		stylepath = stylepath + '/*'
		f = []
		f = glob.glob(stylepath)
		self.Style_Select_COMBO.clear()
		self.Style_Select_COMBO.addItems(f)

		self.Level_Res1_VCP_SELECT.clear()
		self.Level_Res1_VCP_SELECT.addItems(f)

		self.Level_Res2_VCP_SELECT.clear()
		self.Level_Res2_VCP_SELECT.addItems(f)

		self.Level_Res3_VCP_SELECT.clear()
		self.Level_Res3_VCP_SELECT.addItems(f)

		self.Level_Res4_VCP_SELECT.clear()
		self.Level_Res4_VCP_SELECT.addItems(f)

		self.Depth_Res1_VCP_SELECT.clear()
		self.Depth_Res1_VCP_SELECT.addItems(f)

		self.Depth_Res2_VCP_SELECT.clear()
		self.Depth_Res2_VCP_SELECT.addItems(f)

		self.Depth_Res3_VCP_SELECT.clear()
		self.Depth_Res3_VCP_SELECT.addItems(f)

		self.Depth_Res4_VCP_SELECT.clear()
		self.Depth_Res4_VCP_SELECT.addItems(f)

		self.Velocity_Res1_VCP_SELECT.clear()
		self.Velocity_Res1_VCP_SELECT.addItems(f)

		self.Velocity_Res2_VCP_SELECT.clear()
		self.Velocity_Res2_VCP_SELECT.addItems(f)

		self.Velocity_Res3_VCP_SELECT.clear()
		self.Velocity_Res3_VCP_SELECT.addItems(f)

		self.Velocity_Res4_VCP_SELECT.clear()
		self.Velocity_Res4_VCP_SELECT.addItems(f)

		self.Z0_Res1_VCP_SELECT.clear()
		self.Z0_Res1_VCP_SELECT.addItems(f)

		self.Z0_Res2_VCP_SELECT.clear()
		self.Z0_Res2_VCP_SELECT.addItems(f)

		self.Z0_Res3_VCP_SELECT.clear()
		self.Z0_Res3_VCP_SELECT.addItems(f)

		self.Z0_Res4_VCP_SELECT.clear()
		self.Z0_Res4_VCP_SELECT.addItems(f)

		self.Z1_Res1_VCP_SELECT.clear()
		self.Z1_Res1_VCP_SELECT.addItems(f)

		self.Z1_Res2_VCP_SELECT.clear()
		self.Z1_Res2_VCP_SELECT.addItems(f)

		self.Z1_Res3_VCP_SELECT.clear()
		self.Z1_Res3_VCP_SELECT.addItems(f)

		self.Z1_Res4_VCP_SELECT.clear()
		self.Z1_Res4_VCP_SELECT.addItems(f)

		self.HydCat_Res1_VCP_SELECT.clear()
		self.HydCat_Res1_VCP_SELECT.addItems(f)

		self.HydCat_Res2_VCP_SELECT.clear()
		self.HydCat_Res2_VCP_SELECT.addItems(f)

		self.HydCat_Res3_VCP_SELECT.clear()
		self.HydCat_Res3_VCP_SELECT.addItems(f)

		self.HydCat_Res4_VCP_SELECT.clear()
		self.HydCat_Res4_VCP_SELECT.addItems(f)

		self.Risk_Precincts_Res1_VCP_SELECT.clear()
		self.Risk_Precincts_Res1_VCP_SELECT.addItems(f)

		self.Risk_Precincts_Res2_VCP_SELECT.clear()
		self.Risk_Precincts_Res2_VCP_SELECT.addItems(f)

		self.Risk_Precincts_Res3_VCP_SELECT.clear()
		self.Risk_Precincts_Res3_VCP_SELECT.addItems(f)

		self.Risk_Precincts_Res4_VCP_SELECT.clear()
		self.Risk_Precincts_Res4_VCP_SELECT.addItems(f)

		self.Level_Impact_Res1_VCP_SELECT.clear()
		self.Level_Impact_Res1_VCP_SELECT.addItems(f)

		self.Level_Impact_Res2_VCP_SELECT.clear()
		self.Level_Impact_Res2_VCP_SELECT.addItems(f)

		self.Level_Impact_Res3_VCP_SELECT.clear()
		self.Level_Impact_Res3_VCP_SELECT.addItems(f)

		self.Level_Impact_Res4_VCP_SELECT.clear()
		self.Level_Impact_Res4_VCP_SELECT.addItems(f)

		self.Velocity_Impact_Res1_VCP_SELECT.clear()
		self.Velocity_Impact_Res1_VCP_SELECT.addItems(f)

		self.Velocity_Impact_Res2_VCP_SELECT.clear()
		self.Velocity_Impact_Res2_VCP_SELECT.addItems(f)

		self.Velocity_Impact_Res3_VCP_SELECT.clear()
		self.Velocity_Impact_Res3_VCP_SELECT.addItems(f)

		self.Velocity_Impact_Res4_VCP_SELECT.clear()
		self.Velocity_Impact_Res4_VCP_SELECT.addItems(f)

	def add_layer(self):
		FileLoc = self.Layer_Search_BOX.text()
		FileLoc = str(FileLoc)
		FileVCP = self.Style_Select_COMBO.currentText()
		FileLegendEnt = self.Legend_Entry_BOX.text()
		FileLegendEnt = str(FileLegendEnt)
		ListEnt = [FileLoc, FileVCP, FileLegendEnt]

		rowPosition = self.Layer_List_TABLE.rowCount()
		self.Layer_List_TABLE.insertRow(rowPosition)
		self.Layer_List_TABLE.setItem(rowPosition, 0, QtGui.QTableWidgetItem(FileLoc))
		self.Layer_List_TABLE.setItem(rowPosition, 1, QtGui.QTableWidgetItem(FileVCP))
		self.Layer_List_TABLE.setItem(rowPosition, 2, QtGui.QTableWidgetItem(FileLegendEnt))
	
	def remove_layer(self):
		indices = self.Layer_List_TABLE.currentRow()
		self.Layer_List_TABLE.removeRow(indices)
	
	def shift_up(self):
		row = self.Layer_List_TABLE.currentRow()
		if row > 0:
			rowPosition = row - 1
			self.Layer_List_TABLE.insertRow(rowPosition)
			FileLoc = self.Layer_List_TABLE.item(row + 1,0)
			FileVCP = self.Layer_List_TABLE.item(row + 1,1)
			FileLegendEnt = self.Layer_List_TABLE.item(row + 1,2)
			self.Layer_List_TABLE.setItem(rowPosition, 0, QtGui.QTableWidgetItem(FileLoc))
			self.Layer_List_TABLE.setItem(rowPosition, 1, QtGui.QTableWidgetItem(FileVCP))
			self.Layer_List_TABLE.setItem(rowPosition, 2, QtGui.QTableWidgetItem(FileLegendEnt))
			self.Layer_List_TABLE.removeRow(row + 1)

	def shift_down(self):
		row = self.Layer_List_TABLE.currentRow()
		if row < self.Layer_List_TABLE.rowCount()-1:
			rowPosition = row + 2
			self.Layer_List_TABLE.insertRow(rowPosition)
			FileLoc = self.Layer_List_TABLE.item(row, 0)
			FileVCP = self.Layer_List_TABLE.item(row, 1)
			FileLegendEnt = self.Layer_List_TABLE.item(row, 2)
			self.Layer_List_TABLE.setItem(rowPosition, 0, QtGui.QTableWidgetItem(FileLoc))
			self.Layer_List_TABLE.setItem(rowPosition, 1, QtGui.QTableWidgetItem(FileVCP))
			self.Layer_List_TABLE.setItem(rowPosition, 2, QtGui.QTableWidgetItem(FileLegendEnt))
			self.Layer_List_TABLE.removeRow(row)
		
# ---------------------------------------------------------------------------------------------------------------------------------------
	def browse_level1(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Level_Res1_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Level_Res1_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_level2(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Level_Res2_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Level_Res2_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_level3(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Level_Res3_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Level_Res3_Loc_Search_BOX.setText("Problem Saving Settings")
				
	def browse_level4(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Level_Res4_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Level_Res4_Loc_Search_BOX.setText("Problem Saving Settings")
				
# ---------------------------------------------------------------------------------------------------------------------------------------

	def browse_depth1(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Depth_Res1_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Depth_Res1_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_depth2(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Depth_Res2_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Depth_Res2_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_depth3(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Depth_Res3_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Depth_Res3_Loc_Search_BOX.setText("Problem Saving Settings")
				
	def browse_depth4(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Depth_Res4_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Depth_Res4_Loc_Search_BOX.setText("Problem Saving Settings")
				
# ---------------------------------------------------------------------------------------------------------------------------------------

	def browse_velocity1(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Velocity_Res1_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Velocity_Res1_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_velocity2(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Velocity_Res2_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Velocity_Res2_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_velocity3(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Velocity_Res3_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Velocity_Res3_Loc_Search_BOX.setText("Problem Saving Settings")
				
	def browse_velocity4(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Velocity_Res4_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Velocity_Res4_Loc_Search_BOX.setText("Problem Saving Settings")
				
# ---------------------------------------------------------------------------------------------------------------------------------------

	def browse_Z01(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Z0_Res1_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Z0_Res1_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_Z02(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Z0_Res2_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Z0_Res2_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_Z03(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Z0_Res3_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Z0_Res3_Loc_Search_BOX.setText("Problem Saving Settings")
				
	def browse_Z04(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Z0_Res4_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Z0_Res4_Loc_Search_BOX.setText("Problem Saving Settings")
				
# ---------------------------------------------------------------------------------------------------------------------------------------

	def browse_Z11(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Z1_Res1_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Z1_Res1_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_Z12(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Z1_Res2_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Z1_Res2_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_Z13(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Z1_Res3_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Z1_Res3_Loc_Search_BOX.setText("Problem Saving Settings")
				
	def browse_Z14(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Z1_Res4_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Z1_Res4_Loc_Search_BOX.setText("Problem Saving Settings")
				
# ---------------------------------------------------------------------------------------------------------------------------------------

	def browse_HydCat1(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.HydCat_Res1_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.HydCat_Res1_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_HydCat2(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.HydCat_Res2_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.HydCat_Res2_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_HydCat3(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.HydCat_Res3_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.HydCat_Res3_Loc_Search_BOX.setText("Problem Saving Settings")
				
	def browse_HydCat4(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.HydCat_Res4_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.HydCat_Res4_Loc_Search_BOX.setText("Problem Saving Settings")
				
# ---------------------------------------------------------------------------------------------------------------------------------------

	def browse_Risk_Precincts1(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Risk_Precincts_Res1_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Risk_Precincts_Res1_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_Risk_Precincts2(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Risk_Precincts_Res2_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Risk_Precincts_Res2_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_Risk_Precincts3(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Risk_Precincts_Res3_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Risk_Precincts_Res3_Loc_Search_BOX.setText("Problem Saving Settings")
				
	def browse_Risk_Precincts4(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Risk_Precincts_Res4_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Risk_Precincts_Res4_Loc_Search_BOX.setText("Problem Saving Settings")
				
# ---------------------------------------------------------------------------------------------------------------------------------------

	def browse_Level_Impact1(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Level_Impact_Res1_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Level_Impact_Res1_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_Level_Impact2(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Level_Impact_Res2_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Level_Impact_Res2_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_Level_Impact3(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Level_Impact_Res3_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Level_Impact_Res3_Loc_Search_BOX.setText("Problem Saving Settings")
				
	def browse_Level_Impact4(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Level_Impact_Res4_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Level_Impact_Res4_Loc_Search_BOX.setText("Problem Saving Settings")
				
# ---------------------------------------------------------------------------------------------------------------------------------------

	def browse_Velocity_Impact1(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Velocity_Impact_Res1_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Velocity_Impact_Res1_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_Velocity_Impact2(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Velocity_Impact_Res2_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Velocity_Impact_Res2_Loc_Search_BOX.setText("Problem Saving Settings")
	
	def browse_Velocity_Impact3(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Velocity_Impact_Res3_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Velocity_Impact_Res3_Loc_Search_BOX.setText("Problem Saving Settings")
				
	def browse_Velocity_Impact4(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.Velocity_Impact_Res4_Loc_Search_BOX.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.Velocity_Impact_Res4_Loc_Search_BOX.setText("Problem Saving Settings")
				
# ---------------------------------------------------------------------------------------------------------------------------------------

	def run(self):
		Fig_Num = 1

		Event = []
		if  self.Q001_CHECK.is_Checked():
			Event = Event.append(['1 Year ARI', '1yrARI', str(self.Q001_Notation_Box.text())])
		if  self.Q002_CHECK.is_Checked():
			Event = Event.append(['2 Year ARI', '2yrARI', str(self.Q002_Notation_Box.text())])
		if  self.Q005_CHECK.is_Checked():
			Event = Event.append(['20% AEP', '20AEP', str(self.Q005_Notation_Box.text())])
		if self.Q010_CHECK.is_Checked():
			Event = Event.append(['10% AEP', '10AEP', str(self.Q010_Notation_Box.text())])
		if self.Q020_CHECK.is_Checked():
			Event = Event.append(['5% AEP', '5AEP', str(self.Q020_Notation_Box.text())])
		if self.Q050_CHECK.is_Checked():
			Event = Event.append(['2% AEP', '2AEP', str(self.Q050_Notation_Box.text())])
		if self.Q100_CHECK.is_Checked():
			Event = Event.append(['1% AEP', '1AEP', str(self.Q100_Notation_Box.text())])
		if self.Q200_CHECK.is_Checked():
			Event = Event.append(['0.5% AEP', '0.5AEP', str(self.Q200_Notation_Box.text())])
		if self.Q500_CHECK.is_Checked():
			Event = Event.append(['0.2% AEP', '0.2AEP', str(self.Q500_Notation_Box.text())])
		if self.Q1000_CHECK.is_Checked():
			Event = Event.append(['0.1% AEP', '0.1AEP', str(self.Q1000_Notation_Box.text())])
		if self.Q2000_CHECK.is_Checked():
			Event = Event.append(['0.05% AEP', '0.05AEP', str(self.Q2000_Notation_Box.text())])
		if self.QPMF_CHECK.is_Checked():
			Event = Event.append(['Probable Maximum Flood', 'PMF', str(self.QPMF_Notation_Box.text())])

		Result = []
		if  self.Level_CHECK.is_Checked():
			Result = Result.append(['Level', 'Peak Flood Level', str(self.Level_Appendix_Label_BOX.text()),
									self.Level_Res1_Loc_Search_BOX.text, self.Level_Res1_VCP_SELECT.currentText(), self.Level_Res1_Format_SELECT.currentText(),
									self.Level_Res2_Loc_Search_BOX.text, self.Level_Res2_VCP_SELECT.currentText(), self.Level_Res2_Format_SELECT.currentText(),
									self.Level_Res3_Loc_Search_BOX.text, self.Level_Res3_VCP_SELECT.currentText(), self.Level_Res3_Format_SELECT.currentText(),
									self.Level_Res4_Loc_Search_BOX.text, self.Level_Res4_VCP_SELECT.currentText(), self.Level_Res4_Format_SELECT.currentText()])
		if self.Depth_CHECK.is_Checked():
			Result = Result.append(['Depth', 'Peak Flood Depth', str(self.Depth_Appendix_Label_BOX.text()),
								self.Depth_Res1_Loc_Search_BOX.text, self.Depth_Res1_VCP_SELECT.currentText(), self.Depth_Res1_Format_SELECT.currentText(),
								self.Depth_Res2_Loc_Search_BOX.text, self.Depth_Res2_VCP_SELECT.currentText(), self.Depth_Res2_Format_SELECT.currentText(),
								self.Depth_Res3_Loc_Search_BOX.text, self.Depth_Res3_VCP_SELECT.currentText(), self.Depth_Res3_Format_SELECT.currentText(),
								self.Depth_Res4_Loc_Search_BOX.text, self.Depth_Res4_VCP_SELECT.currentText(), self.Depth_Res4_Format_SELECT.currentText()])
		if self.Velocity_CHECK.is_Checked():
			Result = Result.append(['Velocity', 'Peak Flood Velocity', str(self.Velocity_Appendix_Label_BOX.text()),
										self.Velocity_Res1_Loc_Search_BOX.text, self.Velocity_Res1_VCP_SELECT.currentText(), self.Velocity_Res1_Format_SELECT.currentText(),
										self.Velocity_Res2_Loc_Search_BOX.text, self.Velocity_Res2_VCP_SELECT.currentText(), self.Velocity_Res2_Format_SELECT.currentText(),
										self.Velocity_Res3_Loc_Search_BOX.text, self.Velocity_Res3_VCP_SELECT.currentText(), self.Velocity_Res3_Format_SELECT.currentText(),
										self.Velocity_Res4_Loc_Search_BOX.text, self.Velocity_Res4_VCP_SELECT.currentText(), self.Velocity_Res4_Format_SELECT.currentText()])
		if self.Z0_CHECK.is_Checked():
			Result = Result.append(['Z0', 'Velocity Depth Product', str(self.Z0_Appendix_Label_BOX.text()),
									self.Z0_Res1_Loc_Search_BOX.text, self.Z0_Res1_VCP_SELECT.currentText(), self.Z0_Res1_Format_SELECT.currentText(),
									self.Z0_Res2_Loc_Search_BOX.text, self.Z0_Res2_VCP_SELECT.currentText(), self.Z0_Res2_Format_SELECT.currentText(),
									self.Z0_Res3_Loc_Search_BOX.text, self.Z0_Res3_VCP_SELECT.currentText(), self.Z0_Res3_Format_SELECT.currentText(),
									self.Z0_Res4_Loc_Search_BOX.text, self.Z0_Res4_VCP_SELECT.currentText(), self.Z0_Res4_Format_SELECT.currentText()])
		if self.Z1_CHECK.is_Checked():
			Result = Result.append(['Z1', 'Provisional Flood Hazard', str(self.Z1_Appendix_Label_BOX.text()),
									self.Z1_Res1_Loc_Search_BOX.text, self.Z1_Res1_VCP_SELECT.currentText(), self.Z1_Res1_Format_SELECT.currentText(),
									self.Z1_Res2_Loc_Search_BOX.text, self.Z1_Res2_VCP_SELECT.currentText(), self.Z1_Res2_Format_SELECT.currentText(),
									self.Z1_Res3_Loc_Search_BOX.text, self.Z1_Res3_VCP_SELECT.currentText(), self.Z1_Res3_Format_SELECT.currentText(),
									self.Z1_Res4_Loc_Search_BOX.text, self.Z1_Res4_VCP_SELECT.currentText(), self.Z1_Res4_Format_SELECT.currentText()])
		if self.HydCat_CHECK.is_Checked():
			Result = Result.append(['HydCat', 'Hydraulic Categorisation', str(self.HydCat_Appendix_Label_BOX.text()),
									self.HydCat_Res1_Loc_Search_BOX.text, self.HydCat_Res1_VCP_SELECT.currentText(), self.HydCat_Res1_Format_SELECT.currentText(),
									self.HydCat_Res2_Loc_Search_BOX.text, self.HydCat_Res2_VCP_SELECT.currentText(), self.HydCat_Res2_Format_SELECT.currentText(),
									self.HydCat_Res3_Loc_Search_BOX.text, self.HydCat_Res3_VCP_SELECT.currentText(), self.HydCat_Res3_Format_SELECT.currentText(),
									self.HydCat_Res4_Loc_Search_BOX.text, self.HydCat_Res4_VCP_SELECT.currentText(), self.HydCat_Res4_Format_SELECT.currentText()])
		if self.Risk_Precints_CHECK.is_Checked():
			Result = Result.append(['Risk_Precincts', 'Flood Risk Precincts', str(self.Risk_Precincts_Appendix_Label_BOX.text()),
									self.Risk_Precincts_Res1_Loc_Search_BOX.text, self.Risk_Precincts_Res1_VCP_SELECT.currentText(), self.Risk_Precincts_Res1_Format_SELECT.currentText(),
									self.Risk_Precincts_Res2_Loc_Search_BOX.text, self.Risk_Precincts_Res2_VCP_SELECT.currentText(), self.Risk_Precincts_Res2_Format_SELECT.currentText(),
									self.Risk_Precincts_Res3_Loc_Search_BOX.text, self.Risk_Precincts_Res3_VCP_SELECT.currentText(), self.Risk_Precincts_Res3_Format_SELECT.currentText(),
									self.Risk_Precincts_Res4_Loc_Search_BOX.text, self.Risk_Precincts_Res4_VCP_SELECT.currentText(), self.Risk_Precincts_Res4_Format_SELECT.currentText()])
		if self.Level_Impact_CHECK.is_Checked():
			Result = Result.append(['Level_Impact', 'Flood Level Impact', str(self.Level_Impact_Appendix_Label_BOX.text()),
									self.Level_Impact_Res1_Loc_Search_BOX.text, self.Level_Impact_Res1_VCP_SELECT.currentText(), self.Level_Impact_Res1_Format_SELECT.currentText(),
									self.Level_Impact_Res2_Loc_Search_BOX.text, self.Level_Impact_Res2_VCP_SELECT.currentText(), self.Level_Impact_Res2_Format_SELECT.currentText(),
									self.Level_Impact_Res3_Loc_Search_BOX.text, self.Level_Impact_Res3_VCP_SELECT.currentText(), self.Level_Impact_Res3_Format_SELECT.currentText(),
									self.Level_Impact_Res4_Loc_Search_BOX.text, self.Level_Impact_Res4_VCP_SELECT.currentText(), self.Level_Impact_Res4_Format_SELECT.currentText()])
		if self.Velocity_Impact_CHECK.is_Checked():
			Result = Result.append(['Velocity_Impact', 'Flood Velocity Impact', str(self.Velocity_Impact_Appendix_Label_BOX.text()),
									self.Velocity_Impact_Res1_Loc_Search_BOX.text, self.Velocity_Impact_Res1_VCP_SELECT.currentText(), self.Velocity_Impact_Res1_Format_SELECT.currentText(),
									self.Velocity_Impact_Res2_Loc_Search_BOX.text, self.Velocity_Impact_Res2_VCP_SELECT.currentText(), self.Velocity_Impact_Res1_Format_SELECT.currentText(),
									self.Velocity_Impact_Res3_Loc_Search_BOX.text, self.Velocity_Impact_Res3_VCP_SELECT.currentText(), self.Velocity_Impact_Res1_Format_SELECT.currentText(),
									self.Velocity_Impact_Res4_Loc_Search_BOX.text, self.Velocity_Impact_Res4_VCP_SELECT.currentText(), self.Velocity_Impact_Res1_Format_SELECT.currentText()])

		LayerList = []
		for row in self.Layer_List_TABLE.numberRows():
			LayerList.append([self.Layer_List_TABLE.item(row,0), self.Layer_List_TABLE.item(row, 1), self.Layer_List_TABLE.item(row, 2)])

		Scenarios = []
		if not self.Scenario_1_Notation_BOX.text():
			Scenarios.append([self.Scenario_1_Notation_BOX.text(), self.Scenario_1_Title_BOX.text()])
		if not self.Scenario_2_Notation_BOX.text():
			Scenarios.append([self.Scenario_2_Notation_BOX.text(), self.Scenario_2_Title_BOX.text()])
		if not self.Scenario_3_Notation_BOX.text():
			Scenarios.append([self.Scenario_3_Notation_BOX.text(), self.Scenario_3_Title_BOX.text()])
		if not self.Scenario_4_Notation_BOX.text():
			Scenarios.append([self.Scenario_4_Notation_BOX.text(), self.Scenario_4_Title_BOX.text()])

		DefaultTemplate = self.Layout_SELECT.currentText()
		CentroidX = self.Centroid_X_Coord_BOX.Text()
		CentroidY = self.Centroid_Y_Coord_BOX.Text()
		Zoom = self.Zoom_BOX.Text()

		WorkspaceDir = []
		PreviousNote = []
		#Create Dir Storing Figures
		sCounter = 1
		for Res in Result:
			for Eve in Event:
				if not Scenarios:
					for Scen in Scenarios:
						TestRes = 3 in Res
						if TestRes != PreviousNote:
							ResCounter = 1
						if 3 in Res == "":
							Fig_Num = 3 in Res + ResCounter
						else:
							Fig_Num = ResCounter.zfill(3)
						FigureTitle = "Figure" + Fig_Num + "_" + 2 in Eve + "_" + 1 in Scen + "_" + 1 in Res
						FigureLocation = self.Control_Ref_Search_BOX.text()
						CapTop = 2 in Res + " - " + 1 in Eve
						CapBot = 2 in Scen
						MapTemplates = [DefaultTemplate, CentroidX, CentroidY, Zoom]
						if not Scenarios:
							CapBot = 2 in Scen
						if not 4 in Res:
							Res1 = glob.glob(Res(4)*Eve(1)*Scen(1)*Res(6))
							LayerList.append([Res1, 5 in Res])
						if not 6 in Res:
							Res2 = glob.glob(Res(7)*Eve(1)*Scen(1)*Res(9))
							LayerList.append([Res2, 8 in Res])
						if not 8 in Res:
							Res3 = glob.glob(Res(10)*Eve(1)*Scen(1)*Res(12))
							LayerList.append([Res3, 11 in Res])
						if not 10 in Res:
							Res4 = glob.glob(Res(13)*Eve(1)*Scen(1)*Res(15))
							LayerList.append([Res4, 14 in Res])
						WorkspaceDir.append([FigureTitle, FigureLocation, CapTop, CapBot, Fig_Num, LayerList, MapTemplates])
						ResCounter = ResCounter + 1
						PreviousNote = 3 in Res
					else:
						TestRes = 3 in Res
						if TestRes != PreviousNote:
							ResCounter = 1
						if 3 in Res == "":
							Fig_Num = 3 in Res + ResCounter
						else:
							Fig_Num = ResCounter.zfill(3)
						FigureTitle = "Figure" + Fig_Num + "_" + 2 in Eve + "_" + 1 in Res
						FigureLocation = self.Control_Ref_Search_BOX.text()
						CapTop = 2 in Res
						CapBot = 1 in Eve
						if not Scenarios:
							CapBot = 2 in Scen
						if not 4 in Res:
							Res1 = glob.glob(Res(4)*Eve(1)*Res(6))
							LayerList.append([Res1, 5 in Res])
						if not 6 in Res:
							Res2 = glob.glob(Res(7)*Eve(1)*Res(9))
							LayerList.append([Res2, 8 in Res])
						if not 8 in Res:
							Res3 = glob.glob(Res(10)*Eve(1)*Res(12))
							LayerList.append([Res3, 11 in Res])
						if not 10 in Res:
							Res4 = glob.glob(Res(13)*Eve(1)*Res(15))
							LayerList.append([Res4, 14 in Res])
						WorkspaceDir.append([FigureTitle, FigureLocation, CapTop, CapBot, Fig_Num, LayerList])
						ResCounter = ResCounter + 1
						PreviousNote = 3 in Res
		with open("C:\Users\Sam\.qgis2\python\plugins\Test.txt", "wb") as fp:
			pickle.dump(WorkspaceDir, fp)
		#Create Workspaces for all in Dir


			
# ----------------------------------------------------------
#    figure builder
# ----------------------------------------------------------
from ui_Figure_Builder_dialog import *
from tuflowqgis_settings import TF_Settings
class Figure_Builder_dialog(QDialog, Ui_Figure_BuilderDialogBase):
	def __init__(self, iface, project):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		#self.tfsettings = TF_Settings()

		# load stored settings
		#self.last_chk_folder = self.tfsettings.get_last_chk_folder()
		#error, message = self.tfsettings.Load() #exe, tuflow dircetory and projection
		#if error:
		#	QMessageBox.information( self.iface.mainWindow(),"Error", "Error Loading Settings: "+message)

				
		#QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		#if (self.last_chk_folder == "Undefined"):
		#	if self.tfsettings.combined.base_dir:
		#		self.last_chk_folder = os.path.join(self.tfsettings.combined.base_dir,"TUFLOW","Check")
		#		self.emptydir.setText(self.last_chk_folder)
		#	self.emptydir.setText(self.tfsettings.combined.base_dir+"\\TUFLOW\\check")
		#else:
		#	self.emptydir.setText(self.last_chk_folder)
		#self.emptydir.setText = self.tfsettings.get_last_mi_folder()

	def browse_empty_dir(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Directory",self.last_chk_folder)
		if newname != None:
			try:
				self.emptydir.setText(newname)
				self.tfsettings.save_last_chk_folder(newname)
			except:
				self.emptydir.setText("Problem Saving Settings")


	def run(self):
		runID = unicode(self.txtRunID.displayText()).strip()
		basedir = unicode(self.emptydir.displayText()).strip()
		showchecks = self.showchecks.isChecked()


		# run create dir script
		#message = tuflowqgis_import_check_tf(self.iface, basedir, runID, empty_types, points, lines, regions)
		message = tuflowqgis_import_check_tf(self.iface, basedir, runID,showchecks)
		#message = tuflowqgis_create_tf_dir(self.iface, crs, basedir)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Importing TUFLOW Empty File(s)", message)


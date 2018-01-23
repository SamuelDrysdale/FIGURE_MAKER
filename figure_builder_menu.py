# -*- coding: utf-8 -*-
"""
/***************************************************************************
 tuflowqgis_menu
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
build_vers = '0.0.1 (QGIS 2.x)'
build_type = 'developmental' #release / developmental

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import os

# Import the code for the dialog
from master_dialog import *

#par
from figure_builder_library import tuflowqgis_apply_check_tf

class figure_builder_menu:

	def __init__(self, iface):
		self.iface = iface
		self.dockOpened = False

	def initGui(self):
		# Figure Builder
		icon = QIcon(os.path.dirname(__file__) + "/icons/Figure_Builder.png")
		self.run_figure_builder_action = QAction(icon, "Figure Builder", self.iface.mainWindow())
		QObject.connect(self.run_figure_builder_action, SIGNAL("triggered()"), self.run_figure_builder)
		self.iface.addToolBarIcon(self.run_figure_builder_action)
		self.iface.addPluginToMenu("&Figure Builder", self.run_figure_builder_action)
		
		# New Project
		icon = QIcon(os.path.dirname(__file__) + "/icons/New_Project.png")
		self.run_new_project_action = QAction(icon, "New Project", self.iface.mainWindow())
		QObject.connect(self.run_new_project_action, SIGNAL("triggered()"), self.run_new_project)
		self.iface.addToolBarIcon(self.run_new_project_action)
		self.iface.addPluginToMenu("&Figure Builder", self.run_new_project_action)
		
		#Init classes variables
		self.dockOpened = False		#remember for not reopening dock if there's already one opened
		self.resdockOpened = False
		self.selectionmethod = 0						#The selection method defined in option
		self.saveTool = self.iface.mapCanvas().mapTool()			#Save the standard mapttool for restoring it at the end
		self.layerindex = None							#for selection mode
		self.previousLayer = None						#for selection mode
		self.plotlibrary = None							#The plotting library to use

	def unload(self):
		self.iface.removePluginMenu("&Figure Builder", self.about_menu.menuAction())
		self.iface.removePluginMenu("&Figure Builder", self.editing_menu.menuAction())
		self.iface.removePluginMenu("&Figure Builder", self.run_menu.menuAction())
		del self.import_chk_action

	def run_figure_builder(self):
		project = QgsProject.instance()
		dialog = Figure_Builder_dialog(self.iface, project)
		dialog.exec_()

	def run_new_project(self):
		project = QgsProject.instance()
		dialog = New_Project_dialog(self.iface, project)
		dialog.exec_()


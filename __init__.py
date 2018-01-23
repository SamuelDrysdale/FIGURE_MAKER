# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Figure_Builder
                                 A QGIS plugin
 Figure_Builder
                             -------------------
        begin                : 2017-12-20
        copyright            : (C) 2017 by Figure_Builder
        email                : Figure_Builder
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
from figure_builder_menu import figure_builder_menu

def name():
    return "Figure_Builder"


def description():
    return "A tool for creating figures presenting Flood Analysis results."


def version():
    return "Version 0.0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "2.0"

def author():
    return "Samuel Drysdale"

def email():
    return "samuel.e.drysdale@gmail.com"

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Figure_Builder class from file Figure_Builder.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    return figure_builder_menu(iface)

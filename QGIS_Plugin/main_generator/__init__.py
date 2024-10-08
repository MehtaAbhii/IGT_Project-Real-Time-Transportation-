# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Main_Generator
                                 A QGIS plugin
 This plugin is for UI as well as mapping
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-05-06
        copyright            : (C) 2024 by Abhi_Mehta
        email                : abhimehta3845@gmail.com
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
from .Main_Generator import Main_Generator

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Main_Generator class from file Main_Generator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Main_Generator import Main_Generator
    return Main_Generator(iface)

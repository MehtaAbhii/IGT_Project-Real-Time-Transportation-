# # # -*- coding: utf-8 -*-
# # """
# # /***************************************************************************
# #  Main_Generator
# #                                  A QGIS plugin
# #  This plugin is for UI as well as mapping
# #  Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
# #                               -------------------
# #         begin                : 2024-05-06
# #         git sha              : $Format:%H$
# #         copyright            : (C) 2024 by Abhi_Mehta
# #         email                : abhimehta3845@gmail.com
# #  ***************************************************************************/

# # /***************************************************************************
# #  *                                                                         *
# #  *   This program is free software; you can redistribute it and/or modify  *
# #  *   it under the terms of the GNU General Public License as published by  *
# #  *   the Free Software Foundation; either version 2 of the License, or     *
# #  *   (at your option) any later version.                                   *
# #  *                                                                         *
# #  ***************************************************************************/
# # """
# # from qgis.PyQt import QtWidgets, QtGui, QtCore
# # from qgis.core import QgsProject, QgsFeature, QgsGeometry, QgsPointXY, QgsVectorLayer, QgsFields, QgsField, QgsWkbTypes
# # import geopy
# # from geopy.geocoders import Nominatim
# # import requests
# # import csv

# # class TransitRoutingPlugin:
# #     def __init__(self, iface):
# #         self.iface = iface
# #         self.canvas = self.iface.mapCanvas()
# #         self.project_path = "C:\Users\abhim\OneDrive\Downloads\Final_project.qgz"  # Update with your project file path

# #     def initGui(self):
# #         self.action = QtWidgets.QAction("Transit Routing")
# #         self.action.triggered.connect(self.showDialog)
# #         self.iface.addToolBarIcon(self.action)

# #     def unload(self):
# #         self.iface.removeToolBarIcon(self.action)

# #     def showDialog(self):
# #         # Check if the current project matches the specific project
# #         current_project_path = QgsProject.instance().fileName()
# #         if current_project_path == self.project_path:
# #             dialog = TransitRoutingDialog(self.iface)
# #             dialog.exec_()

# # class TransitRoutingDialog(QtWidgets.QDialog):
# #     def __init__(self, iface):
# #         super().__init__()
# #         self.iface = iface
# #         self.setWindowTitle("Transit Routing")
# #         self.setGeometry(100, 100, 400, 300)

# #         # Create UI elements
# #         layout = QtWidgets.QVBoxLayout()
# #         self.setLayout(layout)

# #         self.start_location_label = QtWidgets.QLabel("Start Location:")
# #         self.start_location_edit = QtWidgets.QLineEdit()
# #         self.end_location_label = QtWidgets.QLabel("End Location:")
# #         self.end_location_edit = QtWidgets.QLineEdit()

# #         self.get_routes_button = QtWidgets.QPushButton("Get Transit Routes")
# #         self.get_routes_button.clicked.connect(self.getTransitRoutes)

# #         location_layout = QtWidgets.QGridLayout()
# #         location_layout.addWidget(self.start_location_label, 0, 0)
# #         location_layout.addWidget(self.start_location_edit, 0, 1)
# #         location_layout.addWidget(self.end_location_label, 1, 0)
# #         location_layout.addWidget(self.end_location_edit, 1, 1)

# #         layout.addLayout(location_layout)
# #         layout.addWidget(self.get_routes_button)

# #         self.loadDatasets()

# #     def loadDatasets(self):
# #         self.bus_routes = self.readCSV("path/to/bus_routes.csv")
# #         self.train_routes = self.readCSV("path/to/train_routes.csv")
# #         self.plotRoutes()

# #     def readCSV(self, file_path):
# #         routes = []
# #         with open(file_path, 'r') as file:
# #             reader = csv.DictReader(file)
# #             for row in reader:
# #                 route_id = row['route_id']
# #                 coordinates = [(float(x), float(y)) for x, y in zip(row['lon'].split(','), row['lat'].split(','))]
# #                 routes.append({"route_id": route_id, "coordinates": coordinates})
# #         return routes

# #     def plotRoutes(self):
# #         self.plotBusRoutes()
# #         self.plotTrainRoutes()

# #     def plotBusRoutes(self):
# #         bus_layer = QgsVectorLayer("LineString?crs=epsg:4326", "Bus Routes", "memory")
# #         provider = bus_layer.dataProvider()
# #         fields = QgsFields()
# #         fields.append(QgsField("route_id", QgsField.String))
# #         provider.addAttributes(fields)
# #         bus_layer.updateFields()

# #         for route in self.bus_routes:
# #             route_id = route["route_id"]
# #             coordinates = route["coordinates"]
# #             geometry = QgsGeometry.fromPolylineXY([QgsPointXY(lon, lat) for lon, lat in coordinates])
# #             feature = QgsFeature()
# #             feature.setGeometry(geometry)
# #             feature.setAttributes([route_id])
# #             provider.addFeatures([feature])

# #         QgsProject.instance().addMapLayer(bus_layer)

# #     def plotTrainRoutes(self):
# #         train_layer = QgsVectorLayer("LineString?crs=epsg:4326", "Train Routes", "memory")
# #         provider = train_layer.dataProvider()
# #         fields = QgsFields()
# #         fields.append(QgsField("route_id", QgsField.String))
# #         provider.addAttributes(fields)
# #         train_layer.updateFields()

# #         for route in self.train_routes:
# #             route_id = route["route_id"]
# #             coordinates = route["coordinates"]
# #             geometry = QgsGeometry.fromPolylineXY([QgsPointXY(lon, lat) for lon, lat in coordinates])
# #             feature = QgsFeature()
# #             feature.setGeometry(geometry)
# #             feature.setAttributes([route_id])
# #             provider.addFeatures([feature])

# #         QgsProject.instance().addMapLayer(train_layer)

# #     def getTransitRoutes(self):
# #         start_location = self.start_location_edit.text()
# #         end_location = self.end_location_edit.text()

# #         # Geocode the locations
# #         geolocator = Nominatim(user_agent="my_qgis_plugin")
# #         start_location_coords = geolocator.geocode(start_location)
# #         end_location_coords = geolocator.geocode(end_location)

# #         if start_location_coords and end_location_coords:
# #             # Call Google Maps Transit API for real-time transit routes
# #             transit_routes = self.getTransitRoutesFromAPI(start_location_coords, end_location_coords)

# #             # Display the real-time transit routes on the map
# #             self.displayRoutesOnMap(transit_routes)

# #     def getTransitRoutesFromAPI(self, start_coords, end_coords):
# #         # Call Google Maps Transit API for real-time transit routes
# #         transit_api_url = "https://maps.googleapis.com/maps/api/directions/json"
# #         params = {
# #             "origin": f"{start_coords.latitude},{start_coords.longitude}",
# #             "destination": f"{end_coords.latitude},{end_coords.longitude}",
# #             "mode": "transit",
# #             "departure_time": "now",
# #             "key": "YOUR_API_KEY"
# #         }
# #         response = requests.get(transit_api_url, params=params)
# #         data = response.json()
# #         return data.get("routes", [])

# #     def displayRoutesOnMap(self, transit_routes):
# #         # Create a temporary layer to display the routes
# #         route_layer = QgsVectorLayer("LineString?crs=epsg:4326", "Transit Routes", "memory")
# #         provider = route_layer.dataProvider()
# #         fields = QgsFields()
# #         fields.append(QgsField("route_id", QgsField.String))
# #         provider.addAttributes(fields)
# #         route_layer.updateFields()

# #         # Add the routes to the temporary layer
# #         for i, route in enumerate(transit_routes):
# #             geometry = QgsGeometry.fromPolylineXY([QgsPointXY(point["lng"], point["lat"]) for step in route["legs"][0]["steps"] for point in step["polyline"]["points"]])
# #             feature = QgsFeature()
# #             feature.setGeometry(geometry)
# #             feature.setAttributes([f"Route {i+1}"])
# #             provider.addFeatures([feature])

# #         # Add the temporary layer to the map
# #         QgsProject.instance().addMapLayer(route_layer)

# from qgis.PyQt import QtWidgets, QtGui, QtCore, uic
# from qgis.core import QgsProject, QgsFeature, QgsGeometry, QgsPointXY, QgsVectorLayer, QgsFields, QgsField, QgsWkbTypes
# from geopy.geocoders import Nominatim
# import requests
# import csv

# class TransitRoutingPlugin:
#     def __init__(self, iface):
#         self.iface = iface
#         self.canvas = self.iface.mapCanvas()
#         self.project_path = "C:\\Users\\abhim\\OneDrive\\Downloads\\Final_project.qgz"  # Update with your project file path

#     def initGui(self):
#         self.action = QtWidgets.QAction("Transit Routing", self.iface.mainWindow())
#         self.action.triggered.connect(self.showDialog)
#         self.iface.addToolBarIcon(self.action)

#     def unload(self):
#         self.iface.removeToolBarIcon(self.action)

#     def showDialog(self):
#         # Check if the current project matches the specific project
#         current_project_path = QgsProject.instance().fileName()
#         if current_project_path == self.project_path:
#             dialog = TransitRoutingDialog()
#             dialog.exec_()

# class TransitRoutingDialog(QtWidgets.QDialog):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("C:\\Users\\abhim\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\main_generator\\Main_Generator_dialog_base.ui", self)  # Replace "your_ui_file.ui" with the path to your UI file
#         self.setWindowTitle("Transit Routing")

#         self.get_routes_button.clicked.connect(self.getTransitRoutes)

#         # Initialize empty lists for bus and train routes
#         self.bus_routes = []
#         self.train_routes = []

#         # Load datasets
#         self.loadDatasets()

#     def loadDatasets(self):
#         # Load bus and train routes from CSV files
#         self.bus_routes = self.readCSV("path/to/bus_routes.csv")
#         self.train_routes = self.readCSV("path/to/train_routes.csv")

#         # Geocode start and end locations for all routes
#         for route in self.bus_routes:
#             route['start_coords'] = self.geocodeLocation(route['start_location'])
#             route['end_coords'] = self.geocodeLocation(route['end_location'])

#         for route in self.train_routes:
#             route['start_coords'] = self.geocodeLocation(route['start_location'])
#             route['end_coords'] = self.geocodeLocation(route['end_location'])

#     def readCSV(self, file_path):
#         # Read routes from CSV file
#         routes = []
#         with open(file_path, 'r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 routes.append(row)
#         return routes

#     def geocodeLocation(self, location):
#         # Geocode a location using Nominatim
#         geolocator = Nominatim(user_agent="my_qgis_plugin")
#         location_coords = geolocator.geocode(location)
#         return location_coords
    
#     def getTransitRoutes(self):
#         start_location = self.start_location_edit.text()
#         end_location = self.end_location_edit.text()

#         # Filter bus and train routes based on start and end locations
#         bus_route = self.findRoute(start_location, end_location, self.bus_routes)
#         train_route = self.findRoute(start_location, end_location, self.train_routes)

#         # Plot bus and train routes on the map
#         if bus_route:
#             self.plotRoutes(bus_route, "Bus")
#         if train_route:
#             self.plotRoutes(train_route, "Train")

#     def findRoute(self, start_location, end_location, routes):
#         # Check if a route matches the start and end locations
#         for route in routes:
#             if route['start_location'] == start_location and route['end_location'] == end_location:
#                 return route
#         return None

#     def plotRoutes(self):
#         self.plotBusRoutes()
#         self.plotTrainRoutes()

#     def plotBusRoutes(self):
#         bus_layer = QgsVectorLayer("LineString?crs=epsg:4326", "Bus Routes", "memory")
#         provider = bus_layer.dataProvider()
#         fields = QgsFields()
#         fields.append(QgsField("route_id", QgsField.String))
#         provider.addAttributes(fields)
#         bus_layer.updateFields()

#         for route in self.bus_routes:
#             route_id = route["route_id"]
#             coordinates = route["coordinates"]
#             geometry = QgsGeometry.fromPolylineXY([QgsPointXY(lon, lat) for lon, lat in coordinates])
#             feature = QgsFeature()
#             feature.setGeometry(geometry)
#             feature.setAttributes([route_id])
#             provider.addFeatures([feature])

#         QgsProject.instance().addMapLayer(bus_layer)

#     def plotTrainRoutes(self):
#         train_layer = QgsVectorLayer("LineString?crs=epsg:4326", "Train Routes", "memory")
#         provider = train_layer.dataProvider()
#         fields = QgsFields()
#         fields.append(QgsField("route_id", QgsField.String))
#         provider.addAttributes(fields)
#         train_layer.updateFields()

#         for route in self.train_routes:
#             route_id = route["route_id"]
#             coordinates = route["coordinates"]
#             geometry = QgsGeometry.fromPolylineXY([QgsPointXY(lon, lat) for lon, lat in coordinates])
#             feature = QgsFeature()
#             feature.setGeometry(geometry)
#             feature.setAttributes([route_id])
#             provider.addFeatures([feature])

#         QgsProject.instance().addMapLayer(train_layer)

#     def getTransitRoutes(self):
#         start_location = self.start_location_edit.text()
#         end_location = self.end_location_edit.text()

#         # Geocode the locations
#         geolocator = Nominatim(user_agent="my_qgis_plugin")
#         start_location_coords = geolocator.geocode(start_location)
#         end_location_coords = geolocator.geocode(end_location)

#         if start_location_coords and end_location_coords:
#             # Call Google Maps Transit API for real-time transit routes
#             transit_routes = self.getTransitRoutesFromAPI(start_location_coords, end_location_coords)

#             # Display the real-time transit routes on the map
#             self.displayRoutesOnMap(transit_routes)

#     def getTransitRoutesFromAPI(self, start_coords, end_coords):
#         # Call Google Maps Transit API for real-time transit routes
#         transit_api_url = "https://maps.googleapis.com/maps/api/directions/json"
#         params = {
#             "origin": f"{start_coords.latitude},{start_coords.longitude}",
#             "destination": f"{end_coords.latitude},{end_coords.longitude}",
#             "mode": "transit",
#             "departure_time": "now",
#             "key": "YOUR_API_KEY"
#         }
#         response = requests.get(transit_api_url, params=params)
#         data = response.json()
#         return data.get("routes", [])

#     def displayRoutesOnMap(self, transit_routes):
#         # Create a temporary layer to display the routes
#         route_layer = QgsVectorLayer("LineString?crs=epsg:4326", "Transit Routes", "memory")
#         provider = route_layer.dataProvider()
#         fields = QgsFields()
#         fields.append(QgsField("route_id", QgsField.String))
#         provider.addAttributes(fields)
#         route_layer.updateFields()

#         # Add the routes to the temporary layer
#         for i, route in enumerate(transit_routes):
#             geometry = QgsGeometry.fromPolylineXY([QgsPointXY(point["lng"], point["lat"]) for step in route["legs"][0]["steps"] for point in step["polyline"]["points"]])
#             feature = QgsFeature()
#             feature.setGeometry(geometry)
#             feature.setAttributes([f"Route {i+1}"])
#             provider.addFeatures([feature])

#         # Add the temporary layer to the map
#         QgsProject.instance().addMapLayer(route_layer)

# # Create an instance of the plugin class
# plugin = TransitRoutingPlugin(iface)

# class TransitRoutingPlugin:
#     def __init__(self, iface):
#         self.iface = iface
#         self.canvas = self.iface.mapCanvas()
#         self.project_path = "C:\\Users\\abhim\\OneDrive\\Downloads\\Final_project.qgz"  # Update with your project file path

#     def initGui(self):
#         self.action = QtWidgets.QAction("Transit Routing", self.iface.mainWindow())
#         self.action.triggered.connect(self.showDialog)
#         self.iface.addToolBarIcon(self.action)

#     def unload(self):
#         self.iface.removeToolBarIcon(self.action)

#     def showDialog(self):
#         # Check if the current project matches the specific project
#         current_project_path = QgsProject.instance().fileName()
#         if current_project_path == self.project_path:
#             dialog = TransitRoutingDialog()
#             dialog.exec_()

# class TransitRoutingDialog(QtWidgets.QDialog):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("C:\\Users\\abhim\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\main_generator\\Main_Generator_dialog_base.ui", self)  # Replace "your_ui_file.ui" with the path to your UI file
#         self.setWindowTitle("Transit Routing")

#         self.get_routes_button.clicked.connect(self.getTransitRoutes)

#         # Initialize empty lists for bus and train routes
#         self.bus_routes = []
#         self.train_routes = []

#         # # Load datasets
#         # self.loadDatasets()

#     # def loadDatasets(self):
#     #     # Load bus and train routes from CSV files
#     #     self.bus_routes = self.readCSV("path/to/bus_routes.csv")
#     #     self.train_routes = self.readCSV("path/to/train_routes.csv")

#     #     # Geocode start and end locations for all routes
#     #     for route in self.bus_routes:
#     #         route['start_coords'] = self.geocodeLocation(route['start_location'])
#     #         route['end_coords'] = self.geocodeLocation(route['end_location'])

#     #     for route in self.train_routes:
#     #         route['start_coords'] = self.geocodeLocation(route['start_location'])
#     #         route['end_coords'] = self.geocodeLocation(route['end_location'])

#     # def readCSV(self, file_path):
#     #     # Read routes from CSV file
#     #     routes = []
#     #     with open(file_path, 'r') as file:
#     #         reader = csv.DictReader(file)
#     #         for row in reader:
#     #             routes.append(row)
#     #     return routes

#     def geocodeLocation(self, location):
#         # Geocode a location using Nominatim
#         geolocator = Nominatim(user_agent="my_qgis_plugin")
#         location_coords = geolocator.geocode(location)
#         return location_coords
    
#     def getTransitRoutes(self):
#         start_location = self.start_location_edit.text()
#         end_location = self.end_location_edit.text()

#         # Geocode the locations
#         geolocator = Nominatim(user_agent="my_qgis_plugin")
#         start_location_coords = geolocator.geocode(start_location)
#         end_location_coords = geolocator.geocode(end_location)

#         if start_location_coords and end_location_coords:
#             # Display start and end locations on the map
#             self.displayLocationsOnMap(start_location_coords, end_location_coords)

#             # Draw lines between start and end locations of bus and train routes
#             self.drawRouteLines(start_location_coords, end_location_coords)

#             # Call Google Maps Transit API for real-time transit routes
#             transit_routes = self.getTransitRoutesFromAPI(start_location_coords, end_location_coords)

#             # Display the real-time transit routes on the map
#             self.displayRoutesOnMap(transit_routes)
from qgis.PyQt import QtWidgets, QtGui, QtCore, uic
from qgis.utils import iface
from qgis.core import QgsProject, QgsFeature, QgsGeometry, QgsPointXY, QgsVectorLayer, QgsFields, QgsField, QgsWkbTypes
from geopy.geocoders import Nominatim
import requests

class TransitRoutingPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.project_path = "C:\\Users\\abhim\\OneDrive\\Downloads\\Final_project.qgz"  # Update with your project file path

    def initGui(self, mainWindow):
        self.action = QtWidgets.QAction("Transit Routing", mainWindow)
        self.action.triggered.connect(self.showDialog)
        mainWindow.addToolBarIcon(self.action)

    def unload(self):
        mainWindow = QtWidgets.QApplication.instance().mainWindow()
        mainWindow.removeToolBarIcon(self.action)

    def showDialog(self):
        # Check if the current project matches the specific project
        current_project_path = QgsProject.instance().fileName()
        if current_project_path == self.project_path:
            dialog = TransitRoutingDialog(self.iface)  
            dialog.exec_()
            
class TransitRoutingDialog(QtWidgets.QDialog):
    def __init__(self,iface):
        super().__init__()
        self.iface = iface
         # Store iface in the dialog class

        # Load the UI file
        uic.loadUi("C:\\Users\\abhim\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\main_generator\\Main_Generator_dialog_base.ui", self)  # Replace "your_ui_file.ui" with the path to your UI file
        self.setWindowTitle("Transit Routing")

        # Populate dropdowns with names of points from buses and trains layers
        self.populateDropdowns()

        self.get_routes_button.clicked.connect(self.getTransitRoutes)

    def populateDropdowns(self):
        # Find buses and trains layers in the project
        buses_layer = QgsProject.instance().mapLayersByName("Buses")
        trains_layer = QgsProject.instance().mapLayersByName("Trains")

        # Add names of points from buses layer to the dropdown
        if buses_layer:
            for feature in buses_layer[0].getFeatures():
                name = feature['name']  # Assuming 'name' is the attribute storing the point names
                self.start_location_edit.addItem(name)
                self.end_location_edit.addItem(name)

        # Add names of points from trains layer to the dropdown
        if trains_layer:
            for feature in trains_layer[0].getFeatures():
                name = feature['name']  # Assuming 'name' is the attribute storing the point names
                self.start_location_edit.addItem(name)
                self.end_location_edit.addItem(name)

    def geocodeLocation(self, location):
        # Geocode a location using Nominatim
        geolocator = Nominatim(user_agent="my_qgis_plugin")
        location_coords = geolocator.geocode(location)
        return location_coords
    
    # def geocodeLocation(self, location):
    #     # Geocode a location using Google Maps Geocoding API
    #     result = self.google_maps_client.geocode(location)
    #     if result and len(result) > 0:
    #         # Extract latitude and longitude from the geocoding result
    #         location_coords = result[0]['geometry']['location']
    #         latitude = location_coords['lat']
    #         longitude = location_coords['lng']
    #         return latitude, longitude
    #     else:
    #         return None
    
    def getTransitRoutes(self):
        start_location = self.start_location_edit.currentText()
        end_location = self.end_location_edit.currentText()

        # Geocode the locations
        start_location_coords = self.geocodeLocation(start_location)
        end_location_coords = self.geocodeLocation(end_location)

        if start_location_coords and end_location_coords:
            # Display start and end locations on the map
            self.displayLocationsOnMap(start_location_coords, end_location_coords)

            # Draw lines between start and end locations of bus and train routes
            self.drawRouteLines(start_location_coords, end_location_coords)

            # Call Google Maps Transit API for real-time transit routes
            transit_routes = self.getTransitRoutesFromAPI(start_location_coords, end_location_coords)

            # Display the real-time transit routes on the map
            self.displayRoutesOnMap(transit_routes)

    def drawRouteLines(self, start_coords, end_coords):
        # Draw lines between start and end locations of bus and train routes
        self.drawBusRouteLine(start_coords, end_coords)
        self.drawTrainRouteLine(start_coords, end_coords)

    # def drawBusRouteLine(self, start_coords, end_coords):
    #     bus_route_layer = QgsVectorLayer("LineString?crs=epsg:4326", "Bus Route", "memory")
    #     provider = bus_route_layer.dataProvider()
    #     feature = QgsFeature()
    #     feature.setGeometry(QgsGeometry.fromPolylineXY([QgsPointXY(start_coords.longitude, start_coords.latitude), QgsPointXY(end_coords.longitude, end_coords.latitude)]))
    #     provider.addFeature(feature)
    #     QgsProject.instance().addMapLayer(bus_route_layer)

    # def drawTrainRouteLine(self, start_coords, end_coords):
    #     train_route_layer = QgsVectorLayer("LineString?crs=epsg:4326", "Train Route", "memory")
    #     provider = train_route_layer.dataProvider()
    #     feature = QgsFeature()
    #     feature.setGeometry(QgsGeometry.fromPolylineXY([QgsPointXY(start_coords.longitude, start_coords.latitude), QgsPointXY(end_coords.longitude, end_coords.latitude)]))
    #     provider.addFeature(feature)
    #     QgsProject.instance().addMapLayer(train_route_layer)

    def displayLocationsOnMap(self, start_coords, end_coords):
        # Create a temporary layer to display start and end locations
        location_layer = QgsVectorLayer("Point?crs=epsg:4326", "Locations", "memory")
        provider = location_layer.dataProvider()
        fields = QgsFields()
        fields.append(QgsField("Location", QgsField.String))
        provider.addAttributes(fields)
        location_layer.updateFields()

        # Add start location
        start_feature = QgsFeature()
        start_feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(start_coords.longitude, start_coords.latitude)))
        start_feature.setAttributes(["Start"])
        provider.addFeatures([start_feature])

        # Add end location
        end_feature = QgsFeature()
        end_feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(end_coords.longitude, end_coords.latitude)))
        end_feature.setAttributes(["End"])
        provider.addFeatures([end_feature])

        # Add bus stops and train stations
        self.addBusStopsToLayer(provider)
        self.addTrainStationsToLayer(provider)

        # Add the temporary layer to the map
        QgsProject.instance().addMapLayer(location_layer)

    def addBusStopsToLayer(self, provider):
        # Add bus stops to the temporary layer
        for route in self.bus_routes:
            stop_feature = QgsFeature()
            stop_feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(route['start_coords'].longitude, route['start_coords'].latitude)))
            stop_feature.setAttributes(["Bus Stop"])
            provider.addFeatures([stop_feature])

    def addTrainStationsToLayer(self, provider):
        # Add train stations to the temporary layer
        for route in self.train_routes:
            station_feature = QgsFeature()
            station_feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(route['start_coords'].longitude, route['start_coords'].latitude)))
            station_feature.setAttributes(["Train Station"])
            provider.addFeatures([station_feature])

    def getTransitRoutesFromAPI(self, start_coords, end_coords):
        # Call Google Maps Transit API for real-time transit routes
        transit_api_url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "origin": f"{start_coords.latitude},{start_coords.longitude}",
            "destination": f"{end_coords.latitude},{end_coords.longitude}",
            "mode": "transit",
            "departure_time": "now",
            "key": "YOUR_API_KEY"
        }
        response = requests.get(transit_api_url, params=params)
        data = response.json()
        return data.get("routes", [])

    def displayRoutesOnMap(self, transit_routes):
        # Create a temporary layer to display the routes
        route_layer = QgsVectorLayer("LineString?crs=epsg:4326", "Transit Routes", "memory")
        provider = route_layer.dataProvider()
        fields = QgsFields()
        fields.append(QgsField("route_id", QgsField.String))
        provider.addAttributes(fields)
        route_layer.updateFields()

        # Add the routes to the temporary layer
        for i, route in enumerate(transit_routes):
            geometry = QgsGeometry.fromPolylineXY([QgsPointXY(point["lng"], point["lat"]) for step in route["legs"][0]["steps"] for point in step["polyline"]["points"]])
            feature = QgsFeature()
            feature.setGeometry(geometry)
            feature.setAttributes([f"Route {i+1}"])
            provider.addFeatures([feature])

        # Add the temporary layer to the map
        QgsProject.instance().addMapLayer(route_layer)

# Create an instance of the plugin class
plugin = TransitRoutingPlugin(iface)

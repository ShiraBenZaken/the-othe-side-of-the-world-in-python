from folium import Map, Marker, Popup
from geo import GeoPoint

# Get input values
latitude = 31.78
longitude = 35.04

# Foliom Map
mymap = Map(location = [latitude, longitude])

#create a GeoPoint
geopoint = GeoPoint(latitude = latitude, longitude = longitude)
popup = Popup("Hello from Israel")
popup.add_to(geopoint)
geopoint.add_to(mymap)

# Save the map into a html file
mymap.save("antipode.html")


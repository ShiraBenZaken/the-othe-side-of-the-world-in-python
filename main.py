from folium import Map, Marker, Popup
from geo import GeoPoint

#todo: 1. add the real other point of the correct point.
#      2. the user add the point he wants

# Get input values
locations = [[31.78, 35.04],[41, -1],[36, 17]]

# Foliom Map
mymap = Map(location = [31.78, 35.04])

for lat, lon in locations: 
    # Create a GeoPoint
    geopoint = GeoPoint(latitude = lat, longitude = lon)

    forecast = geopoint.get_weather()
    popup_content = f""" 
    {forecast[0][0][-8:-6]}h: {round(forecast[0][1])}*f <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[1][0][-8:-6]}h: {round(forecast[1][1])}*f <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[2][0][-8:-6]}h: {round(forecast[2][1])}*f <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[3][0][-8:-6]}h: {round(forecast[3][1])}*f <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35>
    """

    popup = Popup(popup_content, max_width=400)
    popup.add_to(geopoint)
    geopoint.add_to(mymap)

# Save the map into a html file
mymap.save("antipode.html")

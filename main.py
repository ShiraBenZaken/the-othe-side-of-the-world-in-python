from folium import Map
from geo import GeoPoint

# Get input values
latitude = 31.78
longitude = 35.04

antipode_latitude = latitude * -1

# Add 180 for negative longitude, Subtract 180 foe positive longitude
if longitude <= 0:
    antipode_longitude = longitude + 180
elif longitude == 0:
    antipode_longitude = 180
else:
    antipode_longitude = longitude - 180

locatoin = [antipode_latitude , antipode_longitude ]
myMap = Map( locatoin )
myMap.save("antipode.html")

myPoint = GeoPoint (20.2,30.3)
cp = myPoint.closest_parallel()

print(antipode_latitude)
print(antipode_longitude)
print(cp)
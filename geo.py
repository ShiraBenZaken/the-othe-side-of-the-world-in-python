from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from folium import Marker
# from random import uniform


class GeoPoint(Marker):
    
    def __init__(self, latitude, longitude, popup = None):
        super().__init__(location = [latitude, longitude], popup = popup)
        self.latitude = latitude
        self.longitude = longitude
    
    def closest_parallel(self):
      return round(self.latitude)
    
    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat = self.latitude, lng = self.longitude )
        if timezone_string is None:
            return None
        time_now = datetime.now(timezone(timezone_string))
        return time_now
    
    def get_weather(self):
        weather = Weather(apikey = '26631f0f41b95fb9f5ac0df9a8f43c92', lat = self.latitude, lon = self.longitude)
        return weather.next_12h_simplified()
    
    # @classmethod
    # def random(cls):
    #    return cls(latitude = uniform(-90, 90), longitude = uniform(-180, 180))
    
    
    
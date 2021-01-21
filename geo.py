

class GeoPoint:
    
   def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
   def closest_parallel(self):
      return round(self.latitude)
    
    
import requests
from pprint import pprint
import matplotlib as plt 


lat = 48.137 #Muc
lon = 11.576

#lat = 52.52 #Berlin
#lon = 13.41

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"

data = requests.get(url).json()
#pprint(data)

class Weather:
    def __init__(self, temperature_2m, time):
        self.temp = temperature_2m
        self.time = time

    def __repr__(self):
        return "Contact: {} {}".format(self.temp, self.time)


    @classmethod
    def from_json(cls, raw_data):
        temp = raw_data["hourly"]["temperature_2m"]
        time = raw_data["time"]
      
        return cls(temp, time)






x_vals = data["hourly"]["time"]
y_vals = data["hourly"]["temperature_2m"]

fig = plt.figure()

ax = fig.add_subplot()

ax.plot(x_vals,y_vals)
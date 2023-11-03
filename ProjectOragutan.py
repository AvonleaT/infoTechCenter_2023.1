print("\n********************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function randomly choosing the weather from a list.
def weather():
    weatherForecast =["Snowing", "Blizzard", "Rain", "Foggy", "Windy", "Icy", "Sunny", "Cloudy", "Thunderstorms"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition


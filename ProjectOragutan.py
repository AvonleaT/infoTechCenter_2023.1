print("\n********************************************\n")

print("Weather Branch")

#Import Libraries Here
import random
from time import sleep

#Create a function randomly choosing the weather from a list.
def weather():
    weatherForecast =["Snowing", "Blizzard", "Rain", "Foggy", "Windy", "Icy", "Sunny", "Cloudy", "Thunderstorms"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

# Variable to call weather() Once in our Vehicle Response System (VRS).
weatherAlert = weather()

# VRS() function will allow my vehicle to respond based on weather conditions.
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNational Weather Service has updated your alarm by 30 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 50 MPH.")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated your alarm by 45 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 30 MPH.")
    elif weatherAlert == "Rain":
        print("\nNational Weather Service has updated your alarm by 10 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 65 MPH.")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service has updated your alarm by 25 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 45 MPH.")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service has updated your alarm by 5 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 75 MPH.")
    elif weatherAlert == "Icy":
        print("\nNational Weather Service has updated your alarm by 60 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 25 MPH.")
    elif weatherAlert == "Sunny":
        print("\nThe weather forcast is calling for a", weatherAlert, "day. Enjoy your drive!")
    elif weatherAlert == "Cloudy":
        print("\nThe weather forcast is calling for a", weatherAlert, "day. Enjoy your drive!")
    else:
        print("\nNational Weather Service has updated your alarm by 25 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 55 MPH.")
vehicleResponseSystem()



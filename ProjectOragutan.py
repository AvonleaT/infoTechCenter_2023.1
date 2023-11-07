

"""
Our Welcome screen will start our program
letting drivers know that the InfoTech Center 2023 is loading.
"""

#Import Libraries Here
import time
import sys
import random
from time import sleep
time_to_sleep = 2

print ("\nWelcome - InfoTech Center 2023\n")
time.sleep(time_to_sleep)

#Add code to have the ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0


while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first, so, message is printed on top of the previous line.
    time.sleep(0.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Loaded - Retina Scanned - Access Granted")

print("\n********************************************\n")
print("Checking Current Gas Levels...\n")
sleep(1)



def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Function with a list of GasStations
def listOfGasStations():
    gasStations = ["Shell","Speedway","Exxon","Meijer","Costco","Marathon","BP","Circle K","Wesco"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#Function will call the gasLevelGauge to determine gas level and then fin a close gas station if low
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1,50), 1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas level is extremely low, checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is",listOfGasStations(), "which is", milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas level is a Quarter Tank, checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is",listOfGasStations(), "which is", milesToGasStationsQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half tank":
        print("Your gas tank is half full. Which is plenty to get to your destinations. - System will warn you if gas becomes low.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas level is three quarters of a tank. You have plenty of gas. - System will warn you if gas becomes low.")
    else:
        print("Your gas tank is full - System will warn you if gas is low.")
    
gasLevelAlert()



print("\n********************************************\n")

print("Checking Current Weather Conditions...")

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




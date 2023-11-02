print("***********************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random
from time import sleep

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












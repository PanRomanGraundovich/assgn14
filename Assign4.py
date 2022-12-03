from Flight import *
from Airport import *

allAirports = {}    # introducing of the main containers...
allFlights = {}


def loadData(airportFile, flightFile):  # loads info from the files, checks if everything is ok
    try:
        global allAirports
        global allFlights
        fileAirport = open(airportFile, "r")
        for line in fileAirport:    # for each line we strip and then add it as an object to the Airports dictionary
            temp = line.split(",")
            temp[0] = temp[0].strip()
            temp[1] = temp[1].strip()
            temp[2] = temp[2].strip()
            allAirports[temp[0]] = Airport(temp[0], temp[2], temp[1])
        fileAirport.close()
        fileFlights = open(flightFile, "r")
        for line in fileFlights:    # doing the same thing but with the flights
            temp = line.split(",")
            tempList = []
            temp[0] = temp[0].strip()
            temp[1] = temp[1].strip()
            temp[2] = temp[2].strip()
            key = temp[1]
            if key in allFlights:   # the idea is to find out if there is already a key in the dictionary of the departure airport of the current flight. If yes, then add to the list of the key. If no, then create a key and a list, then add the flight to it
                tempList = allFlights[temp[1]]
                tempList.append((Flight(temp[0], allAirports[temp[1]], allAirports[temp[2]])))
                allFlights[temp[1]] = tempList
            else:
                tempList.append((Flight(temp[0], allAirports[temp[1]], allAirports[temp[2]])))
                allFlights[temp[1]] = tempList
        fileFlights.close()
    except IOError:  # file exception
        return False
    return True


def getAirportByCode(code):  # gets an airport by the code
    global allAirports
    if code in allAirports.keys():  # checks all the keys of the Airports dictionary and returns the object that is written under the key(code)
        return allAirports[code]
    else:
        return -1


def findAllCityFlights(city):   # finds all the flights by a city
    global allFlights
    temp = []
    for valuesList in allFlights.values():  # checks all the values in the Flights dictionary for the city mentioned in the origin or the destination
        for value in valuesList:
            if (value.getOrigin().getCity() == city) or (value.getDestination().getCity() == city):
                temp.append(value)
    return temp   # returns a list with all the flights by a city


def findAllCountryFlights(country):  # finds all the flights by a country
    global allFlights
    temp = []
    for valuesList in allFlights.values():  # checks all the values in the Flights dictionary for the country mentioned in the origin or the destination
        for value in valuesList:
            if (value.getOrigin().getCountry() == country) or (value.getDestination().getCountry() == country):
                temp.append(value)
    return temp  # returns a list with all the flights by a country


def findFlightBetween(origAirport, destAirport):    # finds a direct flight between two given airports or, if there is no such flight, provides a list of the transfer airports where a single hop is possible for the trip
    global allFlights
    checker = True
    transfers = set()
    while checker:  # checks if there is a direct flight
        for key in allFlights.keys():
            for values in allFlights[key]:
                if (values.getOrigin().getCode() == origAirport.getCode()) and (values.getDestination().getCode() == destAirport.getCode()):
                    return "Direct Flight: {} to {}".format(origAirport.getCode(), destAirport.getCode())
                else:
                    checker = False
    for valueSet in allFlights.values():    # if no, searches for the transfer airports and adds them to a set
        for value in valueSet:
            if value.getOrigin().getCode() == origAirport.getCode():
                for valueSet2 in allFlights.values():
                    for value2 in valueSet2:
                        if (value.getDestination().getCode() == value2.getOrigin().getCode()) and (value2.getDestination().getCode() == destAirport.getCode()):
                            transfers.add(value2.getOrigin().getCode())
    if not transfers:   # if there is a transfer, it returns a set of all possible transfer airports
        return -1
    else:
        return transfers


def findReturnFlight(firstFlight):  # checks if there is a return flight for a flight
    for value in allFlights[firstFlight.getDestination().getCode()]:
        if value.getDestination().getCode() == firstFlight.getOrigin().getCode():
            return value    # if yes, it returns the flight object
    return -1

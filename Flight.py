from Airport import *


class Flight:
    def __init__(self, flightNo, origin, destination):  # the constructor does basic procedures + checks if the given points are Airport class
        if not isinstance(origin, Airport) or not isinstance(destination, Airport): # checks if the disjunction of the isinstances is not True and raises an exception if it is
            raise TypeError("The origin and destination must be Airport objects")
        self._flightNo = flightNo
        self._origin = origin
        self._destination = destination

    def __repr__(self):  # prints out an object in a specific way
        connection = "*none*"
        if self.isDomesticFlight() is True:  # sets a value to the variable depending on the return of isDomesticFlight()
            connection = "domestic"
        else:
            connection = "international"
        return "Flight: {} from {} to {} {{{}}}".format(self._flightNo, self._origin.getCity(), self._destination.getCity(), connection)

    def __eq__(self, other):    # checks if the given object is Flight class and if the called object equals to the given
        if isinstance(other, Flight):
            if (self._origin == other.getOrigin()) and (self._destination == other.getDestination()):
                return True
            else:
                return False
        else:
            return False

    def getFlightNumber(self):  # getters...
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):  # checks if the flight is domestic or international
        if self._origin.getCountry() == self._destination.getCountry():  # compares the get countries from the object
            return True
        else:
            return False

    def setOrigin(self, origin):  # setters...
        self._origin = origin

    def setDestination(self, destination):
        self._destination = destination

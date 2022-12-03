class Airport:
    def __init__(self, code, city, country):  # basic constructor
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):  # printer method: prints out an object in special way
        return "{} ({}, {})".format(self._code, self._city, self._country)

    def getCode(self):  # getters & setters...
        return self._code

    def getCity(self):
        return self._city

    def getCountry(self):
        return self._country

    def setCity(self, city):
        self._city = city

    def setCountry(self, country):
        self._country = country

class City:

    def printcityName(self,name):
        print(f"City name = {name}")
        #print(f"city name from self = {self.cityName}") # ahm.cityName

    def displayCity(self):
        print(f"display city called...")
        self.cityName = "AHMEDABAD"  #Mumbai.cityName = "AHMEDABAD"

ahm = City()
ahm.printcityName("Ahmedabad")  #printCityName(ahm) add 1

mumbai = City()
mumbai.displayCity() #displayCity(mumbai) --> add2


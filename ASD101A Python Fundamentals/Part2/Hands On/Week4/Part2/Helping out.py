class Personal:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_address(self, address):
        self.__address = address
    
    def get_address(self):
        return self.__address
    
    def set_age(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    def get_phone_number(self):
        return self.__phone_number
    
    def printInfo(self):
        print("Name: \t %s \n Address: \t %s \n " % (self.__name, self.__address))
        print("Age: \t %s \n Phone Number: \t %s \n "% (self.__age, self.__phone_number))

myInfo = Personal("Niyah Wilson", "2912 Belknap Way", "28", "858-779-5390")
myMom = Personal("Tamika Wilson", "2455 Brookdale Ave", "53", "858-779-5295")
myDad = Personal("Jeffrey Wilson", "2455 Brookdale Ave", "63", "858-779-9534")

print(myInfo.get_name())
myInfo.printInfo()
myMom.printInfo()
myDad.printInfo()

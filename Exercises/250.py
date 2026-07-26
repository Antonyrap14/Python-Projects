class Reservation:
    def __init__(self,number_of_people:int,name:str,hour:float):
        self.name = name
        self.number_of_people = number_of_people
        self.hour = hour
    
    def moreOfFour(self):
        if self.number_of_people > 4:
            return f"Le persone sono {self.number_of_people}, più di 4"
        else:
            return f"Le persone sono {self.number_of_people}, meno di 4"
    @property
    def hourOfReservations(self):
        return self.hour
    
    def validTime(self):
        if 12.0<=self.hour <=23.0:
            return f"La tua prenotazione è alle {self.hour}"
        else:
            return f"Mi spiace siamo chiusi a quell'ora!"
        
    def changeHour(self,ora):
        if 23 >= ora >= 12:
            self.hour = ora
            return f"Il nuovo orario scelto è {self.hour}"
        else:
            return "Mi spiace per quell'ora siamo chiusi"
    
    def get_info(self):
        return self.name, self.number_of_people, self.hour

antonio = Reservation(4,"Antonio",12.30)
massimo = Reservation(6,"Massimo",15.30)
mimmo = Reservation(2,"Mimmo",11.45)

print(antonio.moreOfFour())
print(massimo.moreOfFour())
print(antonio.validTime())
print(mimmo.validTime())
oretta = massimo.changeHour(23.30)
print(oretta)
print(antonio.get_info())
ora_nuova = antonio.changeHour(22)
print(ora_nuova)
print(antonio.get_info())

        
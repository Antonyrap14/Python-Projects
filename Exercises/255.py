class Veicolo:
    def __init__(self,marca,modello):
        self.marca = marca
        self.modello = modello
    
    def get_info(self):
        return f"Marca:{self.marca}\nModello:{self.modello}"

class Auto(Veicolo):
    def __init__(self, marca, modello,porte):
        super().__init__(marca, modello)
        self.porte = porte
    
    def get_info(self):
        return f"{super().get_info()}\n {self.porte}"

class Camion(Veicolo):
    def __init__(self, marca, modello,capienza):
        super().__init__(marca, modello)
        self.capienza = self.capienza
    
    def get_info(self):
        return f"{super().get_info()}\n{self.capienza}"

a = Veicolo("a1","Yamahh")
print(a.get_info())   

a1 = Auto("Citroen","C4",4)
print(a1.get_info())
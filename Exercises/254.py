class Dipendente:
    def __init__(self,nome,cognome,id:int):
        self.nome = nome
        self.cognome = cognome
        self.id = id

    def visualizza_info(self):
        return f"Nome:{self.nome}\nCognome:{self.cognome}\nId:{self.id}"

class TempoPieno(Dipendente):
    def __init__(self, nome, cognome, id,stipendio_annuale:float):
        super().__init__(nome, cognome, id)
        self.stipendio_annuale = stipendio_annuale
    
    def visualizza_info(self):
        return f"{super().visualizza_info()}\nStipendio annuale:{self.stipendio_annuale}"

class PartTime(Dipendente):
    def __init__(self, nome, cognome, id, paga_oraria:float, ore_settimanali:float):
        super().__init__(nome, cognome, id)
        self.paga_oraria = paga_oraria
        self.ore_settimanali = ore_settimanali
    
    def visualizza_info(self):
        return f"{super().visualizza_info()}\nPaga Oraria:{self.paga_oraria}\nOre Settimanali:{self.ore_settimanali}"

class Consulente(Dipendente):
    def __init__(self, nome, cognome, id, progetto, compenso_totale):
        super().__init__(nome, cognome, id)
        self.compenso_totale = compenso_totale
        self.progetto = progetto
    
    def visualizza_info(self):
        return f"{super().visualizza_info()}\nProgetto:{self.progetto}\nOre Compenso Totale:{self.compenso_totale}"

consulene = Consulente("Andrea","Dibe",1234,"Ai",2000)
print(consulene.visualizza_info())

part = PartTime("Andra","Dixskxskbe",12,8,32)
print(part.visualizza_info())


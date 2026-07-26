 
def stipendio_netto(stipendio_lordo:float,tasse:float,contributi_previdenziali:float) -> float:
    if stipendio_lordo < 0:
        return f"Mi spiace non è possibile"
    
    elif tasse not in range(0,100):
        return "Non è possibile avere le tasse in questo modo"
    
    elif contributi_previdenziali not in range(0,100):
        return "Non è possibile avere le contributi previdenziali in questo modo"
    else:
        stipendio_netto = stipendio_lordo - (stipendio_lordo * tasse / 100) - (stipendio_lordo * contributi_previdenziali / 100)
        return f"Lo stipendio netto è {stipendio_netto}"   

print(stipendio_netto(1000,22,10))
print(stipendio_netto(1000,-22,10))


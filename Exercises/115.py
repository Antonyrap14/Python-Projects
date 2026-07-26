ore_extra = int(input("inserisci un numero di ore: "))

def paga(ore_lavorate):
    salario = 0
    if ore_lavorate >= 40:
        salario = 1000
        return f"Hai ricevuto un bonus di {salario} euro"
    elif 20 <= ore_lavorate < 40:
        salario = 500
        return f"Hai ricevuto un bonus di {salario} euro"
    else:
        return f"NON RICEVERAI BONUS"
    

print(paga(ore_extra))
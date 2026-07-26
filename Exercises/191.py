studenti = {
"Alice": 85,
"Bob": 67,
"Charlie": 90,
"David": 72,  
"Eve": 78
}

studenti_75 = {
    studenti:voto for studenti,voto in studenti.items() if voto >= 75
}

print(f"Gli studenti che hanno preso più di 75 sono:\n{studenti_75} ")
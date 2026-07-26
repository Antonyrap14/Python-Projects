stipendi = {
    "Andrea": 45000,
    "Bianca": 52000,
    "Carlo": 47000,
    "Diana": 80000,
    "Elena": 55000,
}
dizionario = stipendi

new_stipendi = {
    persone :round(dizionario[persone] * 1.10,2)
    for persone in dizionario
    if dizionario[persone] > 50000
   
}

stipendi = {
    "Andrea": 45000,
    "Bianca": 52000,
    "Carlo": 47000,
    "Diana": 80000,
    "Elena": 55000,
}

new_stipendi = {
    persona: round(stipendi[persona] * 1.10, 2) if stipendi[persona] > 50000
    else stipendi[persona]
    for persona in stipendi
}

print(new_stipendi)


print(new_stipendi)
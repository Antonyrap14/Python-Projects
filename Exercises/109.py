vendite = [
    (20, 1), (30, 2), (40, 3), (50, 4),
    (60, 5), (70, 6),(100,7)
]

def mese_migliore(vendite):
    mese_costo_maggiore = 0
    costo_da_battere = 0
    for elemento in vendite:
        costo,mese = elemento
        print(mese)

        if costo > costo_da_battere and mese <= 6:
            mese_costo_maggiore = mese
            costo_da_battere = costo
    return f"il mese è {mese_costo_maggiore} e il costo è {costo_da_battere}"

print(mese_migliore(vendite))
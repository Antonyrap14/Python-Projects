frutta = {
    "fichi":10,
    "mela":20,
    "pera":50,
    "banana":21
}

def regalo(frutta):
    while(True):
        for frutto in frutta:
            frutta[frutto] -= 1
            print(frutta)
        if frutta[frutto] == 0:
            print(f"Abbiamo finito di regalare la frutta perchè il frutto {frutto} è finito")
            break
        

regalo(frutta)






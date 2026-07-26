def paga(saldo):
    if saldo > 5:
        new_saldo = saldo - 5
        return f"puoi giocare, il tuo nuovo saldo è {new_saldo}"
    else:
        new_saldo = saldo
        return f"NON puoi giocare, il tuo saldo è {new_saldo} e una partita costa 5 euro"

saldo = int(input("inserisci saldo:"))
print(paga(saldo))
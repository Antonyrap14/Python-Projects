#INTER
partita = {
    "Milan":{
        "data":"28-08",
        "golTrasferta": 2,
        "golCasa":2
    },
        "Napoli":{
        "data":"28-08",
        "golTrasferta": 3,
        "golCasa":1
    },
        "Juventus":{
        "data":"28-08",
        "golTrasferta": 4,
        "golCasa":3
    },
}

def partita_tranti_gol(partita):
    maxgol = 0
    avversario = ""
    for squadra,dettagli in partita.items():
        if dettagli["golCasa"] > maxgol:
            maxgol = dettagli["golCasa"]
            avversario = squadra
    return avversario


print(partita_tranti_gol(partita))

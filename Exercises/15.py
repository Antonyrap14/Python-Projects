#Sei un assistente di ricerca in un laboratorio di biologia.
#  Hai una lista di campioni che hai annotato nel corso della giornata.
#  Ogni campione viene registrato in una lista Python come un codice univoco.
#  Tu ricevi una comunicazione che alcuni dei campioni sono stati rovinati durante il processo di raccolta
#  e dovranno essere scartati.
#  Si riceve un’altra lista con i codici delle campioni da scartare.
#  Il tuo compito è scrivere un programma in Python che rimuove dalla lista dei campioni i codici che appartengono
#  alla lista dei campioni da scartare.

campioni = [1112,2222,3333,4444]
scartati = [1112,3333]

def tenere(campioni,via):
    lista = []
    for elemento in campioni:
        if elemento in via:
            continue
        else:
            lista.append(elemento)
    return lista

print(tenere(campioni,scartati))


#soluzione libro
def clean_samples(samples, to_be_removed):
    for sample in to_be_removed:
        if sample in samples:
            samples.remove(sample)
    return samples

samples = [
    "sample_1", "sample_2", "sample_5",
    "sample_7", "sample_8", "sample_11",
]
to_be_removed = [
    "sample_2", "sample_7", "sample_11",
]

print(clean_samples(samples, to_be_removed))
                                
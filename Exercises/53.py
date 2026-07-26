#Stai sviluppando un sistema di gestione per una libreria che desidera catalogare i propri libri in modo efficace.
#  Ogni libro ha attributi come titolo, autore, anno di pubblicazione e genere. L’idea è di rappresentare questa struttura 
# con un dizionario annidato, in cui le chiavi principali rappresentano i generi e i valori sono a loro volta dizionari che
#  contengono informazioni sui libri appartenenti a quel genere.

libri = {
    "giallo":{
        "tu!":{
            "autore":"io",
            "anno":2022
        },
        "io!":{
            "autore":"tu",
            "anno":2023
        }
    },
    "horror":{
        "loro":{
            "autore":"noi",
            "anno":2024
        },
        "noi":{
            "autore":"loro",
            "anno":2025
        }
    }
}

libri["science-fiction"]= {"dune":{
    "autore":"bo",
    "anno" :2029,
}
}

print(libri)
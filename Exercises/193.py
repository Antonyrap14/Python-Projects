stipendi = {
    "Andrea": 45000,
    "Bianca": 52000,
    "Carlo": 47000,
    "Diana": 80000,
    "Elena": 55000,
}

def sopra50000(stipendi):
    return {
        dipendenti:stipendio
        for dipendenti,stipendio in stipendi.items() if stipendio > 50000
    }

print(sopra50000(stipendi))
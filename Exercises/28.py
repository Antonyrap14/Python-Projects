# Immagina di lavorare in un magazzino. Hai una lista di pesi di diversi pacchi,
#  rappresentati come numeri decimali, e devi riordinare questa lista in ordine crescente.
#  Come fare ad utilizzare Python per risolvere questo problema?

pacchi = [10,20,33,2,11,44,3,21,9]
print(sorted(pacchi))

def riordina(pacchi):
    pacchi.sort(key=lambda x: x, reverse=True)
    return pacchi

pacchi = [10,20,33,2,11,44,3,21,9]
print(riordina(pacchi))


print(riordina(pacchi))
# Un negozio di e-commerce ha una lista di tutti i prodotti venduti in una giornata.
#  I prodotti sono stati salvati nella lista come stringhe. Il tuo compito è quello di scrivere un programma
#  in Python per contare i prodotti venduti totali e il numero di vendite di ciascun tipo di prodotto.

prodotti_venduti = ["pizza","pasta","pizza","pizza","macchina","caffe","caffe","macchina","sushi"]

def contaProdotti(lista):
    scegli = input("inserisci un prodotto che vuoi cercare nella lista: ")

    count = 0
    for prodotto in lista:
        if prodotto == scegli:
            count += 1

    print(f"Il numero di prodotti {scegli}:{count}")

contaProdotti(prodotti_venduti)

######################################################
sample_data = [
    "televisioni", "cellulari", "cuffie",
    "laptop", "cellulari", "cuffie",
    "televisioni", "televisioni",
    "cellulari", "laptop", "cellulari",
    "cuffie", "televisioni", "cellulari",
    "cuffie", "laptop", "cellulari",
    "laptop", "cellulari", "cuffie",
    "televisioni", "cellulari",
    "caricabatterie",
]

def count_items(sample_data):
    count_dict = {}
    for item in sample_data:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict, len(sample_data)

item_counts, total_sales = count_items(
    sample_data
)

print(f"Numero totale di vendite: {total_sales}")



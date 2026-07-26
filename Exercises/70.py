def prodotti_comuni(lista,lista1):
    return lista & lista1

a = {"pc","cuffie","macchina","pen"}
b = {"macchina","tastiera","mouse","pc"}

print(prodotti_comuni(a,b))
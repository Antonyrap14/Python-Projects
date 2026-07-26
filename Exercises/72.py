clientinewsletter = {"gino","paolo","pino","peppe","andrea","roberto"}
clientiseimesi = {"peppe","pino","andrea"}

def diff(lista,lista1):
    return lista -lista1

print(diff(clientinewsletter,clientiseimesi))
print(diff(clientiseimesi,clientinewsletter))
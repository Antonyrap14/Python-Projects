# IPaddress  datetime  requestmethod  URL  HTTPversion  statuscode  responsesize

log = "192.168.1.1--[10/Oct/2023:13:55:36 +0000] GET /index.html HTTP/1.1 200 1043"

blocco = log.split(" ")
lista = []
#print(blocco)
dizionario = {}

blocco[0] = blocco[0].split("--")
print(blocco[0])
dizionario["IP"] = blocco[0][0]
dizionario["Datetime"] = blocco[0][1].strip("[]") + " " + blocco[1].strip("]") 
dizionario["requestmethon"] = blocco[2]
dizionario["URL"]= blocco[3]
dizionario["HTTP"] = blocco[4]
dizionario["statusCode"] = blocco[5]
dizionario["responsesize"] = blocco[6]
lista.append(dizionario)
for elemento in lista:
    print(f"{elemento}") 
print(lista)
print(" ")


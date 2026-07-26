lista = ["Username:john.doe Date:2023-03-15 AccessType:Login","Username:jane.smith Date:2023-03-15 AccessType:Logout"]

def parse(lista):
    dizionario = {}
    for elemento in lista:
        componente = elemento.split(" ")
        print(componente)
        part = str(componente).split(":")
        dizionario[part[0]] = part[1]
        dizionario[part[2]] = part[3]
   
    print(dizionario)

parse(lista)
print(" ")

def parse_logs(log_string):
    logs = log_string.split("\n")
    log_data = []
    for log in logs:
        if log.strip():
            parts = log.split()
            log_dict = {
                "Username": parts[1],
                "Date": parts[3],
                "AccessType": parts[5],
            }
            log_data.append(log_dict)
    return log_data

# Esempio di utilizzo
log_string = """Username: john.doe Date: 2023-03-15 AccessType: Login
Username: jane.smith Date: 2023-03-15 AccessType: Logout"""

parsed_logs = parse_logs(log_string)
print(parsed_logs)



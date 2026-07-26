lista = ["2023-10-01 10:15:43 INFO User ’alice’ logged in",
"2023-10-01 10:16:07 ERROR Failed to allocate resource",
"2023-10-01 11:01:09 INFO User ’bob’ logged in",
"2023-10-01 11:05:12 INFO User ’alice’ logged out"]

def pullisciStringa(lista):
    for stringa in lista:
      stringa = stringa.split(" ")
      for elemento in stringa:
         print(elemento)
      print(" ")
      

pullisciStringa(lista)


log_lines = [
    "2023-10-01 10:15:43 INFO User ’alice’ logged in",
    "2023-10-01 10:16:07 ERROR Failed to allocate resource",
    "2023-10-01 11:01:09 INFO User ’bob’ logged in",
    "2023-10-01 11:05:12 INFO User ’alice’ logged out",
]

# Lista per memorizzare i record strutturati
logs_data = []

for line in log_lines:
    parts = line.split()
    log_entry = {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "user": parts[4] if parts[3] == "User" else None,
        "action": (
                " ".join(parts[5:])
            if parts[3] == "User"
            else " ".join(parts[3:])
        ),
    }
    logs_data.append(log_entry)

# Stampare i dati strutturati
for log in logs_data:

    print(
        f"Date: {log['date']}, Time: {log['time']}, Level: {log['level']}, User: {log['user']}, Action: {log['action']}"
    )


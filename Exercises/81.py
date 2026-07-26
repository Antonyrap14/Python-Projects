stringa = "12345|login|2023-05-15 10:30:00"
componenti = stringa.split("|")

user = componenti[0]
azione = componenti[1]
timestamp = componenti[2]

print("user:" + user)
print("action:"+ azione)
print("timestamp:" + timestamp)
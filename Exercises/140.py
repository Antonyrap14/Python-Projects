
def search_user(username_list, user_to_search):
    for user in username_list:
        if user == user_to_search:
            print("L’utente", user, "è stato trovato.")
            break
    else:
        print("L’utente non è nella lista.")

# Dati di esempio
username_list = ["Alice", "Bob", "Charlie", "Dave"]
search_user(username_list, "Charlie")


class Verifica(Exception):
    users = {"warlock": "warlock", "menestrello": "mene12", "admin": "admin", "giuse": "gius234"}


try:
    username = input("inserisce username: ")
    password = input("inserisci password: ")
    if username not in Verifica.users:
        raise Verifica("Username non presente nel dizionario.")
    if Verifica.users[username] != password:
        raise Verifica("Password errata.")
    print("Login avvenuto con successo!!")
except Verifica as ex:
    print(f"Errore: {ex}")
except ValueError as ex:
    print(f"Errore:{ex}")
except IndexError as ex:
    print(f"Errore di valore: {ex}")
except KeyError as ex:
    print(f"Errore : {ex}")
except NameError as ex:
    print(f"Errore : {ex}")
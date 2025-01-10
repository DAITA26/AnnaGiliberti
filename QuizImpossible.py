
# Dobbiamo fare 3 o 5 domande: ciascuna con 4 opzioni di risposta.
# Le domande le salviamo in una TUPLA
# Le opzioni le salviamo in un DIZIONARIO
# Per ogni domanda la macchina sceglie a caso una risposta giusta e la salva in una lista
# Per ogni domanda viene richiesto all'utente di scegliere una risposta e che verrà salvata in una lista
# Per ogni domanda facciamo il confronto tra le due risposte comunicando giusto o sbagliato
# Alla fine vogliamo il punteggio

import random

domande = ("Qual è il colore che ho in mente ?",
           "Secondo te che tempo ci sarà domani?",
           "il piatto migliore è?")

risposte = {0: ["arancione", "blu", "cremisi", "denim"],
            1: ['soleggiato', 'nuvoloso', 'piovoso', 'tempestoso'],
            2: ['pizza', 'pasta', 'lasagna', 'risotto']}

listaCPU = []
listaUtente = []
punteggio = 0


def sceltaPC(domanda_index):
    return random.randint(1, 4)


numeroDomanda = 0
for d in domande:
    print(d)
    print(risposte[numeroDomanda])
    numeroDomanda += 1
    sceltaCPU = sceltaPC(d)
    listaCPU.append(sceltaCPU)
    sceltaUtente = int(input(f"La tua risposta è"))
    listaUtente.append (sceltaUtente)
    if sceltaUtente == sceltaCPU:
        print("Hai risposto correttamente!")
        punteggio += 1
    else:
        print(f"Hai risposto in modo errato! La risposta corretta era {sceltaCPU}")

print(f"il tuo punteggio è {punteggio}")

if punteggio>= 2:
    print("Haivinto!")
else:
    print("Hai perso!")





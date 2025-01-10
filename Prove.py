#SCF semplice
import random
# il gioco continua finchè il giocatore vuole giocare
risposta: str= "Y"
while risposta == "Y":

    cpu= random.randint(1,3)
    #Sfrutto tipizzazione dinamica python
    if cpu==1:
     cpu= "sasso"
    else:
     cpu== "carta" if cpu==2 else "forbici"
    #DEGUB
    print(f"la cpu ha scelto {cpu}")
    #chiedo la mossa all'utente senza VALIDAZIONE"
    usr = int(input("""Fai la tua mossa:
                        1-> sasso
                        2-> carta
                        3-> forbici """).strip())
    if usr== 1:
        usr== "sasso"
    elif usr == 2:
        usr== "carta"
    else:
        usr== "forbici"
    print(f"L'utente ha scelto {usr}")
    #Il programma inizia qui!



#Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, 
#aggiungi il valore alla lista di valori già associata alla chiave.

#def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:

""""""

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for i in da_rimuovere:
        while da_rimuovere[i]!=0:
            if i in lista:
                lista.remove(i)
                da_rimuovere[i]=da_rimuovere[i]-1
            else:
                return lista
    return lista


print(rimuovi_elementi([1, 2, 3, 2, 4], {2:2}))


"""Scrivi una funzione che prenda in input una lista di dizionari 
che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario."""

#def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:





#print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))

	

#{'Alice': [90, 85], 'Bob': [75]}


def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    prodotti1={}
    for i in prodotti:
        if prodotti[i] > 20:
            prodotti1[i]=prodotti[i]-(0.1*prodotti[i])
            

    return prodotti1
    
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))

######################################


def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    dizio={}
    for key,value in tuples:
        if key in dizio:
            dizio[key].append(value)
        else:
            dizio[key]=[value]
    return dizio
            
            
            

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))

	

#{'a': [1, 3], 'b': [2]}

"""Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti 
di studenti e aggrega i voti per studente in un nuovo dizionario."""
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    dizio={}
    for studente in voti:
        nome=studente["nome"]
        voto=studente["voto"]
        
        if nome in dizio:
            dizio[nome].append(voto)
        else:
            dizio[nome]=[voto]
    return dizio

        
        
        






print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))

	

#{'Alice': [90, 85], 'Bob': [75]
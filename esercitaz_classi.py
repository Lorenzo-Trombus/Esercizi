#Sistema di Prenotazione Cinema

"""Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(posti_totali): Prenota un certo numero di posti nella sala, se disponibili. 
    Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, posti_totali): Trova il film desiderato e tenta di prenotare posti. 
    Restituisce un messaggio di stato."""


class Film:
    def __init__(self,titolo:str,durata:int):
        self.titolo=titolo
        self.durata=durata


class Sala:
    def __init__(self,id:str,posti_totali:int,posti_prenotati,film_in_programmazione:list[Film]):
        self.id=id
        self.film_in_programmazione=film_in_programmazione
        self.posti_totali=posti_totali
        self.posti_prenotati=posti_prenotati

        
    def prenota_posti(self,num_posti):
        if self.posti_totali - self.posti_prenotati >= num_posti:
            self.posti_prenotati+= num_posti
            return f"i {num_posti} posti sono stati prenotati con successo"
        else:
            return f"ERRORE: i posti disponibili sono inferiori a {num_posti} "

    def posti_disponibili(self):
        self.posti_liberi= self.posti_totali - self.posti_prenotati
        return f"i posti disponibili sono: {self.posti_liberi}"



class Cinema:
    def __init__(self,lista_sale:list[str]=[]):
        self.lista_sale=lista_sale

    def aggiungi_sala(self,sala:Sala):
        self.lista_sale.append(sala)

    def prenota_film(self,titolo_film:str,posti_totali:int):
        pass

film1=Film(titolo="pirati dei caraibi",durata=146)
sala1=Sala(id=12345, posti_totali=100,posti_prenotati=0,film_in_programmazione=film1)
print(sala1.prenota_posti(50))
print(sala1.posti_disponibili())
print(sala1.prenota_posti(51))
print(sala1.prenota_posti(43))
print(sala1.posti_disponibili())


#Gestione di un magazzino
"""
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, 
cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
"""

class Prodotto:
    def __init__(self,nome:str,quantità:str) -> None:
        self.nome=nome
        self.quantità=quantità

dizio_prodotti={} 

class Magazzino:
    def __init__(self) -> None:
        pass

    def aggiungi_prodotto(self,prodotto:Prodotto):
        if prodotto not in dizio_prodotti:
            dizio_prodotti[prodotto]=prodotto.quantità
        else:
            dizio_prodotti[prodotto]+=prodotto.quantità

    def cerca_prodotto(self,nome:str):
        if nome in dizio_prodotti:
            return f"{nome}"
        else:
            return "il prodotto non è nel magazzino"
        
    def verifica_disponibilità(self,nome:str):
        if nome in dizio_prodotti:
            return f"sono presenti {dizio_prodotti[nome]} {nome} nel magazzino"
        else:
            return f"il prodotto {nome}, non è disponibile"
        
prodotto1=Prodotto(nome="aspirapolvere",quantità=3)
#print(dizio_prodotti.aggiungi)


#ESERCITAZIONI CLASSI CON EREDITARIETÀ
"""
Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. 
La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. 
Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio.
"""

class Contatore:
     
    def __init__(self,conteggio:int=0) -> None:
        self.conteggio=conteggio


    def setZero(self):
        self.conteggio=0

    def add1(self):
        self.conteggio+=1

    def sub1(self):
        if self.conteggio >0:
            self.conteggio-=1
        else:
            print(f"Non è possibile eseguire la sottrazione ")
        
    def get(self):
        return self.conteggio
    
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")
    


"""
c = Contatore()  
c.add1() 
c.mostra()

c = Contatore()  
c.sub1()  
c.mostra()
"""
c = Contatore() 
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()  
c.add1()
c.add1()
z  = c.get()
print(z)



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
    def __init__(self,id:str,posti_totali:int,posti_prenotati,film_in_programmazione:list[str]):
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




#Gestione di un magazzino




"""Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, 
o None se il valore non è presente."""


def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    if len(dizionario)==0:
        return None  
    
    for i in dizionario:
        if dizionario[i] == valore:
            return i
            
    if valore not in dizionario:
        return None 
    
"""Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave."""

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    dizio:dict=dict()
    for i in tuples:
        if i[0] not in dizio.keys():
            dizio[i[0]]=[i[1]]
        elif i[0] in dizio.keys():
            dizio[i[0]].append(i[1])
            
            
    return dizio


"""Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
"""


def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA or conditionB and conditionC:
        return "Operazione permessa"
    else:
        return "Operazione negata"
    

"""Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori."""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for i in dict2:
        if i not in dict1:
            dict1[i]=dict2[i]
        elif i in dict1:
            dict1[i]+=dict2[i]
    return dict1
    
"""Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold."""

def sum_above_threshold(numbers: list[int],dato:int ) -> int:
    nums_bigger:list=[]
    for i in numbers:
        if i > dato:
            nums_bigger.append(i)
            
    return sum(nums_bigger)



"""Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51"""

def print_seq(): 
    
    print("Sequenza a):")
    for i in [1, 2, 3, 4, 5, 6, 7]:
        print (f"{i}")
    print()

    print("Sequenza b):")
    for i in [ 3, 8, 13, 18, 23]:
        print (f"{i}")
    print()

    print("Sequenza c):")
    for i in [20, 14, 8, 2, -4, -10]:
        print (f"{i}")
    print()

    print("Sequenza d):")
    for i in [19, 27, 35, 43, 51]:
        print (f"{i}")
    print()
    
    return


"""Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. 
La funzione ritorna "Accesso consentito" oppure "Accesso negato"."""

def check_access(username: str, password: str, is_active: bool) -> str:
    if username=="admin" and password=="12345" and is_active:
        return "Accesso consentito"
    else:
        return "Accesso negato"
    

"""Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista."""

def frequency_dict(elements: list) -> dict:
    dizio:dict=dict()
    for i in elements:
        if i not in dizio.keys():
            dizio[i]=1
        elif i in dizio.keys():
            dizio[i]+=1
            
    return dizio


"""Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1."""

def transform(x: int) -> int:
    if x%2==0:
        x=x/2
        return x
    elif x%2!=0:
        x=(x*3)-1
        return x
    

"""Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i 
prodotti che hanno un prezzo superiore a 20, scontati del 10%."""

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    dizio:dict=dict()
    for i in prodotti:
        if prodotti[i]>20:
            dizio[i]=prodotti[i]*0.9
    return dizio


"""Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica 
i numeri in liste separate per numeri pari e dispari."""

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dizio:dict={"pari": [], "dispari": []}
    for i in lista:
        if i%2==0:
            dizio["pari"].append(i)
        elif i%2!=0:
            dizio["dispari"].append(i)
            
    return dizio



"""Progettare un sistema di videonoleggio con i seguenti requisiti:

1. Classe Movie:

Attributi:

movie_id: str - Identificatore di un film.
title: str - Titolo del film.
director: str - Regista del film.
is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
Metodi:

rent(): Contrassegna il film come noleggiato se non è già noleggiato. 
Se il film non è già noleggiato imposta is_rented a True, 
altrimenti stampa il messaggio "Il film {self.title} è già noleggiato."
return_movie(): Contrassegna il film come restituito. 
Se il film è già noleggiato imposta is_rented a False, altrimenti stampa il messaggio "Il film {self.title} non è attualmente noleggiato."

2. Classe Customer:

Attributi:

customer_id: str - Identificativo del cliente.
name: str - Nome del cliente.
rented_movies: list[Movie] - Lista dei film noleggiati.
Metodi:

rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già stato noleggiato, 
altrimenti stampa il messaggio "Il film {movie.title} è già noleggiato."
return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già presente, 
altrimenti stampa il messaggio "Il film {movie.title} non è stato noleggiato da questo cliente."
3. Classe VideoRentalStore:

Attributi:

movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.
Metodi:

add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel videonoleggio se non è già presente, 
altrimenti stampa il messaggio "Il film con ID {movie_id} esiste già."
register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel videonoleggio se non è già presente, 
altrimenti stampa il messaggio "Il cliente con ID {customer_id} è già registrato."
rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio, 
altrimenti stampa il messaggio "Cliente o film non trovato."
return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un film se entrambi esistono nel videonoleggio, 
altrimenti stampa il messaggio "Cliente o film non trovato."
get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies) 
se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.
For example:"""


class Movie:
    def __init__(self,movie_id:str, title:str, director:str, is_rented: bool=False) -> None:
        self.movie_id=movie_id
        self.title=title
        self.director=director
        self.is_rented=is_rented

    def rent(self):
        if self.is_rented==False:
            self.is_rented=True
        else:
            print (f"Il film {self.title} è già noleggiato")

    def return_movie(self):
        if self.is_rented:
            self.is_rented=False
        else: 
            print(f"il film {self.title} non è attualmente noleggiato")
        
    
class Customer:
    def __init__(self,customer_id:str, name:str, rented_movies:list[Movie]=[]) -> None:
        self.customer_id=customer_id
        self.name=name
        self.rented_movies=rented_movies

    def rent_movie(self, movie:Movie):
        if movie.is_rented == False:
            movie.rent()
            self.rented_movies.append(movie)
        else:
            print(f"Il film {movie.title} è già noleggiato")

    def return_movie(self,movie:Movie):
        if movie not in self.rented_movies:
            print(f"Il film {movie.title} non è stato noleggiato da questo utente")
        elif movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        

class VideoRentalStore:
    def __init__(self, movies:dict[str,Movie]=dict[str,Movie],customers:dict[str,Customer]=dict[str,Customer]) -> None:
        self.movies=movies
        self.customers=customers
    
    def add_movie(self,movie_id:str,director:str,title:str=Movie ):
        if movie_id in self.movies:
            print(f"Il film con ID  {movie_id}: esiste già")
        else :
            self.movies[movie_id]=title

    def register_customer(self,customer_id:str,name:str=Customer):
        if customer_id in self.customers:
            print(f"Il cliente con ID {customer_id} è già registrato")
        else:
            self.customers[customer_id]=name
      
    def rent_movie(self, customer_id:str, movie_id:str):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].rent_movie(movie=self.movies[movie_id])
        else:
            print(f"Cliente o film non trovato")
        
    def return_movie(self,customer_id:str, movie_id:str):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].return_movie(movie=self.movies[movie_id])
        else:
            print(f"Cliente o film non trovato")

    def get_rented_movies(self, customer_id:str):
        if customer_id in self.customers:
           return  self.customers[customer_id].rented_movies
        else:
            print("Cliente non trovato")
            return f"{[]}"



# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")


        






"""In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
 
1. Classe Base: Veicolo
Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
Attributi:
- marca (stringa)
- modello (stringa)
- anno (intero)

Metodi:
- __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
- descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

2. Classe Derivata: Auto
Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:
- numero_porte (intero)

Metodi:
- __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
- descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il - numero di porte nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

3. Classe Derivata: Moto
Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:
- tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

Metodi:
- __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
- descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]"."""


############################



"""Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, 
e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) 
di ricette e i loro ingredienti.
Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.
    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
    Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.
    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - list_recipes(): Elenca tutte le ricette esistenti.
    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. 
    Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
    Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente."""
 

class RecipeManager:
    def __init__(self) -> None:
        self.list_ricette=[]
    
    def create_recipe(self,name:str,ingredients:list[str]):
        if name not in self.list_ricette:



############################


"""Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

Classe Book:

Attributi:
book_id: str - Identificatore di un libro.
title: str - titolo del libro.
author: str - autore del libro
is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
Metodi:
borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
return_book()- Contrassegna il libro come restituito.
Classe Member:

Attributi:
member_id: str - identificativo del membro.
name: str - il nome del membro.
borrowed_books: list[Book] - lista dei libri presi in prestito.
Metodi:
borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
return_book(book): rimuove il libro dalla lista borrowed_books.
Classe Library:

Attributi:
books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
Metodi:
add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro."""


##################


"""Progettare un semplice sistema bancario con i seguenti requisiti:

Classe del Account:
Attributi:
account_id: str - identificatore univoco per l'account.
balance: float - il saldo attuale del conto.
Metodi:
deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
get_balance(): restituisce il saldo corrente del conto.
Classe Bank:
Attributi:
accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
Metodi:
create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
get_balance(account_id): restituisce il saldo del conto con l'ID specificato."""
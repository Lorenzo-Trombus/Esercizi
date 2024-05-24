#Esercizio 2
"""L'esercizio richiede di determinare se una lista collegata (linked list) contiene un ciclo. 
Un ciclo in una lista collegata si verifica quando un nodo nella lista punta a un nodo precedente, creando un percorso circolare. 
In altre parole, se segui i puntatori next dei nodi, finirai per tornare a un nodo che hai già visitato.
Obiettivo dell'esercizio

Scrivere una funzione che, data la testa di una lista collegata, determini se esiste un ciclo nella lista. 
La funzione deve restituire True se c'è un ciclo e False altrimenti."""

class Node:
    pass

class LinkedList:
    pass
        
def has_cycle(head: Node) -> list[int]:
    pass


#Esercizio 1
"""L'esercizio richiede di implementare una pila (stack) utilizzando solo due code (queue). 
Una pila è una struttura dati che segue il principio "Last In, First Out" (LIFO), 
cioè l'ultimo elemento inserito è il primo ad essere rimosso. L'implementazione della pila deve supportare tutte 
le funzioni di una pila normale: push, top, pop e empty.
Classe MyStack

La classe MyStack deve includere i seguenti metodi:

    push(x: int) -> None: Inserisce l'elemento x in cima alla pila.
    pop() -> int: Rimuove e restituisce l'elemento in cima alla pila.
    top() -> int: Restituisce l'elemento in cima alla pila senza rimuoverlo.
    empty() -> bool: Restituisce true se la pila è vuota, false altrimenti.

Dettagli dell'implementazione

Poiché dobbiamo utilizzare solo due code per implementare una pila, dobbiamo sfruttare le operazioni delle code per simulare 
il comportamento LIFO della pila. Le operazioni principali delle code sono l'inserimento (enqueue) alla fine e la rimozione 
(dequeue) dall'inizio."""


class Queue:
    pass


class MyStack:
    pass



#Esercizio 3
"""L'esercizio richiede di determinare se una lista collegata singolarmente (singly linked list) è un palindromo. Una lista collegata è un palindromo se la sequenza di valori dei suoi nodi è la stessa sia letta da sinistra a destra che da destra a sinistra.
Obiettivo dell'esercizio

Scrivere una funzione che, data la testa di una lista collegata, determini se la lista è un palindromo. La funzione deve restituire true se la lista è un palindromo, altrimenti false.
"""

class LinkedList:
    pass
        
def is_palindrome(head: Node) -> list[int]:
    pass

#Esesrcizio 4
"""Given a string s which consists of lowercase or uppercase letters, 
write a function that returns the length of the longest palindrome that can be built with those letters. 
Letters are case sensitive, for example, "Aa" is not considered a palindrome here."""

def longest_palindrome(s: str) -> int:
    from collections import Counter
    
    count = Counter(s)
    len_palin = 0
    
    for char_count in count.values():
        if char_count % 2 == 0:
            len_palin += char_count
        else:
            len_palin += char_count - 1
    
    if len(s)>len_palin:
        len_palin += 1
    
    return len_palin


"""
def longest_palindrome(s: str) -> int:
    list_s=list(s)
    count_len=0
    for i in list_s:
        list_s.remove(i)
        for j in list_s:
            if j==i:
                list_s.remove(j)
                count_len+=2
    if len(s)>count_len:
        count_len+=1
    return count_len

    
print(longest_palindrome("abccccdd"))
"""
    
"""lista_og=list(s)
    list_s=list(s)
    count_pal=0
    for i in list_s:
        list_s.remove(i)
        if i in list_s:
            count_pal+=2
            list_s.remove(i)
            
    if len(lista_og)>=count_pal:
                count_pal+=1
    return count_pal


print(longest_palindrome("abccccdd"))"""



#Esercizio 5

"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine 
if the input string is valid.

An input string is valid if: 

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""
def is_valid_parenthesis(s: str) -> bool:
    lista_s=[]
    dizio_parentesi={")":"(","]":"[","}":"{"}
    for parentesi in s:
        if parentesi in dizio_parentesi.values():
            lista_s.append(parentesi)
        else:
            pass

print(is_valid_parenthesis("(]"))

"""def is_valid_parenthesis(s: str) -> bool:
    lista_s=[]
    dizio_parentesi={"(":")","[":"]","{":"}"}
    if lista_s==True:
        last_el_lista=lista_s[-1]
    else:
        last_el_lista=None
    if len(s)%2==0:
        for parentesi in s:
            if parentesi in dizio_parentesi.keys():
                lista_s.append(parentesi)
            else:
                if not lista_s:
                    return False
                elif parentesi==dizio_parentesi[last_el_lista]:
                    lista_s.pop(-1)
                else:
                    return False
        return not lista_s    
"""         
    
    


    
    


    

#Esercizio lista concatenata
class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse(head: ListNode) -> list[int]:
    reversed_list: list[int] = []
    queue: list[ListNode] = [head]
    
    while queue:
        curr_node = queue.pop()
        if curr_node:
            reversed_list.append(curr_node.val)
            queue.append(curr_node.next)
    return reversed_list[::-1]

def reverse_recursive(head: ListNode) -> list[int]:
    reversed_list: list[int] = []
    _reverse(head, reversed_list)
    return reversed_list[::-1]

def _reverse(curr_node: ListNode, reversed_list: list[int]):
    if curr_node:
        reversed_list.append(curr_node.val)
        _reverse(curr_node.next, reversed_list)
        

head = ListNode(val=0, 
                next=ListNode(val=1, 
                              next=ListNode(val=5, 
                                            next=ListNode(val=6))))
#print(reverse(head))


#Esercizio Sudoku
"""
Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:

Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.

Nota:

Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
Solo le celle riempite devono essere convalidate secondo le regole menzionate.

Esempio: La tavola seguente deve restituire True
"""
def sudoku(tavola: list[list[int]]) -> bool:
    rows: dict[int, list[int]] = {i: [] for i in range(9)}
    # rows = {0: [], 1: [], ... , 8: []}
    cols: dict[int, list[int]] = {i: [] for i in range(9)}
    squares: dict[int, list[int]] = {f'{i}-{j}': [] for i in range(3) for j in range(3)}
    # squares = dict[int, list[int]] = {i: [] for i in range(9)
    for i in range(9):
       for j in range(9):
           curr_elem: str = tavola[i][j]
           if curr_elem != '.':
                square_i, square_j = i // 3, j // 3
                # square_index = 3 * square_i + square_j
                # if curr_elem in rows[i] or curr_elem in cols[j] or curr_elem in squares[square_index]
                if curr_elem in rows[i] or curr_elem in cols[j] or curr_elem in squares[f'{square_i}-{square_j}']:
                    return False
                
                rows[i].append(curr_elem)
                cols[j].append(curr_elem)
                squares[f'{square_i}-{square_j}'].append(curr_elem)
                # squares[square_index].append(curr_elem)
    return True
                
# square_i = 0, square_j = 0 -> 0
# square_i = 0, square_j = 1 -> 1
# square_i = 0, square_j = 2 -> 2
# square_i = 1, square_j = 0 -> 3
# square_i = 1, square_j = 1 -> 4
# square_i = 1, square_j = 2 -> 5
# square_i = 2, square_j = 0 -> 6
# square_i = 2, square_j = 1 -> 7
# square_i = 2, square_j = 2 -> 8 ---> 3 * square_i + square_j
 



#Esercizio rotazione lista 

"""
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni.
 La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione 
 e l'elemento iniziale viene spostato alla fine della lista. 
 Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni 
 sia maggiore della lunghezza della lista.

For example:
Test 	
print(rotate_left([1, 2, 3, 4, 5], 2))

Result


[3, 4, 5, 1, 2]"""


"""def rotate_left(elements: list, k: int) -> list:
    elements1=elements
    while k>len(elements):
        k=k-len(elements)
    for i in elements:
        while i in range(len(k)):
            elements.append(i)
            elements.remove(i)
    
print(rotate_left([1, 2, 3, 4, 5], 2))
"""

#Esercizi di ripasso su Condizionali, Cicli e Funzioni


"""
Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

For example:
Test 	              Result

print(transform(4))     2

	



print(transform(-10))   -5

	

"""

def transform(x: int) -> int:
    if x%2==0:
        x=x/2
    else:
        x=(x*3)-1
    return x
       
print(transform(4))


"""Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. 
L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" 
la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo."""

"""
    Test                            Result    

print(calcola_stipendio(40))        400.0

print(calcola_stipendio(0))         0.0
"""
	
def calcola_stipendio(ore_lavorate: int) -> float:
    pass
    
    
#print(calcola_stipendio(45))
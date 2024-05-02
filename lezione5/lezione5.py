
#dato un intero x restituisce true se è palindromo e false se non lo è

"""
def is_palindrome(x:int) -> bool:

 s:str=str(x)
 i:int= 0
 s_lenght= len(s)
 while i < (s_lenght // 2): #for i in range(len(s))
    j= s_lenght - (i+1)
    if s[i] != s[j]:
        return False
    i+= 1
 return False

is_palindrome(121)"""


"""
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione.
 L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
 La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

"""

"""
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA==True:
        if conditionB==True:
            return"Operazione negata"
        elif conditionC==True:
            return"Operazione negata"
        else:
            return"Operazione permessa"
    else:
        if conditionB==False:
            return"Operazione negata"
        elif conditionC== False:
            return"Operazione negata"
        else:
            return"Operazione permessa"
            

print(check_combination(False,False,False))
"""

"""Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e 
l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in 
cui il numero specificato di posizioni sia maggiore della lunghezza della lista."""
"""
def rotate_left(elements, k: int) -> list:
    while k<=len(elements):
        for i in elements:
            index=elements.index(i)
            if index<k:
                elements.append(i)
                elements.pop(i)
            else:
                return elements

print(rotate_left([1, 2, 3, 4, 5], 2))
"""

#esercizio 4

def is_magic_number(num: int) -> bool:
    numstr=str(num)
    numlist=list(numstr)
    ind=0
    for i in numlist :
        ind+=1
        if i =="7":
            return True
        elif ind not in range(len(numlist)):
            return False
print(is_magic_number(170))


#esercizio 5

def check_access(username: str, password: str, is_active: bool) -> str:
    if (username,password,is_active)==("admin","12345",True):
        return "Accesso consentito"
    else:
        return "Accesso negato"
print(check_access("admin", "54321", True))


#esercizio 9

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    original_lst=list(original_set)
    for i in elements_to_remove:
        if i in original_lst:
            original_lst.remove(i)
    original_set1=set(original_lst)
    return original_set1
print(remove_elements({1, 2, 3, 4}, [2, 3]))
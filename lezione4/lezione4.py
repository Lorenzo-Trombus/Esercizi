
def subtract(x: float,y: float):
    return x-y

print(subtract(10,5))
 
#esempio fatto in classe su max e min di lista di stringhe
"""
listastr: str= ["assagia","le", "mele","piccole"]
print(max(listastr))
print(min(listastr))
"""
# per ordinare una lista di numeri posso usare "sorted"
list=[8,0,-23,10,5.6]
list1= sorted(list)
#print(list1)


def check_value(z: int):    
    if z > 5:
        print("il numero è maggiore di 5")
    elif z==5:
        print("il numero è uguale a 5")
    else:
        print("l numero è minore di 5")
    return z

check_value(10)

#ESERCIZIO 2: 
def check_lenght(a:str):
    if len(a)>10:
        print("la parola ha più di 10 lettere")
    elif len(a)==10:
        print("la parola ha esattamente 10 lettere")
    else:
        print("la parola ha meno di 10 lettere")


check_lenght("parparararara")

#ESERCIZIO 3

def print_numbers(p:list):
    for i in p:
        print(i)
    return i


print_numbers([2,0,37,893,972])

#ESERCIZIO 4
def check_each(b:list):
    for i in b:
        if i>5:
            print("bigger")
        elif i==5:
            print("equal")
        else:
            print("smaller")
    return i

check_each([9,0,7,4,3,54,6])


    




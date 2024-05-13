
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

#Esercizio fatto in classe sui tree(media di ciascun livello)
def visiting_tree_iterative(tree: dict[int, list[int]], root: int):
    stack: list[int] = [root]
    while stack: # while len(stack) != 0
        curr_node = stack.pop(0)
        if curr_node:
            print(curr_node)
            left_child, right_child =\
                tree[curr_node]
            if left_child:
                stack.append(left_child)
            if right_child:
                stack.append(right_child)
    return 

print(visiting_tree_iterative())
"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
"""
 
"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
"""
"""
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.
"""
"""
9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
"""
"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
"""
"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 
"""
"""
9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 
"""
"""
9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.
"""
"""
9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.
"""
"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
"""
"""
9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
"""
"""
9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
"""
"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
"""
"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
"""
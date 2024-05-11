
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
list0=[8,0,-23,10,5.6]
list1= sorted(list0)
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
"""
def print_numbers(p:list):
    for i in p:
        print(i)
    return i


print_numbers([2,0,37,893,972])
"""
#ESERCIZIO 4
"""
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
"""
"""
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning 
about in this chapter. Call the function, and make sure the message displays correctly.
"""
def display_message(mess:str):
    return mess
print(display_message("in this chapter I'm learning about fuctions"))
"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
Call the function, making sure to include a book title as an argument in the function call.
"""
def fav_book(title:str)->str:
     return f"One of my favourite books is {title}"
print(fav_book("Fight Club"))

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed 
on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""
def make_shirt(size:str,text:str)->str:
    return f"la maglietta deve essere della taglia {size} e deve avere scritto:{text}"
print(make_shirt("L","I <3 Pippo Baudo"))
print(make_shirt(text="I <3 Pippo Baudo",size="L"))
 
"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
 Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""
# Guarda 8.3
"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country.
 The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
   Call your function for three different cities, at least one of which is not in the default country.
"""
def descibe_city(name:str,country:str)->str:
    return f"{name} is in {country}"
print(descibe_city("Rome","Italy"))

"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country.
 The function should return a string formatted like this: "Santiago, Chile".
   Call your function with at least three city-country pairs, and print the values that are returned.
"""
def city_country(city:str,country:str):
    return f"{city}, {country}"
print(city_country("rome","italy"))
print(city_country("dublin","ireland"))
print(city_country("london","UK"))

"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
 The function should take in an artist name and an album title, and it should return a dictionary containing 
 these two pieces of information. Use the function to make three dictionaries representing different albums. 
 Print each return value to show that the  dictionaries are storing the album information correctly.
   Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
     If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
       Make at least one new function call that includes the number of songs on an album.
"""

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist
 and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
 Be sure to include a quit value in the while loop.
"""
"""
8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), 
which prints each text message.
"""
shortMess:list[str] = ["ciao","come va?","tutto bene?"]
def show_messages(listaMess):
    for i in listaMess:
        print(i)
show_messages(shortMess)
"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
 Write a function called send_messages() that prints each text message and moves each message to a new list 
 called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages
   were moved correctly.
"""
shortMess:list[str] = ["ciao","come va?","tutto bene?"]
shortMess1=shortMess
def send_messsages(listaMess1):
    sent_mess:list[str]=[]
    for i in listaMess1:
        print(i)
        sent_mess.append(i)
    print(sent_mess)
send_messsages(shortMess1)


    

"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list
 of messages. After calling the function, print both of your lists to show that the original list has retained its messages.
"""
#guarda 8-10
"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandwich that’s being ordered. Call the function three times,
using a different number of arguments each time.
"""
def sandwich(ingredienti:list[str]=list[str]):
    print(f"gli ingredienti del panino sono {ingredienti}")
sandwich("hamburger","pomodori","insalata")

"""
8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other 
key-value pairs that describe you. All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
"""
"""
8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always 
receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 
"""
"""
8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
"""
"""
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""
"""
8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.
"""
#esercizio facoltativo lezione 5
"""
def ransom(note:str,magazine:str)->bool:
    char_count: dict[str,int]={}
    for char in magazine:
        char_count[char]=char_count.get(char,0)+1
    for char in note:
        if char_count.get(char,0)==0:
            return False
        char_count[char]-=1
    
    return True
"""    




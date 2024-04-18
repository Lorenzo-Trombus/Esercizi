# Lorenzo Trombini 18/04/2024

print("hello world")


#Personal Message: Use a variable to represent a person’s name, and print a message to that person.
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
#x= str(input("scrivi il tuo nome:"))
x:str="pippo"
mess: str= f"ciao {x},ti va di imparare python?"
print(mess)  

"""
 Name Cases: Use a variable to represent a person’s name,
 and then print that person’s name in lowercase, uppercase, and title case.
"""

#y= str(input("scrivi il tuo nome:"))
y:str="baudo pippo"
print(f"{y.upper()},{y.lower()}, {y.title()}")

"""
 Find a quote from a famous person you admire. Print the quote and the name of its author. 
 Your output should look something like the following, including the quotation marks: Albert Einstein once said,
 “A person who never made a mistake never tried anything new.”
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person.
 Then compose your message and represent it with a new variable called message. Print your message. 
"""
 
print("ridi e il mondo riderà con te, piangi e piangerai da solo ~Oh Dae-Su")

famous_person: str= "Oh Dae-Su"
message:str= "ridi e il mondo riderà con te, piangi e piangerai da solo"

print(f"{famous_person} una volta disse:{message}")

#File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename.
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.


filename:str="python_notes.txt"
print(filename.removesuffix(".txt"))

#Names: Store the names of a few of your friends in a list called names.
# Print each person’s name by accessing each element in the list, one at a time.
#Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
# The text of each message should be the same, but each message should be personalized with the person’s name.


names: list=["osama","furetto","danila","manuel"]
for i in names[0:5]:
    print(f"{i} te voglio bene")
    


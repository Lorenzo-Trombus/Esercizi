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
for i in names:
    print(f"{i} te voglio bene")


#Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car,
# and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

cars: list=["mercedes","bmw","alfa romeo", "lamborghini"]
for i in cars:
    print(f"mi piacerebbe avere una {i}")

#Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.
"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.

3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""   
listastr: str= ["lecca","le", "palle","lalalalal"]
print(max(listastr))
print(min(listastr))
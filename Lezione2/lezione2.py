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
 
print("")
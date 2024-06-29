

"""An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest 
(possibly) all execution paths! User input is assumed to be a formula that consists of a number, an operator (at least + and -),
 and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), 
 and check whether the resulting list is valid:
 If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). 
Catch any ValueError that occurs, and instead raise a FormulaError.
If the second input is not '+' or '-', again raise a FormulaError.
If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, 
until the user enters quit."""
 
def calculator():
    segno:str=input("inserire l'operatore che si vuole utilizzare, per esempio: -,+,*,/ ")
    lista_operatori=["-","+","*","/"]
    if segno in lista_operatori:
        if segno == "+":
            a=int(input("inserire un numero da sommare "))
            b:int= int(input("inserire il secondo numero da sommare "))
            print( a+b)
        if segno =="-":
            a:int=int(input("inserire il numero a cui sottrarre il secondo numero "))
            b:int=int(input("inserire il numero da sottrarre al primo "))
            print(a-b)
        if segno== "*":
            a:int=int(input("inserire un fattore "))
            b:int=int(input("inserire secondo fattore "))
            print(a*b)
        if segno =="/":
            a:int=int(input("inserire un dividendo "))
            b:int=int(input("inserire un divisore "))
            if b==0:
                print("non puoi dividere per 0  coglione")
            else:
                print(a/b)
    else:
        print("bro devi inserire un operatore, non una scritta a cazzo")

        


calculator()

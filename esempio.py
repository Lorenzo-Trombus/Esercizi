reader=open("files/esempio.txt",encoding="utf-8")


with open("files/esempio.txt") as reader:
    print(reader)
    
try:

    reader.readline()
    print("sono nella try")
    raise Exception("Eccezione")

except Exception:

    print("Sono nella exept")

finally:
    print("sono nella finally")
    reader.close()

class ContextManager:

    def __enter__(self):

        print("ciao sono nell enter")

        return self
    
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type is not None:
            print("Eccezione")
            
            return False
        


with ContextManager() as gm:
    print(gm)
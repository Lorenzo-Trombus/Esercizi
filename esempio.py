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
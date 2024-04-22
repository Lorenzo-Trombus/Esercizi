
#dato un intero x restituisce true se è palindromo e false se non lo è


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

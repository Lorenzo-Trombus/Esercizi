
def lenght_of_last_world(s:str) -> int:
    s1= s.strip()
   # l1:list[str]= s1.split()
    l1=s1.split()
    print(len(l1[-1]))
    
lenght_of_last_world("daje roma dajeee                    ")



# es3
# dato un intero col_number, restituire il suo corrispondente titolo di colonna come ad esempio compare su un foglio excel
"""def convert_to_title(col_number:int) -> str:
    result:str=""
    while col_number > 0:
        resto:int = (col_number - 1)%26
        result=chr(resto+)+result
        col_number= (col_number-1)//26
    return result"""

"""alph=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
convert_to_title(26)"""


#es4
"""data una lista nums di n elementi, restituire l'elemento  che compare più di n/2 volte"""

def majority_element(nums:list[int]) -> int:
    nums:list[int]=[1,2,3,4,2,5,4,2,7,2,2,2,2,2,2,2,2]
    #nums1:list[int] = nums
    d: dict[int,int]={}
    for i in nums:
        d[i]= nums.count(i)

    lenght = len(nums)
    for key in d:
        d[key] /= lenght
        if d[key]>0.5:
            return key
    return None


        
        

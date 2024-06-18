def mergesort(input_list:list)->list:
    """
    
    """

    if len(input_list)==1:
        
        return input_list

    mid_point:int=len(input_list)//2

    list_1=mergesort(input_list=input_list[0:mid_point]) 
    list_2=mergesort(input_list=input_list[mid_point:-1])

    return  merge(list_1,list_2)

def merge(list_1:list[int], list_2:list[int])->list[int]:
    """
    
    """
    i,j=0,0,0     

    result:list[int]=[None for _ in range(len(list_1+list_2))]

    for k in range(len(result)):

        if list_1[i]>list_2[j]:

            result[k]=list_2[j]

            j+=1

        else:

            result[k]=list_1[i]

            i+=1


if __name__ == "__main__":


    input_list:list[int]=[0,1,2,3,4,5,6,7]

    mergesort(input_list=input_list)
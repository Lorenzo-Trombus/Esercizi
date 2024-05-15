#algoritmi ordinamento lista 
def bubble_sort(x:list[float]):
    for i in range(len(x)):
        for j in range(len(x)- i - 1):
            if x[j]>x[j+1]:
                temp:float=x[j+1]
                swap=True
                x[j+1]=x[j]
                x[j]=temp
            if not swap:
                break

a=[1,3,6,4,8]

"""data una lista di numeri interi ("nums"), spostare gli zeri alla fine di questa 
lista mantenendo l'ordine originale dei numeri"""

nums=[2,1,0,8,0,8,90,0,6,0,7,5,0]
def move_zeroes(nums:list[int]):
    for i in nums:
        if i == 0:
            nums.pop(i)
            nums.append(i)
        else:
            continue
    return nums

"""for i in range(len(nums)):
        if nums[i]==0:
        x=nums:pop(i)
        nums.append(x)
"""
nums1=[1,2,1,2,3,4,5,6,2]
nums2=[3,6,7,8,9,1,3,4]
def intersection(nums1: list[int], nums2) -> list[int]:
    nums1: set[int]= set(nums1)
    nums2: set[int]= set(nums2)
    elementi_in_comune: list[int]=[]
    for num in nums1:
        if num in nums2 and num not in elementi_in_comune:
            elementi_in_comune.append(num)
        return elementi_in_comune

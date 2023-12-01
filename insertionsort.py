# def insertionsort(arr):

#     for i in range(len(arr)):
#         key = arr[i]

#         j = i - 1
#         while j>=0 and key < arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1] =  key

# arr = [5,64,6,7,68,68,685,-54,-5454]
# insertionsort(arr)
# print("The sorterd array is :--",arr)

# def bubblesort(arr):

#     swapped = True
#     length = len(arr)
#     for i in range(length):
#         for j in range(0,length-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j+1],arr[j]=arr[j],arr[j+1]
#                 swapped = True
#         if swapped == False:
#             break
# arr = [3,35,5,6,5,775,-565,65,4,-34]
# bubblesort(arr)
# print("The sorted result after the sroting is :--",arr)
nums = [1,2,3,4,5,6,6,7,8,9,10]
prime_no = [x for x in range(2,len(nums)) if all(x % i !=0 for i in range(2,int(x**0.5)+1))]
print(prime_no)
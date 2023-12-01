def bubblesort(arr):


    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(0,length-1-i):

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break
arr = [565,65,46,6464,6,56,57,52]
bubblesort(arr)
print("The sorted list or the array is:--",arr)

def insertionsort(arr):

    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
insertionsort(arr)
print("The result after the sort is :---",arr)

def selectionsort(arr):


    for i in range(len(arr)):

        min_index = i

        for j in range(i+1,len(arr)):

            if arr[min_index] < arr[j]:
                min_index = j
        arr[min_index],arr[j] = arr[j],arr[min_index]
selectionsort(arr)
print("The sorted array after is :--",arr)

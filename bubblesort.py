def bubblesort(arr):

    length = len(arr)
    for i in range(length):
        swapped = False

        for j in range(0,length-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break

arr = [4,5,6,7,7,8,896,5,56,5]

bubblesort(arr)

print("The sorted array is the--",arr)
                
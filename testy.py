def selectionsort(arr):

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index],arr[i]= arr[i],arr[min_index]

arr = int(input("Enter the elements one by one:--"))

for j in range(0,5):
    arr.append(arr)

selectionsort(arr)
print('the sortes list :---',arr)
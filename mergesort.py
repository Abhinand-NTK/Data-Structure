def mergesort(arr):

    if len(arr)>1:

        mid = len(arr)//2

        R = arr[mid:]
        L = arr[:mid]

        mergesort(L)
        mergesort(R)

        i=j=k=0 

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
        
arr = [3,5,6,4,7,75,38,86,3,757,75,75,754] 
mergesort   (arr)
print(arr)
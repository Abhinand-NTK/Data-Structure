    pi = partition(arr,low,heigh)
            
            quicksort(arr,low,pi-1)
            quicksort(arr,pi+1,heigh)

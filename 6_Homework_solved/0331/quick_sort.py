def quicksort(x):

    def sort(start, end):
        if start >= end:
            return

        pivot = x[(start+end)//2]
        
        low, high = start, end
        while low <= high:
            while x[low] < pivot:
                low += 1
            while x[high] > pivot:
                high -= 1
            if low <= high:
                x[low], x[high] = x[high], x[low]
                low += 1
                high -= 1
        
        mid = low

        sort(start, mid-1)
        sort(mid, end)

    sort(0, len(x)-1)
    return x

arr = [15,6,10,22,33,45]
print(quicksort(arr))
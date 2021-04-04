def quick_sort(x):

    def sort(start, end):
        if start >= end:
            return

        pivot = x[start]

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

print(quick_sort([2,312,412,123,12,21,12,2,1,2]))
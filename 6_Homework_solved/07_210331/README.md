# Homework #7

## Quick Sort 구현

#### 1. 공간복잡도 O(1) 일 경우

in place로 구현하기

```python
def quick_sort(x):

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
```

#### 2. 공간복잡도 O(1) 일 경우

1번과 같은데 partition과 sort 함수로 나누었다.

```python
def quick_sort(x):

    def partition(low, high):
        pivot = x[(low+high)//2]

        while low <= high:
            while x[low] < pivot:
                low += 1
            while x[high] > pivot:
                high -= 1
            if low <= high:
                x[low], x[high] = x[high], x[low]
                low, high = low + 1, high - 1
        return low

    def sort(low, high):
        if low >= high:
            return

        mid = partition(low, high)

        sort(low, mid-1)
        sort(mid, high)

    sort(0, len(x)-1)
    return x
```

#### 3. 공간복잡도 O(N) 일 경우

```python
def quick_sort(x):
    if len(x) < 2:
        return x

    left = []
    right = []
    pivot = x[len(x) // 2]

    for idx, el in enumerate(x):
        if idx == (len(x) // 2):
            continue
        if el < pivot:
            left.append(el)
        else:
            right.append(el)

    return quick_sort(left) + [pivot] + quick_sort(right)
```

#### 4. 공간복잡도 O(N) 일 경우 풀이

3번에서는 pivot 으로 지정한 index값만 제외 후에 left, right 를 분리했는데
4번에서는 pivot 과 같은 값을 가지는 경우를 모두 equal로 제외한다.
중복값이 많을 경우, 다음번에 비교해야할 값이 더 적어진다는 장점이 있을 것 같다.

```python
def quick_sort(x):
    if len(x) <= 1:
        return x

    left, equal, right = [], [], []
    pivot = x[len(x) // 2]

    for el in x:
        if el < pivot:
            left.append(el)
        elif el == pivot:
            equal.append(el)
        else:
            right.append(el)

    return quick_sort(left) + equal + quick_sort(right)
```

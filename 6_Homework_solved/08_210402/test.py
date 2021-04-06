def search(x,target):
    def binary_search(left, right):
        if left <= right:
            mid = (left + right) // 2

            if x[mid] < target:
                return binary_search(mid+1, right)
            elif x[mid] > target:
                return binary_search(left, mid-1)
            else:
                return mid
        else:
            return False
    return binary_search(0, len(x)-1)

print(search([1,2,3,4,5],3))
print(search([1,1,2,3,4,5],1))
print(search([1,1,2,3,4,5],7))

def hash_func(s):
    if ord(s) > 90:
        hash_value = ord(s) - 71
    else:
        hash_value = ord(s) - 65
    return hash_value
j = 0
for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
    j += 1
    print(hash_func(i), end=' ')
# print(j)
# hash_func('a')
# hash_func('A')
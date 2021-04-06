def solution(n):
    a, b = 1, 2
    if n == 1:
        return a
    if n == 2:
        return b

    for _ in range(3, n+1):
        a, b = b, a+b
    
    return b % 1000000007

print(solution(4)) # 5
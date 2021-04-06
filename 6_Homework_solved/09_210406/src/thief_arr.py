def solution(money):
    N = len(money)

    dp1 = [0]*N # 첫번째 집을 훔칠 경우, 마지막 집은 훔칠수 없음
    dp1[0] = money[0]
    dp1[1] = money[0]

    dp2 = [0]*N # 두번째 집을 훔칠 경우, 마지막 집까지 훔칠 수 있음
    dp2[1] = money[1]
    
    for i in range(2, N-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
        
    dp1[N-1] = dp1[N-2] # 마지막 집 제외 
    dp2[N-1] = max(dp2[N-2], dp2[N-3] + money[N-1]) # 마지막 집 훔쳤을 경우와 비교
    
    return max(dp1[N-1], dp2[N-1])

print(solution([1,2,3,1])) # 4
def solution(money):
    N = len(money)

    dp1_a, dp1_b = money[0], money[0] # case1) 첫번째 집 훔쳤을 경우 > 마지막 집 전까지 최댓값 확인
    dp2_a, dp2_b = 0, money[1] # case2) 두번째 집 훔쳤을 경우
    
    for i in range(2, N-1):
        dp1_a, dp1_b = dp1_b, max(dp1_b, dp1_a + money[i])
        dp2_a, dp2_b = dp2_b, max(dp2_b, dp2_a + money[i])

    dp2_b = max(dp2_b, dp2_a + money[N-1]) # 마지막 집 훔쳤을 경우와 비교
    
    return max(dp1_b, dp2_b)

print(solution([1,2,3,1])) # 4

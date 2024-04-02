def factorial(n):
    #기본 조건 0!=1
    if n==1:
        return 1
    # n이 0보다 큰 경우,n*(n-1)!을 계산
    else:
        return n * factorial(n-1)
print(factorial(5))
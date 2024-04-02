def factorial(n):                  #반복 구조로 구현한 Factorial 함수
    result = 1
    for k in range(n,0,-1):         #k:n,n-1,... 2, 1
        result = result * k         #기본 연산
    return result
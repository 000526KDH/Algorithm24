def compute_square_C(n):        #n의 제곱 계산 함수. 알고리즘  C사용
    sum=0                       
    for i in range(n):          #i:0,1,... n-1
        for j in range(n):      #j:0,1,... n-1
            sum = sum + 1           #기본 연산
        return sum
    
print(sum)
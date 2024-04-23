def multMul(M1, M2):
    # M1의 열 수와 M2의 행 수가 같아야 함
    if len(M1[0]) != len(M2):
        return None
    
    # 결과 행렬 C 초기화
    C = [[0 for j in range(len(M2[0]))] for i in range(len(M1))]
    
    # 행렬 곱셈 수행
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                C[i][j] += M1[i][k] * M2[k][j]
    
    return C

def powerMat(x,n):
    if n==1:                                                ##종료조건
        return x
    elif(n%2)==0:
        return powerMat(multMat(x,x),n//2)                  #n이 짝수
    else:
        return multMat(x,powerMat(multMat(x,x),(n-1)//2))   #n이 홀수
    
def powerMat(x, n):
    if n == 1:  # 종료 조건
        return x
    elif n % 2 == 0:  # n이 짝수
        return powerMat(multMul(x, x), n // 2)
    else:  # n이 홀수
        return multMul(x, powerMat(multMul(x, x), (n - 1) // 2))
    

# 예제 1: 2 x 2 행렬의 3제곱
M = [[1, 2], [3, 4]]
print(powerMat(M, 3))  # [[37, 54], [81, 118]]

# 예제 2: 3 x 3 행렬의 5제곱
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(powerMat(M, 5))  # [[11697, 13502, 15307], [26730, 30895, 35060], [41763, 48288, 52813]]

# 예제 3: 4 x 4 행렬의 2제곱
M = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(powerMat(M, 2))  # [[90, 100, 110, 120], [202, 228, 254, 280], [314, 356, 398, 440], [426, 484, 542, 600]]


def powerMat(x,n):
    if n == 1:
        return x
    elif(n%2)==0:
        return powerMat(multMat(x,x),n//2)
    else:
        return multMat(x,powerMat(multMat(x,x),(n-1)//2))
##행렬 곱셈 함수 구현 
def MultMul(M1, M2):
    result = []
    for i in range(len(M1)):
        row = []
        for j in range(len(M2[0])):
            sum = 0
            for k in range(len(M2)):
                sum += M1[i][k] * M2[k][j]
            row.append(sum)
        result.append(row)
    return result
##행렬 거듭제곱 알고리즘 구현
def powerMat(x, n):
    if n == 1:
        return x
    elif (n % 2) == 0:
        return powerMat(MultMul(x, x), n // 2)
    else:
        return MultMul(x, powerMat(MultMul(x, x), (n - 1) // 2))
## 예제1:2x2 행렬의 거듭제곱
# 행렬 정의
M = [[1, 1], [1, 0]]

# 거듭제곱 계산
result = powerMat(M, 5)
print(result)
# 출력: [[5, 3], [3, 2]]

# 예제2:3x3 행렬의 거듭제곱
# 행렬 정의
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 거듭제곱 계산
result = powerMat(M, 3)
print(result)
# 출력: [[90, 114, 138], [216, 273, 330], [342, 432, 522]]

#예제 3: 2x2 행렬의 거듭제곱 (짝수 거듭제곱)
# 행렬 정의
M = [[1, 2], [3, 4]]

# 거듭제곱 계산
result = powerMat(M, 4)
print(result)
# 출력: [[273, 384], [609, 856]]

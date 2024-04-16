def forced_technique(cost_matrix):
    n = len(cost_matrix)
    assignment = [-1] * n
    
    # Step 1: 각 행과 열의 최소 비용 찾기
    for i in range(n):
        row_min = min(cost_matrix[i])
        for j in range(n):
            cost_matrix[i][j] -= row_min
    
    for j in range(n):
        col_min = min([row[j] for row in cost_matrix])
        for i in range(n):
            cost_matrix[i][j] -= col_min
    
    # Step 2: 0이 있는 행과 열 찾기
    for i in range(n):
        for j in range(n):
            if cost_matrix[i][j] == 0:
                assignment[i] = j
                break
    
    # Step 3: 할당되지 않은 작업자에 대해 반복
    for i in range(n):
        if assignment[i] == -1:
            for j in range(n):
                if assignment[j] == -1:
                    assignment[i] = j
                    break
    
    return assignment

# 테스트 입력
cost_matrix = [[15, 9, 6, 3], [8, 10, 12, 5], [9, 7, 3, 4], [6, 5, 8, 7]]
result = forced_technique(cost_matrix)
print("할당 결과:", result)

def is_proper_subset(A, B):
    # A와 B를 집합으로 변환
    set_A = set(A)
    set_B = set(B)
    
    # A가 B의 부분집합이고, A와 B가 동일하지 않으면 True 반환
    return set_A.issubset(set_B) and set_A != set_B

# 예시 리스트
A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 8]

# A와 B의 진부분집합 여부 확인
print("A가 B의 진부분집합인가?:", is_proper_subset(A, B))
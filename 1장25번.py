def union_set(A, B):
   
    #A와 B의 합집합을 반환하는 함수
   
    return list(set(A) | set(B))

def intersection_set(A, B):
#A와 B의 교집합을 반환하는 함수
   
    
   
    return list(set(A) & set(B))

def difference_set(A, B): 

#A와 B의 차집합을 반환하는 함수 (A - B)
    
    return list(set(A) - set(B))

# 예시 리스트

A =[1, 2, 3, 4, 5]

B =[4, 5, 6, 7, 8]

print("A와 B의 합집합:", union_set(A, B))
print("A와 B의 교집합:", intersection_set(A, B))
print("A와 B의 차집합:", difference_set(A, B))

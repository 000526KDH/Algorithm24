def is_proper_subset(A,B):
    if set(A)==set(B):
        return False
    return set(A).issubset(set(B))

A=[1,2,3]
B=[1,2,3,4,5]
is_proper = is_proper_subset(A,B)

if is_proper:
    print("A는 B의 진부분집합입니다.")
else:
    print("A는 B의 진부분집합이 아닙니다.")
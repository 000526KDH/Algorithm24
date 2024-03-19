def set_operations(A,B):
    union = list(set(A)|set(B))
    intersection = list(set(A)& set(B))
    difference = list(set(A)-set(B))
    return union, intersection,difference

A =[1,2,3,4]
B=[3,4,5,6]
result_union,result_intersection,result_difference = set_operations(A,B)

print("합집합:",result_union)
print("교집합:",result_intersection)
print("차집합:",result_difference)
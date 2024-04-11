def sequential_search(A,key):
    for i in range(len(A)):
        if A[i]==key:
            return i
        return -1
    printStep(A,i+1)

def printStep(arr,val):
    print(" Step%2d= "%val,end='')
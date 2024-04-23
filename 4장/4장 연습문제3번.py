def insertion_sort(A):
    n = len(A)            #입력의 크기
    for i in range(1, n):              #외부 루프1,2 ..n-1
        key = A[i]                     #A[i]를 key에 저장
        j = i - 1  # 항목 A[i-1]부터 검사
        while j >= 0 and A[j] > key:         #내부 루프
            A[j + 1] = A[j]  # 항목들을 오른쪽으로 한칸씩 이동
            j = j - 1             #위치를 왼쪽으로 이동
        A[j + 1] = key           # 항목 A[i]를 제 위치에 삽입
        printStep(A, i)

def printStep(A, step):
    print(f"Step {step}: {A}")

data = [7,4,9,6,3,8,7,5]
print("Original : ", data)
insertion_sort(data)
print("Insertion: ", data)
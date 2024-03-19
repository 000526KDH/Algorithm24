import collections
                        #큐는 한쪽방향으로만 나갈수있음
Q = collections.deque() #덱은 앞뒤로 넣거나 뺼수있음
Q.append(0)
Q.append(1)

print("F(0)= 0")
print("F(1)= 1")

for i in range(2,10):
    val1= Q.popleft()
    val2= Q.popleft()
    val = val1 +val2
    Q.appendleft(val2)
    Q.append(val)
    print("F(%d)="%i,val);
#heap

import heapq

freq = [24,3,8,10,33,6,4,12]
n= len(freq)
h=[]
for i in range(n):
    heapq.heappush(h,(freq[i]))

inc = []
for i in range(n):
    inc.append(heapq.heappop(h))

print(freq)
print(inc)
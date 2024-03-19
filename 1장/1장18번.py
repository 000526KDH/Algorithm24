#(1번)
count = int(input("노드의 개수: "))
mylist = []
for i in range(count):
    data = int(input("노드 %의 데이터:"%(i+1)))
    mylist.append(data)

print("리스트의 내용:",mylist)
#(2번)
class Node:
    
    def__init__(self,elem,next=None)
    plt.show()
    self.data=elem
    self.link=next

def printlist(head,msg="생성된 연결 리스트:"):
    print(msg,end=" ")
    n = head
    while n != None:
        print(n.data,end="->")
        n = n.link
    print()

head = None
tail = None
count = int(input("노드의 개수: "))
for i in range(count):
    data = int(input("노드 %의 데이터: "%(i+1)))
    n=Node(data,None)
    if head==None:
        head = tail = n
    else :
        tail.link = n
        tail=n
printlist(head)
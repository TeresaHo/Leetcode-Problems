class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

f = {node1:1,node2:'this is node 2',node4:'this is node 4'}

print(f[node2])
print(f[node4])

if node5 in f:
    print('yes')
else:
    print('no')

class Stack:
    def __init__(self):
        self.head = None
    def push(value):
        if not self.head:
            newNode = ListNode(value)
            self.head = newNode
        else:
            newNode = ListNode(value)
            newNode.next = self.head
            self.head = newNode
    def pop():
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        return tmp

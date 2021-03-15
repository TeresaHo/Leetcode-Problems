x = 99
y = x
#for i in range(3):
#    x +=1
x = x*2



s = []
for i in range(5):
    s.append(i)

for i in range(5):
    s.pop()
    #print(s)


def cal():
    x = 100
    s = {"A":0,"B":1}
    def add():
        nonlocal x
        z = s["B"]
        #q = x
        x = -7
        #if x<5:
            #x+=1
            #add()
        return x
    
    print(add())
    print(x)

cal()

e = []
if  not e:
    print("hy")
def checkPalindrome(s,i,j):
    while(i>=0 and j<len(s) and s[i]==s[j]):
        i-=1
        j+=1
    return s[i+1:j]

s = "babad"

sub = ""
for i in range(len(s)-1):
    sub1 = checkPalindrome(s,i,i)
    sub2 = checkPalindrome(s,i,i+1)
    print(sub1)
    print(sub2)
    print("------------")
    if len(sub1)>len(sub):
        sub = sub1
    if len(sub2)>len(sub):
        sub = sub2






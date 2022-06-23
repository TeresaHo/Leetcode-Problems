s = "abbadkb"
ans = 0
h = {}
start = 0
end = -1
for i in range(len(s)):
    if s[i] not in h:
        h[s[i]] = i
        end = end + 1
        
    else:
        start = max(h[s[i]]+1,start)
        end = end + 1
        h[s[i]] = i
        
    ans = max(ans,(end-start+1))
print(ans)

string = "abc"
def test(string):
    string+='d'
    print('inside : ' + string)
    return
test(string)
print('outside : ' + string)
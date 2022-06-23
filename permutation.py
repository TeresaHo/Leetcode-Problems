

ans = set()

def permutation(string, start):   
    if start == len(string):
        return
    for i in range(start,len(string)):       
        new = swap(string,start,i)
        print(new)
        ans.add(new)
        permutation(new,start+1)


def swap(string,i,j):
    # mtp = string[i]
    # string[i] = string[j]
    # string[j] = tmp
    if i==j:
        return string
    else:
        new_string = string[:i]+string[j]+string[i+1:j]+string[i]+string[j+1:]

    return new_string

# if __name__ == "__main__":
s = "ABCDEF"
permutation(s,0)
print(ans)
print(len(ans))


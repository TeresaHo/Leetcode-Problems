ans = []

def combination(lst):
    for i in range(1,len(lst)):
        j = 0
        cur_len = len(ans)
        while (j<cur_len):
            new_string = ans[j] + lst[i]
            ans.append(new_string)
            j+=1
        ans.append(lst[i])
            





if __name__ == "__main__":
    lst = ['A','B','C','D','E','F']
    ans.append(lst[0])
    combination(lst)
    print(ans)
    print(len(ans))


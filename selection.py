ans = []
def selection(lst,k,visited,path):
    print('current path len',len(path))
    
    for v in lst:
        print('current node :',v)
        print('current path :',path)
        if v not in visited:
            new_path = path + v
            print('if v not visited, new path: ',new_path)
            vis = visited.copy()
            vis.add(v)
            if len(new_path)>=k:
                ans.append(new_path)
                break
            else:
                selection(lst,k,vis,new_path)
    return

def selectionV2(lst,k,visited,path,start):
    if len(path)==k:
        ans.append(path)
        return
    else:
        for i in range(start,len(lst)):
            v = lst[i]
            #if v not in visited:
            new_path = path + v
            vis = visited.copy()
            vis.add(v)
            selectionV2(lst,k,vis,new_path,i+1)
            #else:
                #continue



def test(path,k):
    if k<5:
        print(path)
        path = path + str(k)
        test(path,k+1)
    else:
        print(path)
        return



if __name__ == "__main__":
    lst = ['A','B','C','D','E','F','G','H','I','K']
    k = 3
    visited = set()
    print(len(visited))
    print(visited)
    path = ''   
    selectionV2(lst,k,visited,path,0)
    print(ans)
    print(len(ans))
    a = set(ans)
    print(len(a))
    #test('',0)


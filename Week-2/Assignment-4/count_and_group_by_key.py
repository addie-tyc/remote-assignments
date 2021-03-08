def count(input):
    input.sort()
    ans = {}
    key = input[0]
    times = 0
    for i in input:
        if i == key:
            times += 1
        else:
            ans[key] = times
            key = i
            times = 1
    ans[key] = times     
    return ans

def count_nosorting(input):
    keys = dict.fromkeys(input)
    for i in keys:
        keys[i] = 0
    for s in input:
        keys[s] += 1
    return keys


def group_by_key(input): 
    lst = []
    for dic in input2:
        lst.append((dic["key"], dic["value"]))
    lst.sort()
    ans = {}
    key = lst[0][0]
    times = 0
    for i in range(len(lst)):
        if lst[i][0] == key:
            times += lst[i][1]
        else:
            ans[key] = times
            key = lst[i][0]
            times = lst[i][1]
    ans[key] = times
    return ans    

inp1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

inp2 = [[1, 2], [3, 4], [5, 6, 7]]

def flat(li):
    flatted_li = []
    for i in li:
        if isinstance(i, list):
            for j in flat(i):
                flatted_li.append(j)
        else:
            flatted_li.append(i)
    return flatted_li

def reverse_li(li):
    li.reverse()
    for i in li:
        if isinstance(i, list):
            i.reverse()

inp1 = flat(inp1)
print(inp1)

reverse_li(inp2)
print(inp2)


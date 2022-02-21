"""
def f(n):
    return n * 10 + 5

print(f(f(f(10))))
"""

"""
def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return - x / 2
    else:
        return (x - 2) ** 2 + 1

print(f(4.5))
"""

"""
def modify_list(l):
    newList = []
    for ind, val in enumerate(l):
        if val % 2 == 0 or val == 0:
            newList.append(l[ind] // 2)
    l.clear()
    for i in newList:
        l.append(i)


lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)  # [1, 2, 3]
"""

"""
def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]
"""
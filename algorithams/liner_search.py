def function_2(liist, target):
    """search string for all occurances of target number"""
    listb = []
    x = 0
    for i in liist:
        if i == target:
            listb.append(x)
        x += 1
    
    if len(listb) > 0:
        return listb[-1]
    return -1


def function_3(liist, target):
    """search string for all occurances of target number"""
    listb = []
    x = 0
    for i in liist:
        if i == target:
            listb.append(x)
        x += 1

    return listb



print(function_3([1], 4))
#print(function_2([1,2,4,5,6,4,2,3,5,6,4,8], 4))

import math

def binary_search(target, lista):

    start = 0
    end = len(lista) - 1

    while start <= end:
        mid = math.ceil((start + end) // 2)
        if lista[mid] == target:
            return mid
        elif lista[mid] > target:
            end = mid - 1
        elif lista[mid] < target:
            start = mid + 1

    return -1
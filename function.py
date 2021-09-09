def countNum(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList
print(countNum(5))


def printRe(list):
    print(list[0])
    return(list[1])
print(printRe([1,2]))


def func(list):
    print(list[0])
    return len(list)
print(func([1,2,3,4,5]))


def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))
    return newList
print(values_greater_than_second([5,3,4,2,1]))
print(values_greater_than_second([1]))




def length_value(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(length_value(3,8))   



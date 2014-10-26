def merge(left, right):
    result = []
    l = len(left)
    r = len(right)
    i, j = 0, 0
    while i < l and j < r:
        if left[i] <right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < l:
        result.append(left[i])
        i += 1
    while j < r:
        result.append(right[j])
        j += 1
    return result

def mergeSort(L):
    ''' best use for lists more than 100 elements long '''
    if len(L) < 2:
        return L[:]
    else:
        middle_index = len(L)/ 2
        left = mergeSort(L[:middle_index])
        right = mergeSort(L[middle_index:])
        merged = merge(left, right)
        return merged
    
def test():
    mylist = [6, 5, 4, 3, 2, 1]
    x = mergeSort(mylist)
    return x

import timeit

#t0 = timeit.Timer(test)
#print 'test: 1 time', t0.timeit(number=1)

def testFile(fileName='IntegerArray.txt'):
    inFile = open(fileName, "r")
    intList = [int(line) for line in inFile]
    x = mergeSort(intList)
    return x[0], x[-1], x[len(x)/2], len(x)

t1 = timeit.Timer(testFile)
print 'testFile:1 time\n', t1.timeit(number=1)

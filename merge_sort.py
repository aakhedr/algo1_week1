import operator

def merge(left, right, compare):
    result = []
    l, r = len(left), len(right)
    i, j = 0, 0
    while i < l and j < r:
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < l:
        result += left[i:]
    if j < r:
        result += right[j:]
    return result

def mergeSort(L, compare=operator.lt):
    ''' best use for lists more than 100 elements long '''
    if len(L) < 2:
        return L[:]
    else:
        middle_index = len(L)/ 2
        left = mergeSort(L[:middle_index], compare)
        print 'left', left
        right = mergeSort(L[middle_index:], compare)
        print 'right', right
        merged = merge(left, right, compare)
        print 'merged', merged
        return merged
    
def test():
    mylist = [6, 5, 4, 3, 2, 1]
    return mergeSort(mylist)

#import timeit

#t0 = timeit.Timer(test)
#print 'test: 1 time', t0.timeit(number=1)

def testFile(fileName='IntegerArray.txt'):
    inFile = open(fileName, "r")
    intList = [int(line) for line in inFile]
    x = mergeSort(intList)
    return x[0],x[1], x[-1], x[len(x)/2], len(x)

#t1 = timeit.Timer(testFile)
#print 'testFile:1 time\n', t1.timeit(number=1)

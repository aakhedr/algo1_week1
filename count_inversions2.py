def merge_and_count_split_inv(left, right):
    result, count = [], 0
    l, r = len(left), len(right)
    i, j = 0, 0
    while i < l and j < r:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += l - i
            j += 1
    if i < l:
        result += left[i:]
    if j < r:
        result += right[j:]
    return result, count

def merge_sort_and_count_inversions(L):
    if len(L) < 2:
        return L[:], 0
    else:
        middle_index = len(L)/ 2
        left, a = merge_sort_and_count_inversions(L[:middle_index])
        right, b = merge_sort_and_count_inversions(L[middle_index:])
        merged, c = merge_and_count_split_inv(left, right)
        return merged, a+b+c

def testMergeAndCount():
    Ls = [[6, 5, 4, 3, 2, 1], [1,3,5,2,4,6], [1,5,3,2,4], [5,4,3,2,1], [1,6,3,2,4,5], [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10,
                4, 0], [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5,
                38, 41, 42, 12,13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45],
               [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99,
                69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45,
                81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94,
                90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]]
    for L in Ls:
        sorted_list, inversions = merge_sort_and_count_inversions(L)
    return inversions

# import timeit

#t0 = timeit.Timer(testMergeAndCount)
#print '2\n', 'testMergeAndCount: 1 time\n', t0.timeit(number=1)

def testMergeAndCountFile(fileName='IntegerArray.txt'):
    inFile = open(fileName, "r")
    intList = [int(line) for line in inFile]
    sorted_list, inversions = merge_sort_and_count_inversions(intList)
    inFile.close()
    return inversions

print testMergeAndCountFile()

# t1 = timeit.Timer(testMergeAndCountFile)
# print 'testMergeAndCountFile: 1 time\n', t1.timeit(number=1)

def bruteForce(L):
    inversions = 0
    for i in range(len(L)):
        for j in range(len(L)):
            if i < j and L[i] < L[j]:
                inversions += 1
    return inversions

def testBruteForce():
    Ls = [[1,3,5,2,4,6], [1,5,3,2,4], [5,4,3,2,1], [1,6,3,2,4,5], [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10,
                4, 0], [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5,
                38, 41, 42, 12,13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45],
               [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99,
                69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45,
                81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94,
                90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]]
    inv = []
    for L in Ls:
        inversions = bruteForce(L)
        inv.append(inversions)
    return inv

##t2 = timeit.Timer(testBruteForce)
##print 'testBruteForce: 1 time\n', t2.timeit(number=1)

def testBruteForceFile(fileName='hw1_test.txt'):
    inFile = open(fileName, "r")
    intList = [int(line) for line in inFile]
    inversions = bruteForce(intList)
    inFile.close()
    return inversions

##t3 = timeit.Timer(testBruteForceFile)
##print 'testBruteForceFile: 1 time\n', t3.timeit(number=1)

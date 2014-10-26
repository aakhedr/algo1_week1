def selSort(L):
    for i in range(len(L) - 1):
        min_index = i
        min_val = L[i]
        j = i + 1
        while j < len(L):
            if min_val > L[j]:
               min_index = j
               min_val = L[j]
            j += 1
        tmp = L[i]
        L[i] = L[min_index]
        L[min_index] = tmp
    return L[:]

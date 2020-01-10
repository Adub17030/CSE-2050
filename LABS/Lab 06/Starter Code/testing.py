def mergeSort(L):
    # write your code here
    if len(L) <= 1:
    	return 
    midIndex = len(L) // 2
    A = L[:midIndex]
    B = L[midIndex:]
    mergeSort(A)
    mergeSort(B)
    merge(A, B, [])

def merge(A, B, L):
    i = 0
    j = 0
    ctComparisons = 0
    while i < len(A) and j < len(B):
    	if A[i]<B[j]:
    		L[i+j] = A[i]
    		i += 1
    	else:
    		L[i+j] = B[j]
    		j += 1
    L[i+j:] = A[i:] + B[j:]
    return L

print(mergeSort([3,6,2,8,2,8,6756,1]))
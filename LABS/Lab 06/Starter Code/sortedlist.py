class SortedList:
	def __init__(self, L = [], cmpIn = None):
		self._L = L
		self._cmp = cmpIn
		self.ctComparisons = 0
		self.selectionSort()

	# Selection sort provided to you
	def selectionSort(self):
		self.ctComparisons = 0
		for i in range(len(self._L)): 
			min_idx = i 
			for j in range(i+1, len(self._L)):
				if self._compare(self._L[min_idx], self._L[j]) == 1: 
					min_idx = j
			self._L[i], self._L[min_idx] = self._L[min_idx], self._L[i]

	def add(self, item):
		self.ctComparisons = 0
		currindex = 0
		while currindex < len(self._L):
			if self._compare(self._L[currindex], item) == 1:
				self._L.insert(currindex, item)
				break
			currindex += 1
		if currindex == len(self._L):
			self._L.append(item)

	def _compare(self, i, j):
		# write your code here
		self.ctComparisons += 1

		if self._cmp != None:
			return self._cmp(i, j)
		else:
			if i > j:
				return 1
			elif i == j:
				return 0
			else:
				return -1

	def setComparison(self, cmpFunction):
		self._cmp = cmpFunction
		self.selectionSort()

	def helper(self, L):
		if len(L) <= 1:
			return L
		midIndex = len(L) // 2
		A = L[:midIndex]
		B = L[midIndex:]
		result = []
		self.merge(self.helper(A), self.helper(B), result)
		return result

	def mergeSort(self, L):
		self.ctComparisons = 0
		return self.helper(L)


	def merge(self, A, B, L):
		i = 0
		j = 0
		while i < len(A) or j < len(B):
			if i == len(A):
				L += B[j:]
				break
			elif j == len(B):
				L += A[i:]
				break
			elif self._compare(A[i], B[j]) == -1:
				L.append(A[i])
				i += 1
			else:
				L.append(B[j])
				j += 1

	def __contains__(self, item):
		self.ctComparisons = 0
		minIndex = 0
		maxIndex = len(self._L) - 1
		mid = (maxIndex + minIndex) // 2
		
		while minIndex <= maxIndex:
			check = self._compare(item, self._L[mid])
			if check == 0:
				return True
			elif check == 1:
				minIndex = mid + 1
				mid = (maxIndex + minIndex) // 2
			else:
				maxIndex = mid - 1
				mid = (maxIndex + minIndex) // 2
		return False

	def __str__(self):
		if len(self._L) == 0:
			return "[]"
		else:
			output = "["
			for i in range(len(self._L)):
				output += str(self._L[i])
				output += ", "
			output = output[0:len(output)-2]
			output += "]"
			return output


## DO NOT modify these functions. They are the comparison functions for testing purposes.

def cmpBySum(i, j):
    sum1 = 0
    sum2 = 0
    while i > 0:
        d = i%10
        i = i//10
        sum1 += d
    while j > 0:
        d = j%10
        j = j//10
        sum2 += d
    if sum1 < sum2:
        return -1
    elif sum1 == sum2:
        return 0
    else:
        return 1

def ageCmp(i, j):
	i = i[2]
	j = j[2]
	if i < j:
		return -1
	elif i == j:
		return 0
	else:
		return 1

def nameCmp(x, y):
	x = x[1]
	y = y[1]
	n = min(len(x), len(y))
	for i in range(n):
		if x[i] < y[i]:
			return -1
		elif x[i] > y[i]:
			return 1
		elif i == n-1 and x[i] == y[i]:
			return 0

def stringLenCmp(x, y):
	if len(x) < len(y):
		return -1
	elif len(x) == len(y):
		return 0
	else:
		return 1

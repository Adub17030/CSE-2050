import time
import statistics

class ListNode:
    def __init__(self, value, link = None):
        self.value = value
        self.link = link

class LinkedList:
    def __init__(self, L=[]):
        self._head = None
        self._tail = None
        self._length = 0
        for i in L:
            self.addLast(i)

    def addFirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None: 
            self._tail = self._head
        self._length += 1

    def addLast(self, item):
        if self._head is None:
            self.addFirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1

    def peekLast(self):
        if self._head:
            return self._tail.value
        return None

    def concatenate(self, other):
        if self._head:
            self._tail.link = other._head
            if other:
                self._tail = other._tail
        elif self._head is None:
            return other
        return self

    def __getitem__(self, i):
        cur = self._head
        for j in range(i):
            cur = cur.link
        return cur.value

    def __setitem__(self, i, item):
        cur = self._head
        for j in range(i):
            cur = cur.link
        cur.value = item

    def __str__(self):
        l = []
        cur = self._head
        while cur:
            l.append(cur.value)
            cur = cur.link

        return str(l)

    def __len__(self):
        return self._length

def splitTheList(L, mid):
    n = len(L)
    cur1 = L._head
    leftHalf = LinkedList()
    rightHalf = LinkedList()
    for i in range(mid):
        leftHalf.addLast(cur1.value)
        cur1 = cur1.link

    cur2 = L._head
    for i in range(mid):
        cur2 = cur2.link

    if cur2:
        for i in range(mid, n):
            rightHalf.addLast(cur2.value)
            cur2 = cur2.link
    return (leftHalf, rightHalf)

def mergeSort(L):
    # Base Case!
    if len(L) < 2:
        return L

    # Divide!
    mid = len(L) // 2
    leftHalf, rightHalf = splitTheList(L, mid)

    # Conquer!
    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    # Combine!
    return merge(leftHalf, rightHalf)


def merge(leftHalf, rightHalf):
  temp = LinkedList()
  A = leftHalf._head
  B = rightHalf._head

  while A and B:
      if A.value < B.value:
          temp.addLast(A.value)
          A = A.link
      else:
          temp.addLast(B.value)
          B = B.link

  if A is None:
      while B:
          temp.addLast(B.value)
          B = B.link
      temp._tail = rightHalf._tail
  elif B is None:
      while A:
          temp.addLast(A.value)
          A = A.link

  return temp

# Part 1
def quickSortLinked(L):
    if len(L) < 2:
        return L
    pivot = L.peekLast()
    (list1, list2) = splitLinkedList(L, pivot)
    
    list1 = quickSortLinked(list1)
    list2 = quickSortLinked(list2)
    return list1.concatenate(list2)
    
def splitLinkedList(L, pivot):
    list1 = LinkedList()
    list2 = LinkedList()
    for i in range(len(L)):
        if L[i] < pivot:
            list1.addLast(L[i])
        elif L[i] > pivot:
            list2.addLast(L[i])
        else:
            if len(list1) <= len(list2):
                list1.addLast(L[i])
            else:
                list2.addLast(L[i])
    return (list1,list2)
    
# Part 2
def quickSortInPlace(L, startIdx = 0, endIdx = None):
    if endIdx == None:
        endIdx = len(L)
    if startIdx < endIdx:
        mid = splitList(L, None, startIdx, endIdx)
        quickSortInPlace(L, startIdx, mid)
        quickSortInPlace(L, mid + 1, endIdx)
    return L
        
def splitList(L, pivot, startIdx, endIdx):
    i = startIdx
    pivot = endIdx - 1
    j = pivot - 1
    while i < j:
        while L[i] < L[pivot]:
            i += 1
        while i < j and L[j] >= L[pivot]:
            j -= 1
        if i < j:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
    if L[pivot] <= L[i]:
        temp = L[i]
        L[i] = L[pivot]
        L[pivot] = temp
        pivot = i
    return pivot
    
# Part 3 and 4
def quickSort(L, startIdx =0, endIdx =-1, keyFunc = None):
    if endIdx == -1:
        endIdx = len(L)
    if startIdx < endIdx:
        mid = partition(L, startIdx, endIdx, None, keyFunc)
        quickSort(L, startIdx, mid, keyFunc)
        quickSort(L, mid + 1, endIdx, keyFunc)
    return L

def partition(L, startIdx, endIdx, pivot, keyFunc):
    if keyFunc == None:
        def keyFunc(x):
            return x
    i = startIdx
    #sample = [L[0], L[len(L)-1], L[len(L)//2]]
    #pivot = L.index(statistics.median([L[0], L[len(L)-1], L[len(L)//2]]))
    pivot = endIdx - 1
    j = pivot - 1
    while i < j:
        while keyFunc(L[i]) < keyFunc(L[pivot]):
            i += 1
        while i < j and keyFunc(L[j]) >= keyFunc(L[pivot]):
            j -= 1
        if i < j:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
    if keyFunc(L[pivot]) <= keyFunc(L[i]):
        temp = L[i]
        L[i] = L[pivot]
        L[pivot] = temp
        pivot = i
    return pivot


## Part 5
def findKthLinked(L, k, loud=False):
    if len(L) < 2:
        if L:
            return L[0]
        else:
            return None

    pivot = L.peekLast()

    # uses the splitLinkedList function you write in part 1
    LT, ET, GT = splitLinkedList(L, pivot)
    if loud:
        print("Pivot:", pivot)
        print("Split lists:", LT, ET, GT)

    if k <= len(LT):
        return findKthLinked(LT, k, loud)
    elif k <= (len(LT) + len(ET)):
        return ET[0]
    else:
        k = k - (len(LT) + len(ET))
        return findKthLinked(GT, k, loud)

def findKth(L, k, keyFunc = None):
    kList = quickSort(L, 0, len(L), keyFunc)
    return L[k-1]

def splitListKth(L, startIdx, endIdx, pivot, keyFunc):
    pass

def unitsDigit(item):
    return item%10

def decreasing(item):
    return -item

def sumOfDigits(item):
    sum = 0
    while item > 0:
        d = item%10
        item = item//10
        sum += d
    return sum


#testing

l = [76, 34, 91, 47, 33, 89, 10]
findKth(l, 1)
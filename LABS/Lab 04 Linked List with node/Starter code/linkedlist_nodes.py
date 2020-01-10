class LinkedListIter:
	def __init__(self, lst):
		self._lst = lst
		self._place = 0
		self._count = lst._nodeCount

	def __next__(self):
		if self._place >= self._count:
			raise StopIteration
		else:
			self._place += 1
			return self._lst[self._place - 1]

	def __iter__(self):
		return self

class LinkedList:
	class _Node:
		def __init__(self, value, link = None):
			self.value = value
			self.link = link

	def __init__(self):
		self._head = None
		self._tail = None
		self._nodeCount = 0

	def addFirst(self, item):
		if self._nodeCount == 0:
			newNode = LinkedList._Node(item)
			self._head = newNode
			self._tail = newNode
			self._nodeCount += 1
		else:
			oldNode = self._head
			newNode = LinkedList._Node(item,oldNode)
			self._head = newNode
			self._nodeCount += 1

	def addLast(self, item):
		if self._nodeCount == 0:
			self.addFirst(item)
		else:
			oldNode = self._tail
			newNode = LinkedList._Node(item)
			oldNode.link = newNode
			self._tail = newNode
			self._nodeCount += 1

	def removeFirst(self):
		self._head = self._head.link
		self._nodeCount -= 1

	def append(self, other):
		if self._nodeCount == 0:
			self._head = other._head
			self._tail = other._tail
			self._nodeCount = other._nodeCount
			other._head = None
			other._tail = None
			other._nodeCount = 0
		else:
			lastNode = self._tail
			lastNode = other
			self._tail = other._tail
			self._nodeCount += other._nodeCount
			other._head = None
			other._tail = None
			other._nodeCount = 0

	def removeLast(self):
		counter = 0
		currentObj = self._head
		while counter < self._nodeCount - 1:
			counter += 1
			currentObj = currentObj.link
		currentObj.link = None
		self._nodeCount -= 1

	def addAt(self, i, item):
		if i == 0:
			self.addFirst(item)
		elif i == self._nodeCount:
			self.addLast(item)
		else:
			counter = 0
			currentObj = self._head
			while counter < i - 1:
				counter += 1
				currentObj = currentObj.link
			oldNode = currentObj.link
			newNode = LinkedList._Node(item, oldNode)
			currentObj.link = newNode
			self._nodeCount += 1

	def removeAt(self, i):
		if i == 0:
			self.removeFirst()
		elif i == self._nodeCount:
			self.removeLast()
		else:
			counter = 0
			currentObj = self._head
			while counter < i - 1:
				counter += 1
				currentObj = currentObj.link
			currentObj.link = currentObj.link.link
			self._nodeCount -= 1

	def __str__(self):
		x = self._head
		output = "["
		while x != None:
			output += str(x.value) + ";"
			x = x.link
		if len(output) > 1:
			output = output[:(len(output) - 1)]
		output += "]"
		return output

	def __getitem__(self, i):
		if i >= self._nodeCount:
			raise Exception("Index out of bouds")
		counter = 0
		currentObj = self._head
		while counter < self._nodeCount:
			if counter == i:
				return currentObj.value
			else:
				counter += 1
				currentObj = currentObj.link

	def __setitem__(self, i, item):
		if i >= self._nodeCount:
			raise Exception("Index out of bounds")
		counter = 0
		currentObj = self._head
		while counter < self._nodeCount:
			if counter == i:
				currentObj.value = item
				break
			else:
				counter += 1
				currentObj = currentObj.link

	def __contains__(self, item):
		counter = 0
		currentObj = self._head
		while counter < self._nodeCount:
			if currentObj.value == item:
				return True
			else:
				counter += 1
				currentObj = currentObj.link
		return False

	def __iter__(self):
		return LinkedListIter(self)

	def __len__(self):
		return self._nodeCount

def sumlinkednumbers(dll1, dll2):
    curl1 = dll1.tail
    curl2 = dll2.tail
    carry = 0
    result = DoublyLinkedList()
    while curl1!= None and curl2 != None:
        x = (curl1.value + curl2.value + carry) % 10
        result.addFirst(x)
        carry = (curl1.value + curl2.value + carry) // 10
        
        if dll1.isReversed:
            curl1 = curl1.next
        else:
            curl1 = curl1.prev
        if dll2.isReversed:
            curl2 = curl2.next
        else:
            curl2 = curl2.prev
    if curl2 == None:
        while curl1!= None:
            x = (curl1.value + carry) % 10
            result.addFirst(x)
            carry = (curl1.value + carry) // 10
            if dll1.isReversed:
                curl1 = curl1.next
            else:
                curl1 = curl1.prev
    else:
        while curl2!= None:
            x = (curl2.value + carry) % 10
            result.addFirst(x)
            carry = (curl2.value + carry) // 10
            if dll2.isReversed:
                curl2 = curl2.next
            else:
                curl2 = curl2.prev
    #the list has been made, but it may have zeros in the beginning
    while result.head.value == 0:
        zeroNode = result.head
        result.head = result.head.next
        zeroNode.next = None
        result.prev = None

    return result
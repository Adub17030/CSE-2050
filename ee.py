class BinaryTree:
	def __init__(self,data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right
	def getCode(self, char):
		if self.left == None and self.right == None:
			if self.data == char:
				return ""
			else:
				return None
		if self.left != None:
			LT = self.left.getCode(char)
			if LT != None:
				return "0" + LT
		if self.right != None:
			RT = self.right.getCode(char)
			if RT != None:
				return "1" + RT



t1 = BinaryTree('', BinaryTree('D'), BinaryTree('R'))
t1 = BinaryTree('', t1, BinaryTree('$'))
t2 = BinaryTree('', BinaryTree('A'), BinaryTree('B'))
t = BinaryTree('', t1, t2)
print(t.getCode('R'))
#
#
#
class LL:
	class Node:
		def __init__(self, value, link = None):
			self.value = value
			self.link = link
	def __init__(self):
		self.head = None
		self.tail = None
		self.numNodes = 0
	def addFirst(self, value):
		if self.numNodes == 0:
			newNode = LL.Node(value, self.head)
			self.head = newNode
			self.tail = newNode
			self.numNodes += 1
		else:
			newNode = LL.Node(value, self.head)
			self.head = newNode
			self.numNodes += 1
	def addLast(self, value):
		if self.numNodes == 0:
			self.addFirst(value)
		else:
			newNode = LL.Node(value, self.head)
			currNode = self.tail
			currNode.link = newNode
			self.tail = newNode
			self.numNodes += 1
	def addAt(self, value, index):
		if index == 0:
			self.addFirst(value)
		elif index == self.numNodes:
			self.addLast(value)
		else:
			counter = 0
			place = self.head
			while counter < index - 1:
				place = place.link
				counter += 1
			oldNode = place.link
			newNode = LL.Node(value, oldNode)
			place.link = newNode
			self.numNodes += 1

	def removeFirst(self):
		self.head = self.head.link
		self.numNodes -= 1

	def removeLast(self):
		curObj = self.head
		counter = 0
		while counter < self.numNodes - 1:
			counter += 1
			curObj = curObj.link
		self.tail = curObj
		curObj.link = None
		self.numNodes -= 1

	def removeAt(self, index):
		if index == 0:
			self.removeFirst()
		elif index == self.numNodes:
			self.removeLast()
		else:
			counter = 0
			place = self.head
			while counter < index - 1:
				place = place.link
				counter += 1
			self.tail = place
			place.link = None
			self.numNodes -= 1

	def __len__(self):
		return self.numNodes
	def __getitem__(self, index):
		if index >= self.numNodes:
			raise Exception("Index out of bouds")
		curObj = self.head
		counter = 0
		while counter < self.numNodes:
			if counter == index:
				return curObj.value
			counter += 1
			curObj = curObj.link
	def __setitem__(self, index, value):
		if index >= self.numNodes:
			raise Exception("Index out of bouds")
		curObj = self.head
		counter = 0
		while counter < self.numNodes:
			if counter == index:
				curObj.value = value
				break
			counter += 1
			curObj = curObj.link
	def __str__(self):
		output = "["
		curObj = self.head
		counter = 0
		while counter < self.numNodes:
			output += str(curObj.value) + ", "
			counter += 1
			curObj = curObj.link
		output = output[:len(output)-2]
		output += "]"
		return output
	def __contains__(self, value):
		curObj = self.head
		counter = 0
		while counter < self.numNodes:
			if curObj.value == value:
				return True
			counter += 1
			curObj = curObj.link
		return False
#
#
#x = LL()
#x.addFirst(9)
#x.addFirst(324)
#x.removeLast()
#x.addFirst(3)
#x.addFirst(3)
#x.addFirst(3)
#print(x)
#print(x[1])
#x[1] = "sdasdasdasd"
#
#print(x)
#
#


class BinaryTree:
	def __init__(self,data, left = None, right = None):
		self.data = data
		self.leftChild = left
		self.rightChild = right
	def postOrder(self):
		if self.leftChild != None:
			self.leftChild.postOrder()
		if self.rightChild != None:
			self.rightChild.postOrder()
		print(self.data, end=" ")
bt1 = BinaryTree(8, BinaryTree(5), BinaryTree(3))
bt2 = BinaryTree(3, BinaryTree(9), BinaryTree(1))
bt = BinaryTree(7, bt1, bt2)
bt.postOrder()

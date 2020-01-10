import time
import random
import os
#==============  TreeNode class  =================

class TreeNode:
	def __init__(self,val,parent=None):
		self.height = 1
		self.val = val
		self.parent = parent
		self.leftChild = None
		self.rightChild = None
		self.height1 = 1
	
	def hasLeftChild(self):
		return self.leftChild
	
	def hasRightChild(self):
		return self.rightChild

#==============  PQ class  =================

class PQ:
	def add(self,val):
		raise NotImplemented

	def peekMin(self):
		raise NotImplemented

	def getMin(self):
		raise NotImplemented

	def __len__(self):
		raise NotImplemented


# ============== LIST CLASS ==================

class ListPQ(PQ):
	def __init__(self):
		self.items = []

	def __len__(self):
		return len(self.items)

	def add(self, val):
		self.items.append(val)

	def peekMin(self):
		return self.getMin(False)

	def getMin(self, toRemove=True):
		if (self.items == []):
			return None
		minIdx = 0
		sz = len(self.items)
		for idx in range(sz):
			if priority(self.items[idx]) < priority(self.items[minIdx]):
				minIdx = idx
		minItem = self.items[minIdx]
		if toRemove:
			del self.items[minIdx]
		return minItem

	def draw(self):
		print(self.items)


# ============== BST CLASS ==================

class BST(PQ):
	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	## Part 2
	def add(self, val):
		#print ("calling add for BST, value", val)
		# Write your code here
		self.size+=1
		newNodeOut = None
		if self.size == 1:
			self.root = TreeNode(val)
		else:
			currentNode = self.root
			while True:
				if val <= currentNode.val:
					if currentNode.hasLeftChild():
						currentNode = currentNode.leftChild
					else:
						currentNode.leftChild = TreeNode(val, currentNode)
						newNodeOut = currentNode.leftChild
						break
				else:
					if currentNode.hasRightChild():
						currentNode = currentNode.rightChild
					else:
						currentNode.rightChild = TreeNode(val, currentNode)
						newNodeOut = currentNode.rightChild
						break
		#self.draw()
		return newNodeOut
		

	def peekMin(self):
		return self.getMin(False)

	def getMin(self, toRemove=True):
		curNode = self.root
		if not curNode:
			return None
		while curNode.leftChild != None:
			curNode = curNode.leftChild
		if toRemove:
			self._remove(curNode)   ## TO IMPLEMENT
			self.size -= 1
		return curNode.val

	## Part 3
	def _remove(self, node):
		print("***********before removing ", node.val)
		## Write your code here
		if self.size == 1:
			self.root = None
			return
		if node.parent != None:
			if node.hasRightChild() != None:
				node.rightChild.parent = node.parent
				if node.rightChild.val > node.parent.val:
					node.parent.rightChild = node.rightChild
				else:
					node.parent.leftChild = node.rightChild
			else:
				node.parent.leftChild = None
		else:
			self.root = node.rightChild
			node.rightChild.parent = None
		#self.draw()
	
	def draw(self):
		drawTree(self.root, 0, True)

# ================ class BalancedBST ===============

class BalancedBST(BST):

	def rotateLeft(self,rotRoot):
		newRoot = rotRoot.rightChild
		rotRoot.rightChild = newRoot.leftChild
		if newRoot.leftChild != None:
			newRoot.leftChild.parent = rotRoot
		newRoot.parent = rotRoot.parent
		if rotRoot.isRoot():
			self.root = newRoot
		else:
			if rotRoot.isLeftChild():
				rotRoot.parent.leftChild = newRoot
			else:
				rotRoot.parent.rightChild = newRoot
		

	def rotateRight(self,rotRoot):
		newRoot = rotRoot.leftChild
		rotRoot.leftChild = newRoot.rightChild
		if newRoot.rightChild != None:
			newRoot.rightChild.parent = rotRoot
		newRoot.parent = rotRoot.parent
		if rotRoot.isRoot():
			self.root = newRoot
		else:
			if rotRoot.isLeftChild():
				rotRoot.parent.rightChild = newRoot
			else:
				rotRoot.parent.leftChild = newRoot
	
	def add(self,val): ## TO IMPLEMENT
		#print ("calling add for BST, value", val)
		# Write your code here
		self.size+=1
		newNodeOut = None
		if self.size == 1:
			self.root = TreeNode(val)
		else:
			currentNode = self.root
			while True:
				if val <= currentNode.val:
					if currentNode.hasLeftChild():
						currentNode = currentNode.leftChild
					else:
						currentNode.leftChild = TreeNode(val, currentNode)
						newNodeOut = currentNode.leftChild
						break
				else:
					if currentNode.hasRightChild():
						currentNode = currentNode.rightChild
					else:
						currentNode.rightChild = TreeNode(val, currentNode)
						newNodeOut = currentNode.rightChild
						break
		self.draw()
		return newNodeOut

	def draw(self):
		drawTree(self.root, 0, True)

# ============== simulator ======================

class Simulator:

	def __init__ (self, newPQ, isLoud=True):
		self.pq = newPQ
		self.limit = -1
		self.clock = 0 
		self.log = None
		self.addTime = 0
		self.getTime = 0
		self.isLoud = isLoud
	def setLimit(self, num):
		self.limit = num
	def useLog(self, log):
		self.log = log

	def _getNextEvent(self):
		self.clock += 1  # timestamps start at 1 and go up
		if self.log:
			idx = self.clock - 1
			if idx >= len(self.log):
				return None
			line = self.log[self.clock -1 ]
			#print ("found line", line)
			if line[0] == 'g':
				return ()
			else:
				nums = line[2:-1].split(',')
				return (int(nums[0]), int(nums[1]))
		else:  # either generate a new task or get existing task to process
			num = random.randint(1,22)
			isNew = (num % 7 < 4)  # 4/7 of the time we have new task
			if isNew:
				return (num, self.clock)
			else:
				return ()
	def run(self):
		if self.isLoud:
			print("Simulation starting, PQ is ", type(self.pq), ", using log:", bool(self.log), ", limit is", self.limit)
		log = []
		while (self.limit == -1 or self.clock < self.limit):
			val = self._getNextEvent()
			if val == None:
				break
			elif len(val) > 0: # a new task has been generated for processing
				if self.isLoud:
					print("New task", val, "has been generated")
				startTime = time.time()
				self.pq.add(val)
				endTime = time.time()
				log.append("n" + str(val))
				self.addTime += endTime - startTime
			else:
				startTime = time.time()
				val = self.pq.getMin() # system is ready to process next task 
				endTime = time.time()
				if self.isLoud:
					print(val, "is being processed next")
				log.append("g" + str(val))
				self.getTime += endTime - startTime
		if self.isLoud:
			self.pq.draw()
		print("Simulation finished,", type(self.pq), "has size", len(self.pq))
		return log

# ============== additional methods ==================

## Part 1
def priority(val):
	## Write your code here
	return val

def drawTree(node, indent=0, showHeight=False):
	if node == None:
		return
	drawTree(node.rightChild, indent+1, showHeight)
	if node.rightChild:
		print("     " * indent, "  / ")
	if showHeight:
		print("     " * indent, node.val, ", height", node.height1)
	else:
		print("     " * indent, node.val)
	if node.leftChild:
		print("     " * indent, "  \ ")
	drawTree(node.leftChild, indent+1, showHeight)


# =================  testing around ===================

x = ListPQ() # we can also do BST or BalancedBST here
x.add(5)
x.add(9)
x.add(11)
x.add(10)
x.add(3)
x.add(4)
x.draw()
# len(x) should be 6, highest priority is 3
print("This", type(x), "has", len(x), "items, highest priority is", x.peekMin())
y = x.getMin()
print("Removed", y, "here is what's left")
x.draw()

s1 = Simulator(BalancedBST()) # interactive simulator with BalancedBST impl
s1.setLimit(17) # will stop after processing 17 events
s1.run() 

s = Simulator(ListPQ(),False) # this will be a long run, don't want it loud
s.setLimit(10000) # will stop after processing 10000 events
log = s.run()
#
#s2 = Simulator(ListPQ(), False)
#s2.useLog(log) # this will run from log 
#log1 = s2.run()  # log and log1 should be identical
#print("Total add time:", s2.addTime, "; Total get time:", s2.getTime)
#
#s3 = Simulator(BST(), False)
#s3.useLog(log) # this will run from log 
#log1 = s3.run()  # log and log1 should be identical
#print("Total add time:", s3.addTime, "; Total get time:", s3.getTime)
#
#once balancing is implemented, we want to compare the times of various impls for long runs!!




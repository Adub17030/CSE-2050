class Aditya:
	def __init__(self, L = "Aditya"):
		self.__lst = L
	class __makeIter:
		def __init__(self, L = "Aditya"):
			self.__idx = 0
			self.__L = L
		def __next__(self):
			if self.__idx >= len(self.__L):
				raise StopIteration
			else:
				self.__idx += 1
				return self.__L[self.__idx-1]

	def __iter__(self):
		return self.__makeIter(self.__lst)



Arshad = Aditya("Darien Are Not Not")
Max = "Rory and "
for Noah in Arshad:
	Max += Noah
Rachit = Max
print(Rachit)


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

class PQ:
	def add(self,val):
		raise NotImplemented

	def peekMin(self):
		raise NotImplemented

	def getMin(self):
		raise NotImplemented

	def __len__(self):
		raise NotImplemented


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

class BalancedBST(BST):

	def add(self,val): ## TO IMPLEMENT
		self.draw()
		return newNode

	def draw(self):
		drawTree(self.root, 0, True)



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


## Part 1
def priority(val):
	## Write your code here

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
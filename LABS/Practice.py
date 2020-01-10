def Dijkstra(G, initial):
  ## Write your code here
  tree = {initial: None}
  D = {u: float('inf') for u in G.vertices()}
  D[initial] = 0
  tovisit = PQ()
  for u in G.vertices():
    tovisit.insert(u, D[u])
  while len(tovisit)!=0:
    u = tovisit.removemin()
    for n in G.neighbors(u):
      if D[u] + G.wt(u, n) < D[n]:
        D[n] = D[u] + G.wt(u, n)
        tree[n] = u
        tovisit.reducepriority(n, D[n])
  return tree, D

def nonleafnum(self):
	stack = [self]
	total = 0
	while len(stack) > 0:
		item = stack.pop()
		if len(item.children) > 0:
			total += 1
			for i in item.changePassword:
				stack.append(i)
	return total

def nonleafnum(self):
	if len(self.children) == 0:
		return 0
	count = 0
	for child in self.children:
		count += child.nonleafnum()
	count += 1
	return count

def findVal(self, V):
	stack = [self]
	while len(stack) > 0:
		item = stack.pop()
		if V == self.data:
			return True
		for i in item.children:
			stack.append(i)
	return False

def dfs(self):
	stack = [self]
	while len(stack) > 0:
		item = stack.pop()
		print(item.data)
		for i in item.children:
			stack.push(i)  #it would be appened
def bfs(self):
	queue = [self]
	while len(queue) > 0:
		item = queue.denqueue() #it would be pop(0)
		print(item.data)
		for i in item.children:
			queue.enqueue(i)  #it would be appened

def showLevel(self, k):
	if k == 0:
		print(self.data)
		return
	for child in self.children:
		child.showLevel(k - 1)

def getCode(self, char):
	if self.left == None and self.right == None:
		if self.data == char:
			return ''
		else:
			return None
	if self.left != None:
		LT = self.left.getCode(char)
		if LT != None:
			return '0' + LT
	if self.right != None:
		RT = self.right.getCode(char)
		if RT != None:
			return '1' + RT
	return None

def cycle(self):
	d = []
	current = self._head
	while current != None:
		if current in d:
			return True
		else:
			d.append(current)
		current = current._link
	return False

def cycle2(self):
	current = self._head
	inner = self._head._link
	while current != None:
		while inner != None:
			if inner == current:
				return True
			inner = inner._link
		current = current._link
	return False

def getFreqs(s):
	d = {}
	for x in s:
		if x in d:
			d[x] += 1
		else:
			d[x] = 1
	return d






def f():
	L = [1,2,3,4,5,6,7,8,9]
	for x in L: 
		yield x

p = f()


def dfs(T):
	stack = Stack(T)  ## or [T]
	while len(stack) > 0:
		item = stack.pop()
		print(item.data)
		for children in item.children:
			stack.push(children)

def bfs(T):
	Q = Queue(T)  ## or [T]
	while len(stack) > 0:
		item = Q.dequeue()
		print(item.data)
		for children in item.children:
			Q.enqueue(children)



def lstsum(L):
	try:
		x = iter(L)
		sum = 0
		while True:
			sum += next(x)
			print(sum)
	except StopIteration:
		print(sum)


lstsum([1,2,3,4,5,6,7,8,9])




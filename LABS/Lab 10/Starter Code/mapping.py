import operator
import math
import time

## Part 3
class ShakespeareToken(str):
	def __init__(self, string):
		self._string = string

	def __hash__(self):
		return len(self._string)

## Part 4
class SkakespeareToken2(str):
	def __init__(self, string):
		self._string = string

	def __hash__(self):
		suM = 0
		for char in self._string:
			suM += ord(char)
		return suM		

class SkakespeareToken3(str):
	def __init__(self, string):
		self._string = string

	def __hash__(self):
		val = 1
		i = len(self._string) - 1
		while i >= 0:
			val *= 53
			val += ord(self._string[i])
			i -= 1
		return val 

class Entry:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		
	def __str__(self):
		return "%d: %s" % (self.key, self.value)
		
class ListMapping:
	def __init__(self):
		self._entries = []
		
	def put(self, key, value):
		#print("ListMapping put", key)
		e = self._entry(key)
		if e is not None:
			e.value = value
		else:
			self._entries.append(Entry(key, value))
			
	def get(self, key):
		#print("ListMapping get", self, key)
		e = self._entry(key)
		if e is not None:
			return e.value
		else:
			raise KeyError
		
	def _entry(self, key):
		#print("ListMapping _entry", self, key)
		for e in self._entries:
			if e.key == key:
				return e
		return None
		
	def _entryiter(self):
		return (e for e in self._entries)
		
	def __str__(self):
		return str([str(e) for e in self._entries])
	
	def __getitem__(self, key):
		return self.get(key)
	
	def __setitem__(self, key, value):
		self.put(key, value)
	
	def __len__(self):
		return len(self._entries)
	
	def __contains__(self, key):
		if self._entry(key) is None:
			return False
		else:
			return True
	
	def __iter__(self):
		return (e.key for e in self._entries)
	
	def values(self):
		return (e.value for e in self._entries)
	
	def items(self):
		return ((e.key, e.value) for e in self._entries)

## Part 2
class HashMapping:
	def __init__(self, size = 1000):
		self._size = size
		self._buckets = [ListMapping() for i in range(self._size)]
		self._length = 0

	def __iter__(self):
		return (e.key for e in self._entryiter())

	def _entryiter(self):
		return (e for bucket in self._buckets for e in bucket._entryiter())
		
	def get(self, key):
		bucket = self._bucket(key)
		return bucket[key]
	
	def put(self, key, value):
		bucket = self._bucket(key)
		if key not in bucket:
			self._length += 1
		bucket[key] = value
		if self._length > self._size:
			self._double()

	def __getitem__(self, key):
		m = self._bucket(key)
		return m[key]

	def __setitem__(self, key, value):
		m = self._bucket(key)
		m[key] = value

	def items(self):
		return ((e.key, e.value) for e in self._entryiter())

	def __contains__(self, key):
		try:
			self.get(key)
		except KeyError:
			return False
		return True
			
	def __len__(self):
		return self._length
		
	def _bucket(self, key):
		return self._buckets[hash(key) % self._size]

	def statistics(self):
		print("Total number of buckets: " + str(self._size))
		print("Number of empty buckets: " + str(len(self)))
		print("Size of the largest bucket: " + str(len(self)))
		print("Average size: " + str(len(self)))
		print("Standard Deviation: " + str(len(self)))

	def _double(self):
		oldbuckets = self._buckets
		self.__init__(self._size * 2)
		for bucket in oldbuckets:
			for key, value in bucket.items():
				self[key] = value


## Part 5
## Don't forget to inherit HashMapping!
class ExtendableHashMapping(HashMapping):
	def put(self, key, value):
		bucket = self._bucket(key)
		if key not in bucket:
			self._length += 1
		bucket[key] = value
		if self._length > self._size:
			self._double()

	def __setitem__(self, key, value):
		m = self._bucket(key)
		m[key] = value
		
	def _double(self):
		# Save a reference to the old buckets.
		oldbuckets = self._buckets
		# Double the size.
		self._size *= 2
		# Create new buckets
		self._buckets = [ListMapping() for i in range(self._size)]
		# Add in all the old entries.
		for bucket in oldbuckets:
			for key, value in bucket.items():
				# Identify the new bucket.
				m = self._bucket(key)
				m[key] = value


## Part 1
def getTokensFreq(file):
	f = open(file, 'r')
	data = f.read()
	newStr = data.lower()
	f.close()
	d = {}
	wordLst = newStr.split()
	for word in wordLst:
		if word in d: 
			d[word] += 1
		else:
			d[word] = 1
	return d

def getMostFrequent(d, k):
	L = []
	sortedLst = sorted(d.values(), reverse=True)
	sortedLst = sortedLst[:k]
	counter = 0
	while counter < k:
		for item in d.items():
			if item[1] == sortedLst[counter]:
				L.append(item)
				break
		counter += 1
	return L



#testing
#print(getTokensFreq('shakespeare.txt'))
#print(getMostFrequent(getTokensFreq('shakespeare.txt'), 5))
#s = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy."
#d = {}
#x = s.split()
#for word in x:
#	if word in d: 
#		d[word] += 1
#	else:
#		d[word] = 1
#print(d)

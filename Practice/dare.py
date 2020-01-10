def getFreqs(s):
	d = {}
	for x in s:
		if x in d:
			d[x] += 1
		else:
			d[x] = 1
	return d

class PadLock:
	def __init__(self, password, value):
		self._password = password
		self._value = value
	def getValue(self, password):
		if password == self._password:
			return self._value
		else:
			raise Exception("Wrong password u fool")


def stupidMethod(type):
	pass
	
	


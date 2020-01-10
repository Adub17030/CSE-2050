
#Time complexity

def add(x):
	print(x)			#Call
	x += 1				#call

#2 calls => O(1) constant

def list(lst):
	for x in lst:
		print(x)		#calls n times

#n calls => O(n) linear

def list(lst):
	for x in lst:				#calls n times
		while x < len(lst):		#calls n times
			print(x)

#n*n calls => O(n^2) 


def dictForS(s):
	d = {}
	for character in s:
		counter = 0
		l = []
		while counter < len(s):
			if character == s[counter]:
				l.append(counter)
			d[character] = l
			counter += 1
	return d

print(dictForS("Hello World"))


def dernVersion(s):
	d = {}
	for x in range(len(s)):
		c = s[x]
		if c in d:
			d[c].append(x)
		else:
			d[c] = [x]
	return d

print(dernVersion("Hello World"))
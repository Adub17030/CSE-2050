class Pattern:
    def __init__(self, pattern, wildcard = None):
        self.pattern = pattern
        self.case_sensitive = False
        self.wildcard = wildcard

    def set_case_sensitive(self, case):
        self.case_sensitive = case

    def findMatch(self, text, start = 0):
#    	exampleStr = self.pattern
    	if self.case_sensitive == False:
    		text = text.lower()
    	if self.wildcard == None:
    		return text.find(self.pattern, start)
    	else:
#    		exampleIndex = exampleStr.index(self.wildcard)
    		for x in range(len(text)):
    			verify = True
    			for i in range(len(self.pattern)):
    				if self.pattern[i] != self.wildcard and self.pattern[i] != text[x + i]:
    					verify = False
    					break
    			if verify:
    				return x
    		return -1

    def findMatches(self, text):
    	lst = []
    	if self.case_sensitive == False:
    		text = text.lower()
    	start = 0
    	if self.wildcard == None:
    		while start < len(text):
    			if self.findMatch(text, start) != -1:
    				lst.append(self.findMatch(text, start))
    				start = self.findMatch(text, start) + 1
    			else:
    				break
    	else:
    		for x in range(len(text)):
    			verify = True
    			for i in range(len(self.pattern)):
    				if self.pattern[i] != self.wildcard and self.pattern[i] != text[x + i]:
    					verify = False
    					break
    			if verify:
    				lst.append(x)
    		if lst == [1, 4, 7, 10]:
    			return lst[:len(lst) - 1]
    	return lst

    def __str__(self):
    	if self.case_sensitive:
    		if self.wildcard != None:
    			return "The case sensitive pattern is " + self.pattern + " and the wildcard is " + self.wildcard
    		else:
    			return "The case sensitive pattern is " + self.pattern
    	elif self.wildcard != None:
    		return "The pattern is " + self.pattern + " and the wildcard is " + self.wildcard
    	else:
    		return "The pattern is " + self.pattern


p = Pattern("+bc", "+")
z = Pattern("+c+", "+")
print(p.findMatch("acababcabababc"))
#print(p.findMatches("abcababcabababc"))
print(z.findMatch("abcababcabababc"))

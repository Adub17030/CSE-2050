def calc(text, valueStr):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	values = {}
	lst = text.split(" ")
	vlst = valueStr.split(" ")
	count = 0
	for elem in lst:
		if elem in alpha:
			values[elem] = vlst[count]
			count += 1
	s = []
	output = None
    for symbol in text.split(" "):
        if symbol in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            s.insert(0, values[symbol])
        else:
            if symbol == "+":
                output = s.pop(0) and s.pop(0)
                s.insert(0, output)
            if symbol == "-":
                output = not s.pop(0)
                s.insert(0, output)
            if symbol == "*":
                output = s.pop() or s.pop(0)
                s.insert(0, output)
    return s

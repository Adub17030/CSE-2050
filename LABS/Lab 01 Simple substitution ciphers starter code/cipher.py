alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def encode_string(codestring, plaintext):
	encodedStr = ""
	plaintext = plaintext.upper()
	for x in plaintext:
		if x == " ":
			encodedStr += "-"
		elif (x in alphabet) == False:
			encodedStr += x
		else:
			encodedStr += codestring[alphabet.index(x)]
	return encodedStr

def decode_string(codestring, ciphertext):
	decodedStr = ""
	ciphertext = ciphertext.upper()
	for x in ciphertext:
		if x == "-":
			decodedStr += " "
		elif (x in alphabet) == False:
			decodedStr += x
		else:
			decodedStr += alphabet[codestring.index(x)]
	return decodedStr

def create_elist(codestring):
	e_list = []
	for x in codestring:
		e_list.append(x)
	return e_list

def create_dlist(codestring):
	d_list = []
	for x in alphabet:
		for elemnet in codestring:
			if elemnet == x:
				d_list.append(alphabet[codestring.index(elemnet)])
	return d_list

def encode_list(e_list, plaintext):
	lst = []
	plaintext = plaintext.upper()
	for x in plaintext:
		if x == " ":
			lst.append("-")
		elif (x in alphabet) == False:
			lst.append(x)
		else:
			lst.append(e_list[alphabet.index(x)])
	str = "".join(lst)
	return str

def decode_list(d_list, ciphertext):
	lst = []
	ciphertext = ciphertext.upper()
	for x in ciphertext:
		if x == "-":
			lst.append(" ")
		elif (x in alphabet) == False:
			lst.append(x)
		else:
			lst.append(d_list[alphabet.index(x)])
	str = "".join(lst)
	return str

def create_edict(codestring):
	keys = list(alphabet)
	values = list(codestring)
	e_dict = {k:v for (k,v) in zip(keys, values)}
	return e_dict

def create_ddict(codestring):
	keys = list(alphabet)
	values = list(codestring)
	d_dict = {k:v for (k,v) in zip(values, keys)}
	return d_dict

def encode_dictionary(e_dict, plaintext):
	word = []
	plaintext = plaintext.upper()
	for x in plaintext:
		if x == " ":
			word.append("-")
		elif (x in alphabet) == False:
			word.append(x)
		else:
			word.append(e_dict[x])
	str = "".join(word)
	return str

def decode_dictionary(d_dict, ciphertext):
	word = []
	ciphertext = ciphertext.upper()
	for x in ciphertext:
		if x == "-":
			word.append(" ")
		elif (x in alphabet) == False:
			word.append(x)
		else:
			word.append(d_dict[x])
	str = "".join(word)
	return str
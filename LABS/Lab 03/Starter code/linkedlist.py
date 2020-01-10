class LinkedListIter:
  def __init__(self, lst):
    self.L = lst
    self.place = 0
    try:
      x = 0
      while True:
        self.L[x]
        x += 1
    except IndexError:
      self.size = x
  def __next__(self):
    if self.L == None:
      raise StopIteration
    else:
      if self.place >= self.size:
        raise StopIteration
      else:
        self.place += 1
        return self.L[self.place - 1]


class LinkedList:
  def __init__(self, lst=[]):
    self.L = lst
    try:
      x = 0
      while True:
        self.L[x]
        x += 1
    except IndexError:
      self.size = x

  def rev(self):
    x = []
    i = 0
    while i < self.size:
       x.append(self.L[self.size-i-1])
       i += 1
    self.L = x


  def addLast(self, x):
    self.L.append(x)
    self.size += 1

  def addFirst(self, x):
    self.rev()
    self.L.append(x)
    self.size += 1
    self.rev()
    

  def removeFirst(self):
    i = 0
    initial = self.L[self.size - 1]
    while i < self.size - 2:
        self.L[i] = self.L[i + 1]
        i += 1
    self.size -= 1
    self.rev()
    self.L[0] = initial
    self.rev()

  def removeLast(self):
    self.rev()
    self.removeFirst()
    self.rev()

  def addAt(self, idx, x):
    if idx > self.size:
      raise Execption("Invalid Index " + idx)
      return False
    else:
      if self.size == 0:
        self.addFirst(x)
      else:
        i= 0
        while i < self.size - idx:
          y = self.L[idx + i]
          self.L[idx + i] = x
          x = y
          i += 1
        self.addLast(x)
    return True

  def removeAt(self, idx):
    if idx > self.size:
      raise Execption("Invalid Index " + idx)
      return False
    else:
      if self.size == 0:
        self.removeFirst()
      i = 0  
      while i < self.size - idx - 1:
        self.L[idx + i] = self.L[idx + i + 1]
        i += 1
      self.removeLast()
    return True

  def __str__(self):
    if self.size == 0:
      return "[]"
    printStr =""
    x = 0
    while x < self.size:
      printStr += ";"+str(self.L[x])
      x += 1
    printStr += "]"
    printStr = printStr[1:]
    printStr = "[" + printStr
    return printStr
  
  def __contains__ (self, x):
    i = 0
    while i < self.size:
      if self.L[i] == x:
        return True
      i += 1
    return False

  def __setitem__(self, idx, x):
    if idx >= self.size:
      raise Execption("Invalid Index " + idx)
    else:
      self.L[idx] = x

  def __getitem__(self, idx):
    if idx >= self.size:
      raise Execption("Invalid Index " + idx)
    else:
      return self.L[idx]
  
  def __iter__(self):
    return LinkedListIter(self.L)

  def __len__(self):
    return self.size
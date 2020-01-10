## Part 1
class BinaryTree:
    def __init__(self, spec):
        if type(spec) is tuple or type(spec) is list:
            self.data = spec[0]
            if len(spec) == 1:
                self.leftChild = None
                self.rightChild = None
            elif len(spec) == 2:
                self.leftChild = BinaryTree(spec[1])
                self.rightChild = None
            else:
                self.leftChild = BinaryTree(spec[1])
                self.rightChild = BinaryTree(spec[2])
        else:
            self.data = spec
            self.leftChild = None
            self.rightChild = None

    def printpreorder(self):
        print(self.data)
        if self.leftChild != None:
            self.leftChild.printpreorder()
        if self.rightChild != None:
            self.rightChild.printpreorder()

        
class Tree:
    def __init__(self, spec):
        self.temporary = spec
        if type(spec) is tuple or type(spec) is list:
            self.data = spec[0]
            self.children = [Tree(subSpec) for subSpec in spec[1:]]
        else:
            self.data = spec
            self.children = []
    
    def printpreorder(self): 
        print(self.data) 
        for child in self.children: 
            child.printpreorder()

    ## Part 2
    def helper(self, counter):
        pass

    #def printbookcontent(self, counter = 0, chapter = 1):
    #    if self.data[1] == 0:
    #        print("Book title: " + self.data[0])
    #    for child in self.children:
    #        print(str(chapter + counter) +" "+ str(child.data[0]) + ", Page " + str(child.data[1]))
    #        if child.children != []:
    #            child.printbookcontent(counter+0.1, chapter)
    #            chapter += 1
    #        else:
    #            child.printbookcontent(counter, chapter)
    #            counter += 0.1

    def printbookcontent(self):
        chapter = 0
        counter = 0
        for child in self.temporary:
            if type(child[0]) is tuple or type(child[0]) is list:
                subChapter = 0.1
                innerCount = 0
                for section in child:
                    if innerCount == 0:
                        print(str(chapter) + " " + section[0] + ", Page " + str(section[1]))
                        innerCount += 1
                        counter += 1
                    else:
                        subName = section[0]
                        print(str(chapter+subChapter) + " " + subName[0] + ", Page " + str(subName[1]))
                        subChapter += 0.1
                        innerCount += 1
                        counter +=1
                chapter += 1
            else:
                if child[1] == 0:
                    print("Book title: " + child[0])
                else:
                    print(str(chapter) + " " + child[0] + ", Page " + str(child[1]))
                chapter += 1
                counter += 1
    
    ## Part 3
    def computespace(self):
        counter = 0
        for child in self.children:
            if child.children != [] and child.data[1] == None:
                child.computespace()
                counter += child.data[1]
            else:
                counter += child.data[1]
        self.data = (self.data[0], counter) 
    
    def printExpr(self): 
        sOut = ""
        if len(self.children) > 0:
            sOut += '(' + self.children[0].printExpr() + ')'
        sOut += str(self.data)
        if len(self.children) > 1:
            sOut += '(' + self.children[1].printExpr() + ')' 
        return sOut
    
    def computeValue(self): 
        childValues = [x.computeValue() for x in self.children]
        return value(self.data, childValues)
    
    def compute(self, evalFunc): 
        childValues = [x.compute(evalFunc) for x in self.children]
        return evalFunc(self.data, childValues)


## Part 4
def value(data, values):
    if type(data) is int and values == []:
        return float(data)
    elif data == 'sum':
        return sum(values)
    elif data == '+':
        return values[0] + values[1]
    elif data == '-':
        return values[0] - values[1]
    elif data == '*':
        return values[0] * values[1]
    elif data == '/':
        return values[0] / values[1]
    elif data == 'min':
        return min(values)
    elif data == 'max':
        return max(values)
    elif data == 'avg':
        return sum(values) / len(values)
    

## Part 5
def spaceusage(data, values):
    if data [1] != None:
        return data[1]
    x = 0
    for value in values:
        x += value
    return x




#testing

#Tbook = [('Make Money Fast!', 0), [('Motivations', 2), [('Greed', 5)],
#[('Avidity', 10)]], [('Methods', 15), [('Stock Fraud', 20)],
#[('Ponzi Scheme', 25)], [('Bank Robbery', 30)]], [('References', 40)]]
#treeBook = Tree(Tbook)
#print("Calling printbookcontent method:")
#treeBook.printbookcontent()

#Tfile = [('CSE1010/', None), [('Section 1', None), [('HWs/', None),
#[('hw1.doc', 5)], [('hw2.doc', 15)]], [('LABs/', None), [('lab1.py', 7)],
#[('lab2.py', 10)], [('lab3.py', 10)]]], [('Section 2', None),
#[('HWs/', None), [('hw1.doc', 5)], [('hw2.doc', 18)]], [('LABs/', None),
#[('lab1.py', 6)], [('lab2.py', 10)], [('lab3.py', 14)]]],
#[('ToDoList.txt', 20)]]
#treeFile = Tree(Tfile)
#print("Original File System Tree:")
#treeFile.printpreorder()
#print("\nComputing Space...\n")
#treeFile.computespace()
#print("File System Tree After Computing Space")
#treeFile.printpreorder()


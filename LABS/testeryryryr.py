class DoublyyyLinkedList:
    class _Node:
        def __init__(self, value, prev = None, next = None):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, L = None):
        self._head = None
        self._tail = None
        self._nodeCount = 0
        if L:
            if isinstance(L, list):
                for x in L:
                    self.addLast(x)
            else:
                for x in L.split():
                    self.addLast(x)

    def addFirst(self, item):
        if self._nodeCount == 0:
            newNode = DoublyyyLinkedList._Node(item)
            self._head = newNode
            self._tail = newNode
            self._nodeCount += 1
        else:
            oldNode = self._head
            newNode = DoublyyyLinkedList._Node(item, None, oldNode)
            oldNode.prev = newNode
            self._head = newNode
            self._nodeCount += 1

    def addLast(self, item):
        if self._nodeCount == 0:
            self.addFirst(item)
        else:
            oldNode = self._tail
            newNode = DoublyyyLinkedList._Node(item, oldNode, None)
            oldNode.next = newNode
            self._tail = newNode
            self._nodeCount += 1

    def removeFirst(self):
        if len(self) == 1:
            removedNode = self._head
            self._head = None
            self._tail = None
            self._nodeCount = 0
            return removedNode.value
        else:
            removedNode = self._head
            self._head = self._head.next
            self._head.prev = None
            self._nodeCount -= 1
            return removedNode.value

    def removeLast(self):
        if len(self) == 1:
            return self.removeFirst()
        else:
            removedNode = self._tail
            self._tail = self._tail.prev
            self._tail.next = None
            self._nodeCount -= 1
            return removedNode.value

    def appendTop(self, other):
        other._tail.next = self._head
        self._head.prev = other._tail
        self._head = other._head
        self._nodeCount += len(other)
        other._tail = None
        other._head = None
        other._nodeCount = 0

    def appendBottom(self, other):
        other._head.prev = self._tail
        self._tail.next = other._head
        self._tail = other._tail
        self._nodeCount += len(other)
        other._tail = None
        other._head = None
        other._nodeCount = 0

    def __str__(self):
        x = self._head
        output = "["
        while x != None:
            output += str(x.value) + ";"
            x = x.next
        if len(output) > 1:
            output = output[:(len(output) - 1)]
        output += "]"
        return output

    def __len__(self):
        return self._nodeCount


class DeckOfCards(DoublyyyLinkedList):
    
    def addTop(self, item):
        self.addFirst(item)

    def addBottom(self, item):
        self.addLast(item)

    def dealTop(self):
        return self.removeFirst()

    def dealBottom(self):
        return self.removeLast()

    def addPileTop(self, pile):
        self.appendTop(pile)

    def addPileBottom(self, pile):
        self.appendBottom(pile)

    def deal(self, nplayers, ncards = None):
        playerList = []
        for x in range(nplayers):
            playerList.append(DeckOfCards())
        if ncards:
            innerCount = 0
            for x in range(ncards):
                if innerCount == len(playerList):
                    innerCount = 0
                playerList[innerCount].addTop(self.dealTop())
                innerCount += 1
        else:
            innerCount = 0
            for x in range(len(self)):
                if innerCount == len(playerList):
                    innerCount = 0
                playerList[innerCount].addTop(self.dealTop())
                innerCount += 1
        return playerList

x = DoublyyyLinkedList([1,2,3,4,5])
print(x)
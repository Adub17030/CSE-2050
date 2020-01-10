class ListNode:
    def __init__(self, value, prev = None, next = None):
        self.value = int(value)
        self.prev = prev
        self.next = next
        if prev is not None:
            self.prev.next = self
        if next is not None:
            self.next.prev = self

class DoublyLinkedList:
    def __init__(self, string = ''):
        self.head = None
        self.tail = None
        self._length = 0
        self.isReversed = False
        if len(string) != 0:
            for i in range(len(string)):
                self.addLast(string[i])
        
        if self.head is not None:
            while self.head.value == 0:
                zeroNode = self.head
                self.head = self.head.next
                zeroNode.next = None
                self.prev = None

    def addFirst(self, item):
        if self.isReversed:
            if self._length == 0:
                newNode = ListNode(item)
                self.head = newNode
                self.tail = newNode
                self._length += 1
            else:
                oldNode = self.head
                newNode = ListNode(item, oldNode, None)
                oldNode.next = newNode
                self.head = newNode
                self._length += 1
        else:
            if self._length == 0:
                newNode = ListNode(item)
                self.head = newNode
                self.tail = newNode
                self._length += 1
            else:
                oldNode = self.head
                newNode = ListNode(item, None, oldNode)
                oldNode.prev = newNode
                self.head = newNode
                self._length += 1
        
    def addLast(self, item):
        if self.isReversed:
            if self._length == 0:
                self.addFirst(item)
            else:
                oldNode = self.tail
                newNode = ListNode(item, None, oldNode)
                oldNode.prev = newNode
                self.tail = newNode
                self._length += 1
        else:
            if self._length == 0:
                self.addFirst(item)
            else:
                oldNode = self.tail
                newNode = ListNode(item, oldNode, None)
                oldNode.next = newNode
                self.tail = newNode
                self._length += 1

    def reverse(self):
        reference = self.tail
        curerntHead = self.head
        self.head = self.tail
        self.tail = curerntHead
        while reference != None:
            currentNext = reference.next
            reference.next = reference.prev
            reference.prev = currentNext
            reference = reference.next

    def fastReverse(self):
        if self.isReversed == False:
            self.isReversed = True
        else:
            self.isReversed = False
        curerntHead = self.head
        self.head = self.tail
        self.tail = curerntHead

    def __str__(self):
        if self.isReversed:
            output = "{"
            reference = self.head
            while reference != None:
                output += str(reference.value) + ";"
                reference = reference.prev
            return output +"}"
        else:
            output = "{"
            reference = self.head
            while reference != None:
                output += str(reference.value) + ";"
                reference = reference.next
            return output + "}"
        
    
    def __len__(self):
        return self._length

def sumlinkednumbers(dll1, dll2):
    curl1 = dll1.tail
    curl2 = dll2.tail
    carry = 0
    result = DoublyLinkedList()
    while curl1!= None and curl2 != None:
        x = (curl1.value + curl2.value + carry) % 10
        result.addFirst(x)
        carry = (curl1.value + curl2.value + carry) // 10
        
        if dll1.isReversed:
            curl1 = curl1.next
        else:
            curl1 = curl1.prev
        if dll2.isReversed:
            curl2 = curl2.next
        else:
            curl2 = curl2.prev
    if curl2 == None:
        while curl1!= None:
            x = (curl1.value + carry) % 10
            result.addFirst(x)
            carry = (curl1.value + carry) // 10
            if dll1.isReversed:
                curl1 = curl1.next
            else:
                curl1 = curl1.prev
    else:
        while curl2!= None:
            x = (curl2.value + carry) % 10
            result.addFirst(x)
            carry = (curl2.value + carry) // 10
            if dll2.isReversed:
                curl2 = curl2.next
            else:
                curl2 = curl2.prev
    #the list has been made, but it may have zeros in the beginning
    while result.head.value == 0:
        zeroNode = result.head
        result.head = result.head.next
        zeroNode.next = None
        result.prev = None

    return result
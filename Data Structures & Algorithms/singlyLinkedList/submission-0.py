class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        idx_count = 0
        curr = self.head

        while curr != None:
            if idx_count == index:
                return curr.val
            idx_count += 1
            curr = curr.next
        return -1 

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def remove(self, index: int) -> bool:
        idx_count = 0
        curr, prev = self.head, None
        while curr != None:
            if idx_count == index:
                if curr == self.head:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                return True
            idx_count += 1
            prev = curr
            curr = curr.next
        return False  

    def getValues(self) -> List[int]:
        curr = self.head
        linked_list = []

        if self.head == None:
            return []

        while curr != None:
            linked_list.append(curr.val)
            curr = curr.next
        return linked_list


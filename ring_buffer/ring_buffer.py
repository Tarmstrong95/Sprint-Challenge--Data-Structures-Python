from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):#O(n)
        count = 1
        curr = self.storage.head
        if curr is not None:
            while curr.next:
                if curr.value == self.current:
                    break
                count += 1
                curr = curr.next
            if count == self.capacity:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
            else:
                if curr.next is not None:
                    curr.next.value = item
                else:
                    self.storage.add_to_tail(item)
        else:
            # if no head
            self.storage.add_to_head(item)
        self.current = item

    def get(self): #O(n)
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        curr = self.storage.head
        while curr:
            if curr.value:
                list_buffer_contents.append(curr.value)
            curr = curr.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------

# THE ADVANTAGE OF USING AN ARRAY IS I CAN USE THE INDEX VALUE TO UPDATE THE ARRAY IN CONSTANT TIME
# IF THE TEST DIDNT REQUIRE THE INITIAL ARRAY TO BE SET WITH *CAPACITY* SPACES, THEN I COULD ALSO *GET* THE 
# ITEMS FROM THE ARRAY IN CONSTANT TIME AS WELL, INSTEAD OF LOOPING TO FIND ONLY NON-NONE VALUES FOR 
# IF THE ARRAY IS SMALLER THAN THE CAPACITY
class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = [self.current]*self.capacity

    def append(self, item):
        if self.current is None:
            self.storage[0] = item
        else:
            i = self.storage.index(self.current)
            if i < len(self.storage)-1:
                self.storage[i+1] = item
            else:
                self.storage[0] = item
        self.current = item


    def get(self):
        tmp = []
        for i in self.storage:
            if i is not None:
                tmp.append(i)
        return tmp



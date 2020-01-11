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


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass



class Node:
    def __init__(self, value, child):
        self.value = value
        self.child = child


class LinkedList:
    def __init__(self, list):
        self.head = None

        list_len = len(list)
        for ind in range(list_len):
            ind = list_len - ind - 1
            value = list[ind]
            self.head = Node(value, self.head)

    def nth_from_head(self, n):
        new_ll = LinkedList([])
        new_ll.head = head_ptr_e = self.head

        ind = 0
        while head_ptr_e:
            head_ptr_e = head_ptr_e.child

            if ind > n:
                new_ll.head = new_ll.head.child

            ind += 1

        return new_ll

    def to_list(self):
        array = []

        head_ptr = self.head
        while head_ptr:
            array.append(head_ptr.value)
            head_ptr = head_ptr.child

        return array

from linked_list import LinkedList

if __name__ == '__main__':
    ll = LinkedList([5, 4, 3, 2, 1])

    ll2 = ll.nth_from_head(2)
    print(ll2.to_list())

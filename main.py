from binary_search_tree import BTNode

if __name__ == '__main__':
    tree = BTNode(4,
                  BTNode(1,
                         BTNode(0),
                         BTNode(2, BTNode(1))),
                  BTNode(5,
                         BTNode(3),
                         BTNode(6)))


    def display(tree_ptr, prev_nodes):
        if tree_ptr:
            prev_nodes = prev_nodes.copy() + [tree_ptr.value]

            if tree_ptr.right:
                display(tree_ptr.right, prev_nodes)
            if tree_ptr.left:
                display(tree_ptr.left, prev_nodes)

            if not (tree_ptr.right and tree_ptr.left):
                print(prev_nodes)

    display(tree, [])

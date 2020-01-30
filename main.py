from binary_tree import BTNode

if __name__ == '__main__':
    tree = BTNode(5,
                  BTNode(1,
                         BTNode(3,
                                BTNode(6),
                                BTNode(7)),
                         BTNode(8)),
                  BTNode(4,
                         BTNode(9),
                         BTNode(2)))


    def set_paths(tree_ptr, prev_nodes, paths):
        if not tree_ptr:
            return

        prev_nodes = prev_nodes.copy() + [tree_ptr.value]

        if tree_ptr.right:
            set_paths(tree_ptr.right, prev_nodes, paths)
        if tree_ptr.left:
            set_paths(tree_ptr.left, prev_nodes, paths)

        if not (tree_ptr.right and tree_ptr.left):
            paths.append(prev_nodes)


    def lca(num1, num2):
        paths = []
        set_paths(tree, [], paths)

        path1 = list(filter(lambda path: num1 in path, paths))
        path2 = list(filter(lambda path: num2 in path, paths))

        if not (len(path1) and len(path2)):
            return None
        else:
            path1, path2 = path1[0], path2[0]

            # if len(path1) == len(path2):
            #     return path1[0]

        common = list(filter(lambda n1: n1 in path2, path1))
        if not len(common):
            return None

        return common


    print(lca(2, 4))

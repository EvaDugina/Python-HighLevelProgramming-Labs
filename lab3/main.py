from Tree import Tree

if __name__ == '__main__':

    #      3
    #   0     4
    # 1   2     6

    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(6)
    tree.add(2)
    tree.add(1)

    for i in tree:
        print(i)

    # tree.view_nodes_from_small()
    # print(tree.find(3).v)
    # print(tree.find(10))
    # tree.delete_tree()
    # tree.view_tree()



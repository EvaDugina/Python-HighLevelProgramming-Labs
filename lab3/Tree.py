from Node import Node


class Tree:
    root = None
    listOfNode = list()

    def __str__(self):
        return str(self.root)

    def __iter__(self):
        if self.root:
            yield from self._view_tree(self.root)

    def get_root(self):
        return self.root

    def add(self, val):
        if not self.root:
            self.root = Node(val)
            self.listOfNode.append(self.root)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.value:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = Node(val)
                self.listOfNode.append(node.left)
        else:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = Node(val)
                self.listOfNode.append(node.right)

    def find(self, val):
        if self.root:
            return self._find(val, self.root)

    def _find(self, val, node):
        if val == node.value:
            return node
        elif val < node.value and node.left:
            return self._find(val, node.left)
        elif val > node.value and node.right:
            return self._find(val, node.right)

    def delete_tree(self):
        if self.root:
            self.root = None

    def _view_tree(self, node):
        if node is None:
            return
        if node.left:
            yield from self._view_tree(node.left)

        yield node.value

        if node.right:
            yield from self._view_tree(node.right)

    def view_nodes_from_small(self):
        from_small_list_nums = []
        [from_small_list_nums.append(n.value) for n in self.listOfNode]
        return print(sorted(from_small_list_nums))
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

        self.size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)

            if result:
                return result.payload

        return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True

        return False

    def __delitem__(self, key):
        self.delete(key)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)

            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, node):
        if node.is_leaf():
            if node == node.parent.left_child:
                node.parent.left_child = None
            else:
                node.parent.right_child = None

        elif node.has_any_children() and not node.has_both_children():
            if node.has_left_child():
                if node.is_left_child():
                    node.left_child.parent = node.parent
                    node.parent.left_child = node.left_child
                elif node.is_right_child():
                    node.left_child.parent = node.parent
                    node.parent.right_child = node.left_child
                else:
                    key, payload, left_child, right_child = node.left_child
                    node.replace_node_data(key, payload, left_child, right_child)
            else:
                if node.is_left_child():
                    node.right_child.parent = node.parent
                    node.parent.left_child = node.right_child
                elif node.is_right_child():
                    node.right_child.parent = node.parent
                    node.parent.right_child = node.right_child
                else:
                    key, payload, left_child, right_child = node.right_child
                    node.replace_node_data(key, payload, left_child, right_child)
        elif node.has_both_children():
            successor = node.find_successor()
            successor.splice_out()
            node.key = successor.key
            node.payload = successor.payload

    def print_in_line(self):
        alist = []
        for node in self:
            alist.append(node)

        print(alist)

    def print_tree(self):
        depth = self.tree_depth()
        width = 2 ** depth
        print('depth=', depth)
        print('width=', width)
        current_level = [self.root]

        while current_level and depth > 0:
            next_level = []
            pad = int(width / len(current_level))
            for node in current_level:
                print(just(node.key, int(pad - 1)), end="")

                if node:
                    if node.has_left_child():
                        next_level.append(node.left_child)
                    else:
                        next_level.append(TreeNode('--', '--'))
                    if node.has_right_child():
                        next_level.append(node.right_child)
                    else:
                        next_level.append(TreeNode('--', '--'))
                else:
                    next_level.append(TreeNode('--', '--'))
                    next_level.append(TreeNode('--', '--'))

            depth -= 1

            print()
            current_level = next_level

    def tree_depth(self):
        def depth(node):
            if not node:
                return 0

            lDepth = depth(node.left_child)
            rDepth = depth(node.right_child)

            return max(lDepth, rDepth) + 1

        return depth(self.root)

    def _print_tree(self, node, just):
        print(str.ljust(str(node.key), just))

        if node.has_left_child():
            self._print_tree(node.left_child, just - 2)

        if node.has_right_child():
            self._print_tree(node.right_child, just + 2)


def just(value, pad):
    return (' ' * pad) + str.ljust(str(value), 2) + (' ' * pad)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc

        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        successor = None

        if self.has_right_child():
            successor = self.right_child.find_min()
        elif self.parent:
            if self.is_left_child():
                successor = self.parent
            else:
                self.parent.right_child = None
                successor = self.parent.find_successor()
                self.parent.right_child = self

        return successor

    def find_min(self):
        node = self

        while node.has_left_child():
            node = node.left_child

        return node

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None

        elif self.has_any_children():
            if self.has_left_child():

                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent

            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.left_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem

            yield self.key

            if self.has_right_child():
                for elem in self.right_child:
                    yield elem


tree = BinarySearchTree()

tree[27] = 27
tree[34] = 34
tree[30] = 30
tree[23] = 23
tree[4] = 4
tree[67] = 67
tree[19] = 19
tree[11] = 11

tree.print_in_line()
tree.print_tree()

tree.delete(34)
tree.print_tree()
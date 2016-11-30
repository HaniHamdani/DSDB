class Node:

    def __init__(self, val, left=None, right=None):
        self.left = left  # is a Node
        self.right = right  # is a Node
        self.value = val

    def __repr__(self):
        return "value = " + str(self.value)

# ABR :
# left.val <= val <= right.val


class Tree:

    __nodes_count = 0

    def __init__(self, node):
        self.root = node
        if node is not None:
            self.__nodes_count += 1

    def add(self, val):
        """add a node with a value = val in the tree"""
        if val is None:
            return
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            self.__nodes_count += 1
        else:
            parent, x = None, self.root
            while x is not None:
                parent = x
                if val <= x.value:
                    x = x.left
                elif val > x.value:
                    x = x.right
            if val <= parent.value:
                parent.left = new_node
            else:
                parent.right = new_node
            self.__nodes_count += 1

    @property
    def nodes_count(self):
        return self.__nodes_count

    def __repr__(self):
        ch = "root's left "
        ch += repr(self.root.left) + ", root's "
        ch += repr(self.root) + ", root's right "
        ch += repr(self.root.right)
        return ch


class ABR:

    def __init__(self, node, val):
        self.__node = node
        self.__value = val

    def run(self):
        """search val in the tree with a root == node"""
        x = self.__node
        while x is not None:
            if self.__value < x.value:
                x = x.left
            elif self.__value > x.value:
                x = x.right
            else:
                return True
        return False


class Test:

    def __init__(self):
        self.node1 = Node(5)
        self.tree1 = Tree(self.node1)
        self.tree1.add(None)
        self.tree2 = Tree(None)
        self.abr = ABR(self.node1, 10)

    def get_classes(self):
        """return list of implemented classes"""
        list_of_classes = [
            self.node1.__class__,
            self.tree1.__class__,
            self.abr.__class__]
        return list_of_classes

    def run(self):
        """run different tests to verify our implementation"""
        print self.node1
        self.tree2.add(self.node1)
        print self.node1.__class__
        print self.abr.run(), self.tree1.nodes_count
        list_of_values = [15, 2, 7, 10, 9, 12]
        [self.tree1.add(n) for n in list_of_values]
        print self.tree1
        print self.abr.run(), self.tree1.nodes_count
        print self.get_classes()

if __name__ == '__main__':
    test1 = Test()
    test1.run()

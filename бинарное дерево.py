""" Node is defined as"""
# https://neerc.ifmo.ru/wiki/index.php?title=%D0%94%D0%B5%D1%80%D0%B5%D0%B2%D0%BE_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0,_%D0%BD%D0%B0%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F_%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None



class Tree:
    root = None

    def __init__(self):
        root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return
        if x < self.root.data:
            if self.root.left is None:
                self.root.left = Tree()
            self.root.left.insert(x)
        else:
            if self.root.right is None:
                self.root.right = Tree()
            self.root.right.insert(x)

    def find(self, x):
        if self.root is None:
            return None
        if x == self.root.data:
            return self.root
        if x < self.root.data:
            if self.root.left is None:
                return None
            return self.root.left.find(x)
        else:
            if self.root.right is None:
                return None
            return self.root.right.find(x)

    def print(self):
        if self.root is None:
            return
        if self.root.left:
            self.root.left.print()
        print(self.root.data)
        if self.root.right:
            self.root.left.print()


T = Tree()
T.insert(2)
T.insert(1)
T.insert(8)
T.insert(3)
T.insert(9)
T.insert(5)
# print(T.find(1))
# print(T.find(5))
T2 = Tree()
T2.find(1)
T.print()
T2.print()

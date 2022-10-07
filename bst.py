
class SortTree:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    def insert_val(self, _value):
        if _value < self.value:
            if self.left is None:
                self.left = SortTree(_value)
            else:
                self.left.insert_val(_value)
        else:
            if self.right is None:
                self.right = SortTree(_value)
            else:
                self.right.insert_val(_value)

    # @classmethod
    # def display(cls, _node):
    #     return list(filter(None, \
    #         [i for b in [cls.display(_node.left) if isinstance(_node.left, SortTree) else [getattr(_node.left, 'value', None)], [_node.value], cls.display(_node.right) if isinstance(_node.right, SortTree) else [getattr(_node.right, 'value', None)]] for i in b]))

    @classmethod
    def display(cls, _node):
        return list(filter(None,
                           [i for b in [cls.display(_node.left) if _node.left is not None else [getattr(_node.left, 'value', None)], [_node.value], cls.display(_node.right) if _node.right is not None else [getattr(_node.right, 'value', None)]] for i in b]))

    # l = [i for i in list/tuple/dict] #
    # este <=>
    # l = []
    # for i in list:
    #     l.append(i)


if __name__ == "__main__":
    tree = SortTree(4)
    for i in [5, 3, 1, 2, 8, 7, 4]:
        tree.insert_val(i)

    print(SortTree.display(tree))

class TreeNode():
    def __init__(self, id, value='', parent=None, children=[], root=None, height=0):
        self.id = id
        self.value = value
        self.parent = parent
        self.children = children
        self.root = root
        self.height = height

    def get_id(self):
        return self._id

    def set_id(self, id):
        # chek id
        self._id = id

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def get_children(self):
        return self._children

    def set_children(self, children):
        self._children = children

    def get_root(self):
        return self._root

    def set_root(self, root):
        self._root = root

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    id = property(get_id, set_id)
    value = property(get_value, set_value)
    parent = property(get_parent, set_parent)
    children = property(get_children, set_children)
    root = property(get_root, set_root)
    height = property(get_height, set_height)


class TreeNode():
    def __init__(self, id, value='', parent=None, children=[], root=None, height=0):
        self.id = id
        self.value = value
        self.parent = parent
        self.children = children
        self.root = root
        self.height = height

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        # chek id
        self.__id = id

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_root(self):
        return self.root

    def get_height(self):
        return self.height

    def set_paren(self, parent):
        self.parent = parent

    def set_children(self, children):
        self.children = children

    def set_root(self, root):
        self.root = root

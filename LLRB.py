RED = True
BLACK = False

class LLRBNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = RED

class LLRB:
    def __init__(self):
        self.root = None

    def is_red(self, node):
        if node is None:
            return False
        return node.color == RED

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x

    def flip_colors(self, h):
        h.color = RED
        if h.left:
            h.left.color = BLACK
        if h.right:
            h.right.color = BLACK

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.root.color = BLACK

    def _insert(self, h, key, value):
        if h is None:
            return LLRBNode(key, value)

        if key < h.key:
            h.left = self._insert(h.left, key, value)
        elif key > h.key:
            h.right = self._insert(h.right, key, value)
        else:
            h.value = value

        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)

        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)

        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)

        return h

    def get(self, key):
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def contains(self, key):
        return self.get(key) is not None
    
    def inorder(self, node=None, result=None):
        if result is None:
            result = []

        if node is None:
            node = self.root

        if node is None:
            return result

        if node.left:
            self.inorder(node.left, result)

        if node.value is not None:
            result.append((node.key, node.value))

        if node.right:
            self.inorder(node.right, result)

        return result



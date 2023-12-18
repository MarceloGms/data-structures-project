def inp():
    str = input().split(" ")

    if len(str) == 1:
        comando = str[0]
        return comando, None

    elif len(str) == 2:
        comando = str[0]
        topico = str[1]
        return comando, topico
    
class Topico:
    def __init__(self, topic, cnt):
        self.topic = topic
        self.cnt = int(cnt)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Splay:
    def __init__(self):
        self.root = None

    def zig(self, node):
        parent = node.parent
        grandparent = parent.parent

        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node

        if parent.left == node:
            parent.left = node.right
            if node.right is not None:
                node.right.parent = parent

            node.right = parent
        else:
            parent.right = node.left
            if node.left is not None:
                node.left.parent = parent

            node.left = parent

        node.parent = grandparent
        parent.parent = node

    def splay(self, node):
        while node.parent is not None:
            parent = node.parent
            grandparent = parent.parent

            if grandparent is None:
                self.zig(node)
            elif (grandparent.left == parent) == (parent.left == node):
                self.zig(parent)
                self.zig(node)
            else:
                self.zig(node)
                self.zig(node)

        self.root = node

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return self.root

        node = self.root
        while node is not None:
            if value.topic == node.value.topic:
                return node

            if value.topic < node.value.topic:
                if node.left is None:
                    node.left = Node(value)
                    node.left.parent = node
                    self.splay(node.left)
                    return node.left

                node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    node.right.parent = node
                    self.splay(node.right)
                    return node.right

                node = node.right

    def search(self, topico):
        node = self.root
        while node is not None:
            if topico == node.value.topic:
                self.splay(node)
                return node.value

            if topico < node.value.topic:
                if node.left is None:
                    self.splay(node)
                    return None

                node = node.left
            else:
                if node.right is None:
                    self.splay(node)
                    return None

                node = node.right
                
    def list(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            self.list(node.left)

        print(node.value.topic + " " + str(node.value.cnt))

        if node.right:
            self.list(node.right)

    
tree = None

while True:
    comando = ""
    topico = ""

    comando, topico = inp()

    temp = Topico

    if comando == "ADD_SUBJECT":
        if tree is None:
            tree = Splay()
            tree.insert(Topico(topico, 1))
            print("REGISTADO")

        else:
            temp = tree.search(topico)
            if temp is not None:
                temp.cnt += 1
                print("REGISTADO")
                    
            else:
                temp = Topico(topico, 1)
                tree.insert(temp)
                print("REGISTADO")

    elif comando == "GET_SUBJECT_COUNT":
        if tree is None:
            print("SUBJECT NAO ENCONTRADO")

        else:
            temp = tree.search(topico)
            if temp is not None:
                print(topico + " " + str(temp.cnt))
                
            else:
                print("SUBJECT NAO ENCONTRADO")

    elif comando == "LIST_ALL":
        tree.list()
        print("FIM")

    elif comando == "FIM":
        break

    else: print("COMANDO INVALIDO")
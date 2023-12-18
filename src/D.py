import sys

def inp():
    str = input().split(" ")

    if len(str) == 1:
        comando = str[0]
        return comando, None, None

    elif len(str) == 2:
        comando = str[0]
        user_name = str[1]
        return comando, user_name, None

    elif len(str) == 3:
        comando = str[0]
        user_name = str[1]
        plano = str[2]
        if plano in ["FREE", "BASIC", "PREMIUM"]:
            return comando, user_name, plano
        else:
            sys.exit("Plano inválido! (FREE, BASIC, PREMIUM)")

class User:
    def __init__(self, username, plan):
        self.username = username
        self.plan = plan

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if node is None:
            return Node(value)

        if value.username < node.value.username:
            node.left = self.insert_recursive(node.left, value)
        else:
            node.right = self.insert_recursive(node.right, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1:
            if value.username < node.left.value.username:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if value.username > node.right.value.username:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def get(self, chat_id):
        node = self.root
        while node is not None:
            if chat_id == node.value.username:
                return node.value
            elif chat_id < node.value.username:
                node = node.left
            else:
                node = node.right
        return None

    def delete(self, chat_id):
        self.root = self.delete_recursive(self.root, chat_id)

    def delete_recursive(self, node, chat_id):
        if node is None:
            return None

        if chat_id == node.value.username:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
                temp = self.get_min(node.right)
                node.value = temp.value
                node.right = self.delete_recursive(node.right, temp.value.username)
        elif chat_id < node.value.username:
            node.left = self.delete_recursive(node.left, chat_id)
        else:
            node.right = self.delete_recursive(node.right, chat_id)

        if node is None:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
    
    def rotate_left(self, node):
        new = node.right
        temp = new.left

        new.left = node
        node.right = temp

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new.height = 1 + max(self.get_height(new.left), self.get_height(new.right))

        return new

    def rotate_right(self, node):
        new = node.left
        temp = new.right

        new.right = node
        node.left = temp

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new.height = 1 + max(self.get_height(new.left), self.get_height(new.right))

        return new

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min(node.left)
        
tree = None

while True:
    comando = ""
    user_name = ""
    plano = ""

    comando, user_name, plano = inp()

    temp = User

    if comando == "NEW_USER":
        if tree is None:
            tree = AVL()
            tree.insert(User(user_name, plano))
            print("USER " + user_name + " CRIADO")

        else:
            temp = tree.get(user_name)
            if temp is not None:
                print("USER " + user_name + " JA EXISTE")
                    
            else:
                temp = User(user_name, plano)
                tree.insert(temp)
                print("USER " + user_name + " CRIADO")

    elif comando == "UPDATE_USER":
        if tree is None:
            print("USER NAO ENCONTRADO")

        else:
            temp = tree.get(user_name)
            if temp is not None:
                temp.plan = plano
                print("USER " + user_name + " ATUALIZADO")
                
            else:
                print("USER NAO ENCONTRADO")

    elif comando == "GET_TYPE":
        if tree is None:
            print("USER NAO ENCONTRADO")

        else:
            temp = tree.get(user_name)
            if temp is not None:
                print(temp.plan)
                    
            else:
                print("USER NAO ENCONTRADO")

    elif comando == "DELETE_USER":
        if tree is None:
            print("USER NAO ENCONTRADO")

        else:
            if(tree.get(user_name) is None):
                print("USER NAO ENCONTRADO")
            else:
                tree.delete(user_name)
                print("USER " + str(user_name) + " APAGADO")

    elif comando == "FIM":
        break

    else: print("COMANDO INVALIDO")
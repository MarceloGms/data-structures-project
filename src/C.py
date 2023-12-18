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

class ABP:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            node = self.root
            while True:
                if value.username < node.value.username:
                    if node.left is None:
                        node.left = new_node
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = new_node
                        break
                    else:
                        node = node.right

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
        self.root = self.delete_recursivo(self.root, chat_id)

    def delete_recursivo(self, node, chat_id):
        if node is None:
            return None

        if chat_id == node.value.username:
            # Node nao tem filhos
            if node.left is None and node.right is None:
                return None
            # Node tem 1 filho
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node tem 2 filhos
            else:
                min = node.right
                while min.left is not None:
                    min = min.left
               
                node.value = min.value
                
                node.right = self.delete_recursivo(node.right, min.value.username)

        elif chat_id < node.value.username:
            node.left = self.delete_recursivo(node.left, chat_id)
        else:
            node.right = self.delete_recursivo(node.right, chat_id)

        return node
        
tree = None

while True:
    comando = ""
    user_name = ""
    plano = ""

    comando, user_name, plano = inp()

    temp = User

    if comando == "NEW_USER":
        if tree is None:
            tree = ABP()
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
                print("USER " + str(user_name) + " NAO ENCONTRADO")
            else:
                tree.delete(user_name)
                print("USER " + str(user_name) + " APAGADO")

    elif comando == "FIM":
        break

    else: print("COMANDO INVALIDO")
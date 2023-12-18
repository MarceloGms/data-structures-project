def inp():
    inp_str = input().split(" ")

    if len(inp_str) == 1:
        comando = inp_str[0]
        return comando, None, None, None

    elif len(inp_str) == 2:
        comando = inp_str[0]
        chat_id = int(inp_str[1])
        return comando, chat_id, None, None

    elif len(inp_str) >= 4:
        comando = inp_str[0]
        chat_id = int(inp_str[1])
        user_name = inp_str[2]
        prompt = " ".join(inp_str[3:])
        return comando, chat_id, user_name, prompt
    
class Conversa:
    def __init__(self, chatId, username):
        self.chatId = int(chatId)
        self.username = username
        self.prompts = []

    def add_prompt(self, prompt):
        self.prompts.append(prompt)

    def get_prompt(self):
        return self.prompts
    
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
            current_node = self.root
            while True:
                if value.chatId < current_node.value.chatId:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def get(self, chat_id):
        current_node = self.root
        while current_node is not None:
            if chat_id == current_node.value.chatId:
                return current_node.value
            elif chat_id < current_node.value.chatId:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def delete(self, chat_id):
        self.root = self._delete_recursive(self.root, chat_id)

    def _delete_recursive(self, current_node, chat_id):
        if current_node is None:
            return None

        if chat_id == current_node.value.chatId:
            # Node nao tem filhos
            if current_node.left is None and current_node.right is None:
                return None
            # Node tem 1 filho
            elif current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            # Node tem 2 filhos
            else:
                min_node = current_node.right
                while min_node.left is not None:
                    min_node = min_node.left
               
                current_node.value = min_node.value
                
                current_node.right = self._delete_recursive(current_node.right, min_node.value.chatId)

        elif chat_id < current_node.value.chatId:
            current_node.left = self._delete_recursive(current_node.left, chat_id)
        else:
            current_node.right = self._delete_recursive(current_node.right, chat_id)

        return current_node

    
tree = None

while True:
    comando = ""
    chat_id = ""
    user_name = ""
    prompt = ""

    comando, chat_id, user_name, prompt = inp()

    temp = Conversa

    if comando == "NEW_PROMPT":
        if tree is None:
            tree = ABP()
            tree.insert(Conversa(chat_id, user_name))
            tree.get(chat_id).add_prompt(prompt)
            print("CHAT " + str(chat_id) + " CRIADO")

        else:
            temp = tree.get(chat_id)
            if temp is not None:
                temp.add_prompt(prompt)
                print("CHAT " + str(chat_id) + " ATUALIZADO")
                
            else:
                temp = Conversa(chat_id, user_name)
                temp.add_prompt(prompt)
                tree.insert(temp)
                print("CHAT " + str(chat_id) + " CRIADO")

    elif comando == "GET_CHAT":
        if tree is None:
            print("CHAT " + str(chat_id) + " NAO ENCONTRADO")

        else:
            temp = tree.get(chat_id)
            if temp is not None:
                print(temp.username)
                prompts = temp.get_prompt()
                for prompt in prompts:
                    print(prompt)
                print("FIM")
                
            else:
                print("CHAT " + str(chat_id) + " NAO ENCONTRADO")

    elif comando == "DELETE_CHAT":
        if tree is None:
            print("CHAT " + str(chat_id) + " NAO ENCONTRADO")

        else:
            if(tree.get(chat_id) is None):
                print("CHAT " + str(chat_id) + " NAO ENCONTRADO")
            else:
                tree.delete(chat_id)
                print("CHAT " + str(chat_id) + " APAGADO")

    elif comando == "FIM":
        break

    else: print("COMANDO INVALIDO")
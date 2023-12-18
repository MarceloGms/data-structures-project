def inp():
    str = input().split(" ")

    if len(str) == 1:
        comando = str[0]
        return comando, None, None, None

    elif len(str) == 2:
        comando = str[0]
        chat_id = int(str[1])
        return comando, chat_id, None, None

    elif len(str) >= 4:
        comando = str[0]
        chat_id = int(str[1])
        user_name = str[2]
        prompt = " ".join(str[3:])
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

class VP:
    def __init__(self, value):
        self.left = None 
        self.right = None
        self.parent = None
        self.color = 1  # 1 vermelho, 0 preto
        self.value = value

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, z):
        while z.parent is not None and z.parent.color == 1:
            if z.parent == z.parent.parent.right:
                y = z.parent.parent.left
                if y is not None and y.color == 1:
                    y.color = 0
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rotate_right(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.rotate_left(z.parent.parent)
            else:
                y = z.parent.parent.right
                if y is not None and y.color == 1:
                    y.color = 0
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.rotate_left(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.rotate_right(z.parent.parent)
        self.root.color = 0

    def insert(self, value):
        node = VP(value)
        node.parent = None
        node.value = value
        node.left = None
        node.right = None
        node.color = 1 # 1 vermelho, 0 preto
        y = None
        x = self

        while x != None:
            y = x
            if node.value.chatId < x.value.chatId:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self = node
        elif node.value.chatId < y.value.chatId:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get(self, chat_id):
        if chat_id < self.value.chatId:
            if self.left is None:
                return None
            else:
                return self.left.get(chat_id)

        elif chat_id > self.value.chatId:
            if self.right is None:
                return None
            else:
                return self.right.get(chat_id)
        
        else:
            return self.value
        
    def delete(self, value):
        pass
        
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
            tree = VP(Conversa(chat_id, user_name))
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
            temp = tree.get(chat_id)
            if temp is not None:
                tree.delete(temp)
                print("CHAT " + str(chat_id) + " APAGADO")
        
            else:
                print("CHAT " + str(chat_id) + " NAO ENCONTRADO")

    elif comando == "FIM":
        break

    else: print("COMANDO INVALIDO")
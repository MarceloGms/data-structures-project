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

class ABP:
    def __init__(self, value):
        self.left = None 
        self.right = None
        self.value = value

    def insert(self, value):
        if value.topic < self.value.topic:
            if self.left is None:
                self.left = ABP(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = ABP(value)
            else: 
                self.right.insert(value)

    def get(self, topico):
        if topico < self.value.topic:
            if self.left is None:
                return None
            else:
                return self.left.get(topico)

        elif topico > self.value.topic:
            if self.right is None:
                return None
            else:
                return self.right.get(topico)
        
        else:
            return self.value
        
    def list(self):
        if self.left:
            self.left.list()
        print(self.value.topic + " " + str(self.value.cnt))
        if self.right:
            self.right.list()
    
tree = None

while True:
    comando = ""
    topico = ""

    comando, topico = inp()

    temp = Topico

    if comando == "ADD_SUBJECT":
        if tree is None:
            tree = ABP(Topico(topico, 1))
            print("REGISTADO")

        else:
            temp = tree.get(topico)
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
            temp = tree.get(topico)
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
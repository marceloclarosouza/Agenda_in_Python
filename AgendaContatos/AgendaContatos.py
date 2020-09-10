"""Agenda de contatos usando OOP. Quero armazenar os contatos em uma lista de dicionarios"""

class Agenda():
    def __init__(self):
        self.contacts={}
        self.agenda=[]

    def dicionario(self, name, age, phone, email):
        if name not in self.contacts:
            self.contacts["name"] = name
            self.contacts["age"] = age
            self.contacts["phone"] = phone
            self.contacts["email"] = email
            self.agenda.append(self.contacts)
        else:
            print("Este contato já foi cadastrado no sistema")
         
    #def __str__(self, agenda):
        #print(agenda)

data = Agenda()
insere = True
while insere == True:
    data.dicionario(input("Nome"), input("age"), input("phone"), input("email"))
    retorno = print("Deseja adicionar outro contato? S/N", input())
    insere = (True if retorno == "S" else False)



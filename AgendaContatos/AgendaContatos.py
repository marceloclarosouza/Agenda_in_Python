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
            return self.agenda
        else:
            print("Este contato já foi cadastrado no sistema")

    #def __str__(self, agenda):
        #print(agenda)

data = Agenda()
while = True
    data.dicionario(input(), input(), input(), input())
    data = print('Deseja adicionar outro contato? S ou N', input())
        if data == S:
            return True
        else:
            return False
        
        
    




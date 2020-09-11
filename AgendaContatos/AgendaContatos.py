"""Agenda de contatos usando OOP. Quero armazenar os contatos em uma lista de dicionarios"""

import json

class Agenda():
    def __init__(self):
        self.contacts={}
        self.agenda=[]

    def dicionario(self, name, age="None", phone="None", email="None"):
        #if name not in self.contacts:
            self.contacts["name"] = name
            self.contacts["age"] = age
            self.contacts["phone"] = phone
            self.contacts["email"] = email
            self.agenda.append(self.contacts)
            with open("agenda_dados.txt", "w") as arquivo:
                arquivo.write(json.dumps(self.agenda))
        #else:
            #print("Este contato já foi cadastrado no sistema")


    #def salva_retorna_agenda(self):
        #with open("agenda_dados.txt", "w") as arquivo:
            #arquivo.write(json.dumps(self.agenda))
    def retorna_agenda(self):
        with open("agenda_dados.txt", "r") as arquivo:
            aberto = arquivo.read()
            return aberto
   

data = Agenda()

data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))
data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))
#data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))

print(data.retorna_agenda())

"""Agenda de contatos usando OOP. Quero armazenar os contatos em uma lista de dicionarios"""

import json

class Agenda():
    def __init__(self):
        self.contacts={}
        self.agenda=[]

    def dicionario(self, name, age="None", phone="None", email="None"):
        if name not in self.contacts:
            self.contacts["name"] = name
            self.contacts["age"] = age
            self.contacts["phone"] = phone
            self.contacts["email"] = email
            #self.agenda.append(self.contacts)
        else:
            print("Este contato já foi cadastrado no sistema")
            
            
    def salvar(self):
            with open("agenda_dados.txt", "a") as arquivo:
                #arquivo.write(json.dumps(self.agenda))
                arquivo.write(json.dumps(self.contacts))
                
  
    def retorna_agenda(self):
        with open("agenda_dados.txt", "r") as arquivo:
            aberto = arquivo.read()
            for dic in aberto:
                self.agenda.append(dic)
            data.salvar(self.agenda)    
            return self.agenda
   

data = Agenda()

data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))
data.salvar()
data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))
data.salvar()
#data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))

print(data.retorna_agenda())

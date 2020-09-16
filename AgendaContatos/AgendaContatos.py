"""Agenda de contatos usando OOP. Quero armazenar os contatos em uma lista de dicionarios"""

import json

class Agenda():
    def __init__(self):
        """Inicia a lista e o dicionário utilizados na classe Agenda"""
        self.contacts={}
        self.agenda=[]

    def criar_agenda(self):
        """Cria a agenda de contatos"""#deve ser executada uma única vez
        with open("agenda_dados.txt", "w") as arquivo:
            arquivo.write(json.dumps(""))
        pass


    def dicionario(self, name, age="None", phone="None", email="None"):
        """Adiciona os contatos a agenda"""
        self.contacts["name"] = name
        self.contacts["age"] = age
        self.contacts["phone"] = phone
        self.contacts["email"] = email
        self.agenda.append(self.contacts)
        return self.agenda
    
    def salvar_agenda(self):
        with open("agenda_dados.txt", "a") as arquivo:
            arquivo.write(json.dumps(self.agenda))
            

    def retorna_agenda(self):
        """retorna a aganda"""
        with open("agenda_dados.txt", "r") as arquivo:
            aberto = arquivo.read()
            return aberto


data = Agenda()
data.criar_agenda()

data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))
data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))
data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))

data.salvar_agenda()

print(data.retorna_agenda())

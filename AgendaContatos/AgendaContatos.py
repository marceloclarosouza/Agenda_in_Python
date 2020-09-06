"""Agenda de contatos usando OOP. Quero armazenar os contatos em uma lista de dicionarios"""

class Agenda():
    def __init__(self):
        self.contacts={}
        self.agenda=[]

    def dicionario(self, name, age, phone, email):
        self.contacts["name"] = name
        self.contacts["age"] = age
        self.contacts["phone"] = phone
        self.contacts["email"] = email
        self.agenda.append(self.contacts)

    def __str__(self):
        print(self.agenda)


data = Agenda()
data.dicionario("mcs", 2131, "hlkhlh", "kljlkjl")



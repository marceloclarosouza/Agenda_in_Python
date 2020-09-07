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
        return self.agenda

    #def __str__(self, agenda):
        #print(agenda)

data = Agenda()
print(data.dicionario("mcs", "2131", "hlkhlh", "kljlkjl"))




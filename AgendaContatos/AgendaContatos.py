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

    #def retorna_agenda(self):
        #return self.agenda
    
    def salva_agenda(self):
        with open("agenda_dados.txt", "a") as arquivo:
            arquivo.write(self.agenda)
            return arquivo
        

   

data = Agenda()

data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))
data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))
data.dicionario(input("Nome: "), input("age: "), input("phone: "), input("email: "))

#print(data.retorna_agenda())
print(data.salva_agenda())







class Agenda():
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.agenda = []
        self.contacts = {}

    def dicionario(self, contacts):
        contacts['name'] = self.name
        contacts['age'] = self.age
        contacts['phone'] = self.phone
        contacts['email'] = self.email
        
    def selfagenda(self, agenda):
       self.agenda.append(contacts)
       return self.agenda

    
dados = Agenda("marcelo", "37", 54654654654, "a@a.com.br")

print(dados)


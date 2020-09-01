



class Agenda():
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.agenda = []
        self.contacts = {}

    def dicionario(self):
        self.contacts['name'] = self.name
        self.contacts['age'] = self.age
        self.contacts['phone'] = self.phone
        self.contacts['email'] = self.email
        self.agenda.append(contacts)  
        
    #def selfagenda(self):
        #self.agenda.append(contacts)       

    def __str__(agenda):
        return self.agenda

    
data = Agenda("marcelo", "37", 54654654654, "a@a.com.br")
print(data())


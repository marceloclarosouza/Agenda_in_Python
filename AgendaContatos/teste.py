

def dicionario(name, age, phone, email):
    contacts['name'] = name
    contacts['age'] = age
    contacts['phone'] = phone
    contacts['email'] = email
    agenda.append(contacts)
    return agenda

contacts = {}
agenda = []

contador = 's'

while (contador == 's'):
    dados = dicionario(input("Name "),input('age '), input("phone "), input("email "))
    print('Deseja continuar? S ou N')
    contador = input()
    

print(dados)

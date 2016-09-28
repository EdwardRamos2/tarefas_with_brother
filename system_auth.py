#!/usr/bin/env python
#Autor: Edward Ramos
#Date: 09/28/2016

#Sistema de autenticacao

user = raw_input('Insert you user:  ')
pass1 = raw_input("Insert you pass:  ")

db_user = ['eduardo', 'john', 'yale', 'karla']
db_pass = ['1234','3232','5454','8080']

if user not in db_user or pass1 not in db_pass:
    print("Usuario ou Senha nao corresponde")

elif user in db_user and pass1 in db_pass:
    usuario = db_user.index(user)
    senha = db_pass.index(pass1)
    if usuario == senha:
        print("Usuario e Senha corretos")
    else:
        print("Usuario ou Senha nao corresponde")

#!/usr/bin/env python
print("####################################################################")
print("####################  Autor: Edward Ramos  #########################")
print("####################  Date: 09/26/2016     #########################")
print("####################################################################")
print("####################################################################")

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


        def mochila2():
                if 0 == 0:
                    print("Itens da mochila a serem inseridos:  \n")
                    print("Insert o 1 produto! Categoria higiene:\n")
                    item_1 = str(raw_input("Insert produto!:"))
                if item_1 != 0:
                    print
                    print("(+) Produto inserido com sucesso!\n")
                else:
                    print("Next")

                print("Insert o 2 produto! Categora roupa:\n")
                item_2 = str(raw_input("Insert produto!:\n"))
                if item_2 != 0:
                    print("(+) Produto inserido com sucesso!\n")
                else:
                    print("Next")

                print("Insert o 3 produto! Categoria acessorios:\n")
                item_3 = str(raw_input("Insert produto!:\n"))
                if item_3 != 0:
                    print("(+) Produto inserido com sucesso!\n")
                else:
                    print("Next")

                print("Produtos inseridos na mochila:\n")
                print("CATEGORIA: HIGIENE")
                print(item_1)
                print("")
                print("CATEGORIA: ROUPA")
                print(item_2)
                print("")
                print("CATEGORIA: ACESSORIOS")
                print(item_3)
                print("")


                print("TODOS PRODUTOS INSERIDOS")

        print(mochila2())

        def adicional():
                print("Produtos adicionais:")
                print("Categoria: ALIMENTO - LANCHE\n")

                alimento = str(raw_input("Insert 1 ALIMENTO"))
                if alimento != 0:
                    print("(+) Alimento inserido com sucesso!\n'")
                else:
                    print("Next")

                lanche = str(raw_input("Insert 1 LANCHE"))
                if lanche != 0:
                    print("(+) Lanche insrido com sucesso!\n")
                else:
                    print("Next")

                print("Lanche inserido com sucesso!\n'")

                print("Produtos adicionais inseridos:")
                print("CATEGORIA: ALIMENTO")
                print(alimento)

                print("CATEGORIA: LANCHE")
                print(lanche)
                print("")
                print("PRODUTOS ADICIONAIS INSERIDOS")

        print(adicional())

    else:
        print("Usuario ou Senha nao corresponde")













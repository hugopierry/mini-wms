from time import sleep

usuario = "goku"
senha = "123456"
print("--"*30)


print("Log in e senha:".center(50))
sleep(2)
print("--"*30)
while True:
    cadastrar_usuario =input("Usuário: ")
    cadastrar_senha = input("Senha: ")
    print("--"*30)


    if cadastrar_usuario == usuario and cadastrar_senha == senha:
        print(f"Cadastro encontrado!")
        sleep(2)
        print(f"Bem Vindo!")
        break
    else:
        print("Usuário incorreto")
print("--"*30)
        

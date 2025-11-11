
menu = """
    --- DSA Mini-Projeto 2 - Sistena Bancário Digital---

    1. Adicionar Cliente
    2. Criar Conta
    3. Acessar Conta
    4. Sair
    """
print(menu)

escolha = input("Escolha uma opção: ")

def tipo_escolha(opcao):

    match opcao:
        case '1':
            print("Cliente")
        case '2':
            print("Conta")
        case '3':
            print("Acessar_conta")
        case '4':
            print("Obrigado por usar o nosso sistema. Até logo!")
        case '_': 
            print("Opção invalida. Por favor, tente novamente.")

tipo_escolha(escolha)




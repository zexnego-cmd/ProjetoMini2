
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

#cliente.py
class Cliente:

    def __init__(self, nome:str, cpf:str):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
    def __str__(self):
        return (f"Cliente:{self.nome} (CPF: {self.cpf})")

cli1 = Cliente("Jose", "399.258.258.04")

print(cli1)
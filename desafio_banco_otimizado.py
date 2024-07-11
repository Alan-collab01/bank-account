# Função para realizar um saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
    return saldo, extrato


# Função para realizar um depósito
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


# Função para gerar o extrato
def gerar_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


# Lista para armazenar os usuários cadastrados
usuarios = []

# Lista para armazenar as contas bancárias
contas = []

# Função para cadastrar um usuário
def cadastrar_usuario():
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe o CPF (apenas números): ")
    endereco = input("Informe o endereço (formato: logradouro, nro - bairro - cidade/sigla estado): ")

    cpf_numeros = cpf.replace(".", "").replace("-", "")
    for usuario in usuarios:
        if usuario["cpf"] == cpf_numeros:
            print(f"Já existe um usuário cadastrado com o CPF {cpf}")
            return
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_numeros,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")


# Função para criar uma conta bancária vinculada a um usuário
def criar_conta_bancaria():
    cpf = input("Informe o CPF do usuário para vincular a conta: ")

    # Procurar o usuário pelo CPF na lista de usuários
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break
    
    if usuario_encontrado:
        # Gerar número da conta (sequencial)
        numero_conta = len(contas) + 1
        nova_conta = {
            "agencia": "0001",
            "numero_conta": numero_conta,
            "usuario": usuario_encontrado
        }
        contas.append(nova_conta)
        print(f"Conta bancária criada para {usuario_encontrado['nome']} - Número da conta: {numero_conta}")
    else:
        print(f"Usuário com CPF {cpf} não encontrado.")


# Menu inicial
menu = """

[u] Cadastrar Usuário
[c] Criar Conta Bancária
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do programa
while True:
    opcao = input(menu)

    if opcao == "u":
        cadastrar_usuario()

    elif opcao == "c":
        criar_conta_bancaria()

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

    elif opcao == "e":
        gerar_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

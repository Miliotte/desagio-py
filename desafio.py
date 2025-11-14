# ====== SISTEMA BANCÁRIO ======

menu = """

[1] Criar Usuário
[2] Criar Conta
[3] Depósito
[4] Saque
[5] Extrato
[6] Listar Contas
[0] Sair

=> """

# --------- BANCO DE DADOS EM MEMÓRIA -----------
usuarios = []
contas = []
AGENCIA = "0001"


# --------- FUNÇÕES DO SISTEMA ------------------

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")

    # verifica se já existe
    for u in usuarios:
        if u["cpf"] == cpf:
            print("Usuário já cadastrado!")
            return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (Rua, Número - Bairro - Cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf):
    for u in usuarios:
        if u["cpf"] == cpf:
            return u
    return None


def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if not usuario:
        print("Usuário não encontrado. Crie primeiro o usuário!")
        return

    numero_conta = len(contas) + 1
    conta = {
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "limite": 500,
        "saques": 0,
        "limite_saques": 3
    }

    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {AGENCIA} Conta: {numero_conta}")


def selecionar_conta():
    numero = int(input("Número da conta: "))
    for c in contas:
        if c["numero_conta"] == numero:
            return c
    print("Conta não encontrada!")
    return None


def deposito():
    conta = selecionar_conta()
    if not conta:
        return
    
    valor = float(input("Valor do depósito: "))

    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado!")
    else:
        print("Valor inválido.")


def saque():
    conta = selecionar_conta()
    if not conta:
        return

    valor = float(input("Valor do saque: "))

    if valor <= 0:
        print("Valor inválido.")
        return

    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
    elif valor > conta["limite"]:
        print("Saque excede o limite permitido.")
    elif conta["saques"] >= conta["limite_saques"]:
        print("Limite de saques diário atingido.")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["saques"] += 1
        print("Saque realizado!")


def extrato():
    conta = selecionar_conta()
    if not conta:
        return

    print("\n========== EXTRATO ==========")
    print("Sem movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"Saldo: R$ {conta['saldo']:.2f}")
    print("==============================\n")


def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n======= CONTAS REGISTRADAS =======")
    for c in contas:
        print(f"Agência: {c['agencia']} | Conta: {c['numero_conta']} | Cliente: {c['usuario']['nome']}")
    print("==================================\n")


# ========= LOOP PRINCIPAL DO SISTEMA ==========
while True:
    opcao = input(menu)

    if opcao == "1":
        criar_usuario()

    elif opcao == "2":
        criar_conta()

    elif opcao == "3":
        deposito()

    elif opcao == "4":
        saque()

    elif opcao == "5":
        extrato()

    elif opcao == "6":
        listar_contas()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")

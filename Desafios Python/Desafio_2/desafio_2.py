""" 
    Criando um sistema bancário com Python separando as operações básicas: Depósito, Saque e Extrato em funções 
    Criar duas novas funções para cliente do banco e conta corrente 
"""

# Exibe o menu interativo do banco
def menu():
    return """
    === Bem-vindo ao Banco ===
    [1] Realizar depósitos
    [2] Realizar saques
    [3] Ver extratos
    [4] Criar usuário
    [5] Criar conta corrente
    [6] Sair do sistema
    """

# Cria um novo usuário e o adiciona à lista de usuários
def criar_usuario(usuarios):
    cpf = input("Digite o CPF (apenas números): ")
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite o endereço (logradouro, bairro, cidade/sigla do estado): ")

    # Verifica se o CPF já existe
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Esse CPF já está cadastrado em nosso sistema.")
        return usuarios

    # Criando o dicionário
    usuarios.append({ 'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf,  'endereco': endereco})

    print("Usuário criado com sucesso!")
    return usuarios

# Cria uma conta corrente e vincula ao usuário
def criar_conta_corrente(contas, usuarios):
    cpf = input("Digite o CPF do usuário para vincular a conta (apenas números): ")
    
    if not any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário não encontrado. Por favor, é necessário criar um usuário antes de criar uma conta.")
        return contas

    # Gera um número de conta sequencial
    numero_conta = len(contas) + 1
    
    # Número fixo para agência
    AGENCIA = "0001"
    
    conta = { 'numero_conta': numero_conta, 'agencia': AGENCIA,'cpf_usuario': cpf }

    # Adiciona a conta criada à lista de contas
    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}, Agência: {AGENCIA}")
    return contas

# Realiza o depósito na conta
def deposito(saldo, valor, extrato, contas, usuarios, cpf_usuario, /):

    # Verifica se o usuário tem uma conta
    if not any(conta['cpf_usuario'] == cpf_usuario for conta in contas):
        print("Usuário não possui conta. Crie uma conta antes de realizar depósitos.")
        return saldo, extrato

    if valor <= 0:
        print("Valor incorreto, adicione um valor positivo.")
    else:
        saldo += valor
        conta = next(conta for conta in contas if conta['cpf_usuario'] == cpf_usuario)
        nome_usuario = next(usuario['nome'] for usuario in usuarios if usuario['cpf'] == cpf_usuario)
        extrato += (f"Depósito: R$ {valor:.2f}\n"
                    f"Conta: {conta['numero_conta']} - Agência: {conta['agencia']}\n"
                    f"Nome: {nome_usuario}\n"
                    "\n")
        print("\n Depósito realizado com sucesso!\n")
    
    return saldo, extrato

# Realiza o saque na conta
def saque(*, saldo, valor, extrato, limite, numero_saque, LIMITE_SAQUE, contas, usuarios, cpf_usuario):

    # Verifica se o usuário tem uma conta
    if not any(conta['cpf_usuario'] == cpf_usuario for conta in contas):
        print("Usuário não possui conta. Crie uma conta antes de realizar saques.")
        return saldo, extrato, numero_saque

    if numero_saque >= LIMITE_SAQUE:
        print("Número de saques diários excedido! Tente novamente amanhã.\n")
    
    elif valor > limite:
        print("O limite máximo para saques diários é de R$ 500.00.\n")
    
    elif saldo < valor:
        print("Não foi possível realizar o saque. Saldo insuficiente.\n")
    
    elif valor <= 0:
        print("Valor incorreto, adicione um valor positivo.\n")
        
    else:
        saldo -= valor
        conta = next(conta for conta in contas if conta['cpf_usuario'] == cpf_usuario)
        nome_usuario = next(usuario['nome'] for usuario in usuarios if usuario['cpf'] == cpf_usuario)
        extrato += (f"Saque: R$ {valor:.2f}\n"
                    f"Conta: {conta['numero_conta']} - Agência: {conta['agencia']}\n"
                    f"Nome: {nome_usuario}\n"
                    "\n")
        print("\n Retirada realizada com sucesso!\n")
        numero_saque += 1

    return saldo, extrato, numero_saque

# Exibe o extrato da conta
def extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    """
    print("# Extrato da conta #".center(36, "-"))
    print("\nMovimentações na conta inativas." if not extrato else extrato)
    print(f"\nValor Total em conta: Saldo: R$ {saldo:.2f} \n")
    print("## ## ##".center(36, "-"))

# Função principal que executa o menu e chama as outras funções conforme a opção escolhida
def main():
    # Inicializando variáveis
    saldo = 0
    limite = 500
    extrato_banco = ""
    numero_saque = 0
    LIMITE_SAQUE = 3
    usuarios = []  # Lista para armazenar os usuários
    contas = []    # Lista para armazenar as contas correntes

    while True:
        opcao = input(menu())
        
        # opcao depósito 
        if opcao == "1":
            cpf_usuario = input("Digite o CPF do usuário (apenas números): ")
            cpf_usuario = ''.join(filter(str.isdigit, cpf_usuario))
            saldo, extrato_banco = deposito(
                saldo,
                float(input("Qual a quantia que você deseja depositar? ")),
                extrato_banco,
                contas,
                usuarios,
                cpf_usuario
            )

        # opcao saque
        elif opcao == "2":
            cpf_usuario = input("Digite o CPF do usuário (apenas números): ")
            cpf_usuario = ''.join(filter(str.isdigit, cpf_usuario))
            saldo, extrato_banco, numero_saque = saque(
                saldo=saldo,
                valor=float(input("Qual a quantia que você deseja sacar? ")),
                extrato=extrato_banco,
                limite=limite,
                numero_saque=numero_saque,
                LIMITE_SAQUE=LIMITE_SAQUE,
                contas=contas,
                usuarios=usuarios,
                cpf_usuario=cpf_usuario
            )
        
        # opcao extrato
        elif opcao == "3":
            extrato(saldo, extrato=extrato_banco)
        
        # opcao criar usuario
        elif opcao == "4":
            usuarios = criar_usuario(usuarios)
        
        # opcao criar conta corrente
        elif opcao == "5":
            contas = criar_conta_corrente(contas, usuarios)
        
        #opcao sair do sistema
        elif opcao == "6":
            print("Saindo do sistema. Até breve!")
            break
        
        # Caso o usuário escolha um numero não oferecido no menu 
        else:
            print("Opção inválida. Por favor, selecione novamente a opção desejada.\n")

main()

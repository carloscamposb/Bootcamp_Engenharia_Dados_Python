# Criando um sistema bancário com Python utilizando as operações básicas: Depósito, Saque e Extrato

# Criação do menu interativo
menu = """
       === Bem-vindo ao Banco ===
       [1] Realizar depósitos
       [2] Realizar saques
       [3] Ver extratos
       [4] Sair do sistema
"""

# Inicializando variáveis
saldo = 0
LIMITE = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3 

# Criação de estrutura de repetição 
while True:
    opcao = input(menu)
    
    # Operação de depósito
    if opcao == "1":
        adicao_valor = float(input("Qual a quantia que você deseja depositar? "))
        if adicao_valor <= 0:
            print("Valor incorreto, adicione um valor positivo.")
        else:
            saldo += adicao_valor
            extrato += f"Depósito: R$ {adicao_valor:.2f}"
            print("Depósito realizado com sucesso!\n")

    # Operação de saque 
    elif opcao == "2":
        retirada_valor = float(input("Qual a quantia que você deseja sacar? "))
       
        if numero_saque >= LIMITE_SAQUE:
            print("Número de saques diários excedido! Tente novamente amanhã.\n")
       
        elif retirada_valor > LIMITE:
            print("O limite máximo para saques diários é de R$ 500.00.\n")
        
        elif saldo < retirada_valor:
            print("Não foi possível realizar o saque. Saldo insuficiente.\n")
       
        elif retirada_valor <= 0:
            print("Valor incorreto, adicione um valor positivo.\n")    
            
        else:    
            saldo -= retirada_valor  
            extrato += f"\nSaque: R$ {retirada_valor:.2f}"
            print("Retirada realizada com sucesso!\n")
        
            numero_saque += 1

    # Verificação do extrato 
    elif opcao == "3":
       print("# Extrato da conta #".center(36, "-"))
       print("\n Movimentações na conta inativa." if not extrato else extrato)    
       print(f"\nValor Total em conta: Saldo: R$ {saldo:.2f} \n")
       print("## ## ##".center(36,"-"))
    elif opcao == "4":
        print("Saindo do sistema. Até breve!")
        break    

    # Qualquer opção que não corresponde as opções do Menu
    else:
        print("Opção inválida. Por favor, selecione novamente a opção desejada.\n")


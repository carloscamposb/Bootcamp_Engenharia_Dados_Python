from abc import ABC, abstractmethod 

# Classe base Cliente para gerenciar informações e contas de clientes
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []  # Inicializa a lista de contas como vazia

    def realizar_transacao(self, conta, transacao):
        """Realiza uma transação em uma conta específica"""
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """Adiciona uma conta à lista de contas do cliente"""
        self.contas.append(conta)

# Classe derivada PessoaFisica para clientes do tipo pessoa física
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# Classe base Conta para gerenciar as operações bancárias
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0  # Inicializa o saldo como 0
        self._numero = numero
        self._agencia = "001"  # Código da agência
        self._cliente = cliente
        self._historico = Historico()  # Inicializa o histórico de transações

    @classmethod
    def nova_conta(cls, cliente, numero):
        """Cria uma nova instância de Conta"""
        return cls(numero, cliente)

    @property
    def saldo(self):
        """Retorna o saldo da conta"""
        return self._saldo

    @property
    def numero(self):
        """Retorna o número da conta"""
        return self._numero

    @property
    def agencia(self):
        """Retorna o código da agência"""
        return self._agencia

    @property
    def cliente(self):
        """Retorna o cliente associado à conta"""
        return self._cliente

    @property
    def historico(self):
        """Retorna o histórico de transações da conta"""
        return self._historico

    def sacar(self, valor):
        """Realiza um saque da conta"""
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("""
                    Operação falhou
                   ---------------------
                  Não foi possível realizar o saque. Saldo insuficiente.
                  """)
            return False

        elif valor < 0:
            print("""
                    Operação falhou
                   ---------------------
                  Digite um número válido, positivo.
                  """)
            return False

        else:
            self._saldo -= valor
            print("""
                    Operação bem sucedida
                   ---------------------
                  Saque realizado com sucesso.
                  """)
            return True

    def depositar(self, valor):
        """Realiza um depósito na conta"""
        if valor < 0:
            print("""
                    Operação falhou
                   ---------------------
                  Digite um número válido, positivo.
                  """)
            return False
        else:
            self._saldo += valor
            print("""
                    Operação bem sucedida
                   ---------------------
                  Depósito realizado com sucesso.
                  """)
            return True

# Classe ContaCorrente para contas correntes com limites específicos
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saque

    def sacar(self, valor):
        """Realiza um saque, considerando limites diários"""
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"])

        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("""
                    Operação falhou
                   ---------------------
                    O limite máximo para saques diários é de R$ 500.00!
                  
                  """)
        elif excedeu_saque:
            print("""
                    Operação falhou
                   ---------------------
                    Número de saques diários excedido! Tente novamente amanhã
                  
                  """)
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        """Retorna uma representação da conta corrente"""
        return f"""
                Agência:{self.agencia}
                C/C:{self.numero}
                Titular: {self.cliente.nome}
        """

# Classe Historico para gerenciar o histórico de transações
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        """Retorna a lista de transações"""
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """Adiciona uma transação ao histórico"""
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
        })

# Classe base Transacao para definir a interface de transações
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        """Propriedade abstrata para o valor da transação"""
        pass

    @abstractmethod
    def registrar(self, conta):
        """Método abstrato para registrar a transação em uma conta"""
        pass

# Classe Saque para representar uma transação de saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        """Retorna o valor do saque"""
        return self._valor

    def registrar(self, conta):
        """Registra a transação de saque na conta"""
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Classe Deposito para representar uma transação de depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        """Retorna o valor do depósito"""
        return self._valor

    def registrar(self, conta):
        """Registra a transação de depósito na conta"""
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Função para exibir o menu de opções
def menu():
    return """
    === Bem-vindo ao Banco ===
    [1] Realizar depósitos
    [2] Realizar saques
    [3] Ver extratos
    [4] Criar usuário
    [5] Criar conta corrente
    [6] Listar contas
    [7] Sair do sistema
    """

# Função para filtrar clientes pelo CPF
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# Função para recuperar a conta do cliente
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("""
               Operação falhou!
              -------------------
              O cliente ainda não possui conta no banco!
        """)
        return
    return cliente.contas[0]

# Função para realizar um depósito
def depositar(clientes):
    cpf = input("Informe o seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("""
               Operação falhou!
              -------------------
              CPF não cadastrado. Por favor, cadastre o CPF antes de prosseguir!
        """)
        return

    valor = float(input("Informe o valor que deseja depositar: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

# Função para realizar um saque
def sacar(clientes):
    cpf = input("Informe o seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("""
               Operação falhou!
              -------------------
              CPF não cadastrado. Por favor, cadastre o CPF antes de prosseguir!
        """)
        return

    valor = float(input("Informe o valor que deseja sacar: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

# Função para exibir o extrato da conta
def exibir_extrato(clientes):
    cpf = input("Informe o seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("""
               Operação falhou!
              -------------------
              CPF não cadastrado. Por favor, cadastre o CPF antes de prosseguir!
        """)
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n ========== Extrato ============")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n R$ {transacao['valor']:.2f}"
    print(extrato)
    print(f"\n Saldo:\nR$ {conta.saldo:.2f}")
    print("============================")

# Função para criar uma nova conta corrente
def criar_conta(numero_conta, clientes):
    cpf = input("Informe o seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("""
               Operação falhou!
              -------------------
              CPF não cadastrado. Por favor, cadastre o CPF antes de prosseguir!
        """)
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    cliente.adicionar_conta(conta)
    print("""
            Operação bem sucedida!
           --------------------------
           Conta criada com sucesso.
    """)

# Função para listar todas as contas dos clientes
def listar_contas(clientes):
    for cliente in clientes:
        if cliente.contas:
            print("\n====================================")
            print(f"Nome: {cliente.nome}")
            print(f"CPF: {cliente.cpf}")
            for conta in cliente.contas:
                print(conta)
                print("====================================")

# Função para criar um novo cliente
def criar_cliente(clientes):
    cpf = input("Informe o seu CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("""
               Operação falhou!
              -------------------
              Já existe cliente cadastrado com esse CPF!
        """)
        return

    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, número - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("""
            Operação bem sucedida!
           --------------------------
           Usuário cadastrado com sucesso.
    """)

# Função principal para rodar o sistema bancário
def main():
    clientes = []
    numero_conta = 1

    while True:
        opcao = input(menu())

        if opcao == "1":
            depositar(clientes)
        elif opcao == "2":
            sacar(clientes)
        elif opcao == "3":
            exibir_extrato(clientes)
        elif opcao == "4":
            criar_cliente(clientes)
        elif opcao == "5":
            criar_conta(numero_conta, clientes)
            numero_conta += 1
        elif opcao == "6":
            listar_contas(clientes)
        elif opcao == "7":
            print("""
                   Volte sempre!
                  ----------------
                 Encerrando o sistema.
            """)
            break
        else:
            print("""
                   Operação inválida!
                  ---------------------
                 Selecione uma operação válida!
            """)

main()

## Bootcamp Engenharia de Dados com Python - DIO. NTT DATA

### Projeto desenvolvido durante o desafio: *Otimizando o Sistema Bancário com Funções Python* 🏦 
---

### Linguagem Utilizada:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Proposta:
Neste projeto, refizemos o desafio I de [Sistema Bancário em Python](https://github.com/carloscamposb/Sistema_Bancario_I), colocando as três operações essênciais: **depósito**, **saque** e **extrato** dentro de funções e criando duas novas funções para **criar usuário** e **criar conta corrente**. Com isso foi possível aplicar conhecimentos em programação Python e criar um sistema funcional que simulava as operações bancárias um pouco mais completo. 

### Instruções do desafio:  
> Depósito: 
* Só aceitar do cliente valores positivos;
* Os depósitos devem ser armazenados em uma variável e exibidas no extrato;
* A função depósito deve receber argumentos apenas por posição `positional only` 
* Sugestão de argumentos: `saldo` , `valor` , `extrato`
* Retorno: `saldo` e `extrato`
 
> Saque:
* O sistema deve permitir apenas três saques diários com limite máximo de R$ 500.00 por saque;
* Caso o cliente não tenha saldo em conta suficiente, exibir mensagem informando que não é possível sacar devido à falta de saldo
* Os saques devem ser armazenados em uma variável e exibidos no extrato
* A função saque deve receber argumentos apenas por nome `keyword only`
* Sugestão de argumentos: `saldo` , `valor` , `extrato`, `limite`, `numero_saque` , `LIMITE_SAQUE`
* Retorno: `saldo` e `extrato`

>Extrato:
* Listar todos os depósitos e saques realizados na conta do cliente
* Os valores devem ser escritos utilizando o formato **R$ xxx.xxx**  Ex.: 150.45 -> R$ 150.45
* Deve constar histórico de movimentação na conta
*  A função saque deve receber argumentos por posição `positional only`: `saldo` e por nome `keyword only` : `extrato`

> Criação de usuário:
* Criar a função `criar_usuario`
* Usuário deve ser adicionado a lista de usuários
* Usuário é composto por: `nome`, `data_nascimento`, `cpf` (apenas números) e `endereco`
* O endereço é uma string com formato: logradouro - Bairro - Cidade/Sigla estado
* Não pode haver dois usuários com o mesmo CPF 

> Criação de Conta corrente:
* Criar a função `criar_conta_corrente`
* Armazenar as contas em uma lista 
* A conta é composto por: `numero_conta`, `cpf_usuario`
* O número da conta é sequencial, iniciando em `1`
* O número da agência é fixo `:0001`
* O usuário pode ter mais de uma conta vinculada a ele mas uma conta tem apenas um usuário

**Dica repassada no início do desafio:**
> Para vincular conta com o usuário, filtre a lista de usuários buscando o CPF informado para cada usuário da lista
---
#### Saiba mais sobre o Bootcamp : [Dio.](https://web.dio.me/track/953ab0a9-6d55-4e00-ab7f-5ed855d288ca?tab=path)


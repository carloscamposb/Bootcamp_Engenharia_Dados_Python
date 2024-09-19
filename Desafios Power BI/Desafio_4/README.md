## Bootcamp Engenharia de Dados com Python - DIO. NTT DATA

### Projeto desenvolvido durante o desafio: *Dashboard de Vendas com Power BI utilizando Satr Schema* 📈 ✨
---

### Tecnologias Utilizadas:
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

# Proposta
Criar o diagrama dimensional – star schema – com base no diagrama relacional disponibilizado no módulo.
Deverá ser criada a tabela Fato que contêm o contexto analisado. Da mesma forma, é necessária a criação das tabelas dimensão que serão compostas pelos detalhes relacionados ao contexto.

> Esse modelo é amplamente utilizado em Data Warehouses por ser simples e eficiência nas análises de dados. Ele consiste em uma tabela de fatos central (Nesse caso, tabela professor),
que armazena dados de várias tabelas de dimensões (Nesse caso, curso, calendario,departamento,disciplina) que descrevem atributos contextuais relacionados aos fatos.

### Instruções:
> * O Professor é o objeto de análise
> * Montar o esquema em estrela com o foco na análise dos dados dos professores.
> * Tabela fato deve refletir diversos dados sobre professor, cursos ministrados, departamento ao qual faz parte...
> * Não é necessário refletir dados sobre os alunos! (Tabela pode ser excluida)
> * Tabelas não relacionadas devem excluidas
> * Adicionar uma tabela dimensão de datas. Para compensar a falta de dados de datas do modelo relacional,
> * Suponha que você tem acesso aos dados da tabela datas e crie os campos necessários para modelagem.
> * A granularidade, não está fixada. Podem ser utilizados diferentes formatos que correspondem a diferentes níveis de granularidade para data.

#### Imagem Referencia:
<div align="center">
  <image src="https://github.com/user-attachments/assets/7a623377-a581-4f9f-955f-906d3fabb383" height=400 />
</div>

#### Imagem após transformação no modelo star schema:
<div align="center">
  <image src="https://github.com/user-attachments/assets/d1ba0897-de20-4804-99df-a1b6f86b997a" height=400 />
</div>

#### Estrutura do Projeto:
> Tabela de Fatos -
  *  (f_Professor): Armazena informações sobre professores, como nome, data de nascimento, sexo e CPF. Essa tabela se relaciona com várias dimensões para fornecer mais detalhes contextuais sobre o professor.
> Tabela dimensões -
  * d_departamento: Armazena informações sobre o departamento, como nome, campus, andar e área de estudo.
  * d_disciplina: Contém informações sobre as disciplinas, como tipo e pré-requisitos.
  * d_Curso: Armazena os dados do curso, incluindo nome e faixa salarial.
  * d_Datas: Registra as datas relacionadas ao início, término e dias de aula.

#### Relações no Modelo:
>O Star Schema foi implementado com uma relação de muitos-para-um (N:1) entre a tabela de fatos (f_Professor) e cada tabela de dimensão. Isso significa que cada professor pode estar associado a um único departamento, curso, disciplina e conjunto de datas, enquanto cada dimensão pode ser referenciada por múltiplos professores. Isso vai permitir consultas rápidas e mais eficientes sobre os dados dos professores e seus atributos relacionados.

#### Alterações pontuais
> * Adição de campos que não estavam presente no modelo referencia
> * exclusão das tabelas de matricula, aluno e tabelas de junção
> * pré-requisito tornou-se atributo em disciplina
> * tabela data foi nomeada calendário

---
#### Saiba mais sobre o Bootcamp : [Dio.](https://web.dio.me/track/953ab0a9-6d55-4e00-ab7f-5ed855d288ca?tab=path)

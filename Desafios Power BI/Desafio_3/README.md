## Bootcamp Engenharia de Dados com Python - DIO. NTT DATA

### Projeto desenvolvido durante o desafio: *Criando Um Dashborad corporativo com integração com MySQL e Azure* 📈 
---

### Tecnologias utilizadas:
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) <br>
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)<br>
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)<br>

### Dados utilizados:
script e inserts fictícios simulando dados de uma empresa 

### Proposta:
O intuito desse desafio proposto pela DIO. junto à NTT Data foi a criação de uma instância na Azure para MySQL, criação do banco de dados com base no script fornecido, integrar o Power BI com o MySQL no Azure e por fim verificar problemas na base de dados a fim de realizar a transformação desses dados.

### Etapas realizadas
<div align=center>
 <img src="https://github.com/user-attachments/assets/24bbed94-9aef-40ee-8ba6-4fda19339dcb" height="200"/>
</div>


### Instruções
> Realizar a configuração do setup de banco de dados da Azure
> Popular o servidor com script fornecido
> integrar o MySQL com Power BI
> Realizar as transformações indicadas

#### Transformações Necessárias
> * Cabeçalhos alterados para serem mais legíveis <br>
> * Valores monetários de salário foram alterados para Double <br>
> * Nulos foram analisados para dois campos em gerente e foram tratados como solicitado <br>
> * Colunas de aniversario foram separadas em dia, mês e ano <br>
> * Colunas de endereço foram separadas em número, bairro, cidade e estado <br>
> * Coluna de funcionário foi mesclada via Power BI com departamento associados aos colaboradores <br>
> * Junção de colaboradores com seus respectivos gerentes , via Power BI <br>
> * Agrupei os dados para saber quantos colaboradores cada gente possui <br>
> * Eliminação das colunas não necessárias para a análise: (nome do meio) - funcionário, ( dia , mês) - aniversário , (numero_endereco, rua, bairro, estado(eram os mesmos)) - endereço, (data_criação)- departamento <br>
> * Mescla das colunas de nome e sobrenome <br>
> * Mescla das colunas de nome de departamento e local de departamento como solicitado <br>

> Usamos `Mesclar` quando o objetivo é relacionar duas tabelas com base em colunas compartilhadas, ou seja, quando precisamos combinar dados que têm uma correspondência específica entre si. `Atribuir` seria usado em cenários diferentes, onde a tarefa é simplesmente adicionar mais registros, sem a necessidade de correspondência entre as colunas.<br>

#### Imagens do MySQL instanciado na Azure
<div align=center>
 <img src = "https://github.com/user-attachments/assets/78beffcb-d601-4831-8d53-456180993bdf"  />
</div>

#### Conexão com o workbanch MySQL
<div align=center>
 <img src = "https://github.com/user-attachments/assets/9cc74e64-84ab-4954-a72d-972dd63e12b9"  /> 
<br>
  <img src = "https://github.com/user-attachments/assets/f910c5ef-b8bf-49be-a070-76edcfd337d7"  />
 <br> 
 <img src = "https://github.com/user-attachments/assets/2be9da36-2d2a-4b3f-8d4e-b683862bad95"  />
</div>

#### Imagens das tabelas criadas e populadas (Script e Inserts azure_company)
 <div align=center>
 <img src = "https://github.com/user-attachments/assets/cd2b496a-1b3f-4811-96c2-9e9a34b5d05a"  width=400 />
 <br>
   <img src = "https://github.com/user-attachments/assets/b212c360-9a5f-4765-b9f2-70671bd85b42"  width=400 />
</div>

 ##### Após foi feita a integração com o PowerBI através do link: `powerbicarloscampos.mysql.database.azure.com`

#### Imagem das tabelas do script já integrado ao Power BI antes das transformações
![image](https://github.com/user-attachments/assets/e453be03-b59f-402e-b71c-60874b4c36f9)

#### Imagem das tabelas do script já integrado ao Power BI após as transformações
![image](https://github.com/user-attachments/assets/8d1cd627-5021-4cfe-b460-9bb727200a07)

### Etapas da transformação:

#### Mesclando a tabela projetos com works_on para obter as horas de projeto
<img src = "https://github.com/user-attachments/assets/c007458e-8b3e-49a5-979b-b1b5c75f1c05" height="300" />

#### Departamentos sem gerente e após com adição de gerente do departamento 4
<img src="https://github.com/user-attachments/assets/602e7cb9-4f04-4e3a-a13e-d495618a0103" height="300"/>
<img src="https://github.com/user-attachments/assets/2bd019c8-028c-431d-ab1b-430592166764" height="300" />

#### Usando a ferramenta de dividir colunas do Power BI - Foi separado o aniversário e o endeço
<img src="https://github.com/user-attachments/assets/8625dde2-0207-49c4-9b05-457aa2e0ad18" height="300"/> 

#### aniversário
<img src="https://github.com/user-attachments/assets/6abc8661-3229-49a7-887a-7932213092ba" height="300"/>
<img src="https://github.com/user-attachments/assets/d8eaaa06-8053-4c16-bb59-0f119c2fad9e" height="300"/>

##### Para as analises que iria fazer julguei que não necessitaria de dia e mês do aniversário

#### Endereço
 <img src="https://github.com/user-attachments/assets/9fd4c27f-a604-4b65-a034-91c2d5f0c8df" height="300"/> <br>
##### Endereço seguiu o mesmo processo e dessa tabela eu exclui as colunas de número, bairro e país pois não seriam usados nas analises


#### Mesclar nome e sobrenome
 <img src="https://github.com/user-attachments/assets/0d67bf95-a01f-4f00-80d6-13d0231a9b93" height="300"/>
 <img src="https://github.com/user-attachments/assets/08da7696-ec35-471b-9a86-c872b21143ba" height="300"/>

#### Relacionar Gerente e Colaborador
* Separei por suas etapas. A primeira eu mesclei departamento com funcionário utilizando o Ssn (código do funcionário)
* Depois eu puxei os nomes relacionados ao ssn e em seguida adicionei na tabela mesclada o Super_Ssn que é usado pelos gerentes
<img src="https://github.com/user-attachments/assets/8e697c95-c3eb-402f-a481-bf6f5250aac1" height="300"/> <br>
* Após isso eu apliquei a mescla novamente usando como referencia a coluna do Super_Ssn
* Por fim puxei o nomes baseado no Super_Ssn
* Tirei as duplicatas e obtive a tabela com a relação
<img src="https://github.com/user-attachments/assets/956dfc5d-9bfa-4aac-b661-96b2d17d655c" height="300"/>
<img src="https://github.com/user-attachments/assets/29ec51b2-3735-401e-8240-d86a3805f778" height="300"/>

#### Contagem de colaboradores por gerente
<img src="https://github.com/user-attachments/assets/86bbfeaf-ae70-4250-b642-cffe7f6f08b1" height="300"/>

### Resultado final das tabelas antes da criação do Relatório

#### Departamento
  ![image](https://github.com/user-attachments/assets/89f4e061-d43c-49b4-a180-6059eeb2a1bb)
#### Contagem Colaborador por gerente
  ![image](https://github.com/user-attachments/assets/a438f0ae-35c1-4183-8f21-70c0d66cda4e)
#### Funcionário
  ![image](https://github.com/user-attachments/assets/a952410b-1c25-433b-891d-186dafb5cebc)
#### Relação Funcionario e Colaborador
  ![image](https://github.com/user-attachments/assets/92061f2a-3a17-4486-a984-0087caed31a4)
#### Relação de projeto com horas
  ![image](https://github.com/user-attachments/assets/a92b1d03-cb1f-4498-8ac4-11df83499801)
#### Projetos
  ![image](https://github.com/user-attachments/assets/a15788e3-7668-448e-b808-0eb107b7d822)
  
#### Alterações salvas e prontas para gerar o relatório
  ![image](https://github.com/user-attachments/assets/66e9dc81-4dec-4530-9b5a-ac1a727c1215)


### Resultado final: Relatório no Power BI 
![image](https://github.com/user-attachments/assets/3791e04e-b933-4806-a930-5e7ed96d066c)


---
#### Saiba mais sobre o Bootcamp : [Dio.](https://web.dio.me/track/953ab0a9-6d55-4e00-ab7f-5ed855d288ca?tab=path)
    
  

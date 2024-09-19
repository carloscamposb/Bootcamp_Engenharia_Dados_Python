## Bootcamp Engenharia de Dados com Python - DIO. NTT DATA

### Projeto desenvolvido durante o desafio: *Modelando um Dashboard de E-commerce com Power BI Utilizando Fórmulas DAX* 📈 
---
### Tecnologias Utilizadas:
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

### Dados utilizados:
Planilha de finanças gerada pelo PowerBI para estudo

### Proposta
* Utilização da tabela única de Financial Sample para criar as tabelas dimensão e fato do modelo baseado em star schema.

### Instruções
#### A partir da cópia da tabela original serão selecionadas as colunas que irão compor a visão da nova tabela.
 > A partir da tabela principal serão criadas as tabelas:
    * Financials_origem (modo oculto – backup)
    * d_Produtos (ID_produto, Produto, Média de Unidades Vendidas, Médias do valor de vendas, Mediana do valor de vendas, Valor máximo de Venda, Valor mínimo de Venda)
    * d_Produtos_detalhes(ID_produtos, Discount Band, Sale Price, Units Sold, Manufactoring Price)
    * d_Descontos (ID_produto, Discount, Discount Band)
    * d_Detlahes_extras(ID_produto, Segment, Country, Profit, CGOS, SK_ID)
    * d_datas – Criada por DAX com calendar()
    * f_Vendas (SK_ID , ID_Produto, Produto, Units Sold, Sales Price, Discount Band, Segment, Country, Salers, Profit, Date (campos))

### Imagem inicial da tabela financial
<div align=center>
  
<img src="https://github.com/user-attachments/assets/c76bcf73-e960-4ce9-80bf-9543daf9ac57" height= 400/>

</div>

### Execução da atividade
> Foram criadas as tabelas dimensão (d_ )  e a tabela fato (f_ )   
<div align=center>
<img src="https://github.com/user-attachments/assets/9b6a55dc-5bd1-42f5-8cde-cb6dfc9c49e0" height= 300/>
</div>

* Informações comtempladas nas tabelas dimensões foram avaliadas e retiradas da tabela fato quando necessário
* Os tipos dos dados em cada coluna foi revisado e quando necessário ajustados
* Foram criados índices para a tabela d_Produtos (id_Produtos) e para a tabela f_Vendas (id_Vendas)
* As colunas foram reorganizadas dentro das tabelas para uma leitura mais fluída dos dados

> Avaliação d_Produtos 
  * Foi decidido ao analisar a tabela Produtos que algumas colunas seriam agrupadas para melhor visualização e resultado
<div align=center>
<img src="https://github.com/user-attachments/assets/6b672b43-2665-43b7-ba32-780c23c010d1" height= 300/>
</div>

 > Adição de ID_produto
<div align=center>
<img src="https://github.com/user-attachments/assets/291cde8c-b538-4dc3-92ec-e4d0cff5d006" height= 300/>
</div>

### Criação da tabela para armazenar datas
* Uso da linguagem M - Fórmulas DAX
1) Criação da tabela
  `d_datas = CALENDARAUTO(12)`
2) Criação da tabela Year
  `YEAR= YEAR('d_datas'[Date])`
3) Criação dia da semana (numero)
   `week_number = WEEKNUM('d_datas'[Date])`
5) Criação dia da semana (nome)
    `dia_da_semana = FORMAT('d_datas'[Date],"DDDD")`
7) Criação do mês (numero
    `Month_number = MONTH('d_datas'[Date]) `
9) Criação do mês (nome)
    `Month_name = FORMAT('d_datas'[Date],"MMMM")`

> As datas em formato long foram transformadas em Short, tanto na tabela d_data quanto na tabela f_Vendas**

> Depois foi construido a hierarquia com granularidade alta. As colunas fora dessa hierarquia foram ocultadas para melhor visualização na criação dos visuais de relatórios no Power PI
<div align=center>
<img src="https://github.com/user-attachments/assets/ed7eb4ed-7d5b-45c1-9f87-5afc5e8ba852" />
</div>

### Visão geral das tabelas 

#### Recorte da Tabela d_datas ( presente no modelo de exibição, tabela criada via DAX)
<div align=center>
<img src="https://github.com/user-attachments/assets/366c0674-045c-4331-bfaa-2453c06e2e93"  width= 400/>
</div>

#### Tabela d_Produtos (completa) 
<div align=center>
<img src="https://github.com/user-attachments/assets/b816e205-d189-4fd0-b328-b9c61aca407d" width= 400/>
</div>


#### Recorte da Tabela d_Descontos
<div align=center>
<img src="https://github.com/user-attachments/assets/9a3b95a4-12fb-4099-b7ba-ee11be31c5a5" width= 450/>
</div>


#### Recorte da Tabela d_produtos_detalhes
<div align=center>
<img src="https://github.com/user-attachments/assets/a6fad0d6-6e1f-4718-80e3-dd5d5440bc84" width= 450/>
</div>


#### Recorte da Tabela d_detalhes_extras
<div align=center>
<img src="https://github.com/user-attachments/assets/93f9d6f6-e7bd-4995-bcca-a5e9629893da" width= 450/>
</div>

#### Recorte da Tabela f_Vendas
<div align=center>
<img src="https://github.com/user-attachments/assets/705cc662-5055-46f7-8628-118722fde1cb" />
</div>


### Resultado final das tabelas dimensões e tabela fato no modelo star schema
<div align=center>
<img src="https://github.com/user-attachments/assets/6eedc43e-6ef1-46de-923c-9bd016a71917" height= 400/>
</div>


---
#### Saiba mais sobre o Bootcamp : [Dio.](https://web.dio.me/track/953ab0a9-6d55-4e00-ab7f-5ed855d288ca?tab=path)

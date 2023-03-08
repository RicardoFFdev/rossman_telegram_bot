 <h1 align="center"> Rossmann Sales Forecast </h1>

![Getting Started](./img/rossmann_shop_foto_stralsund.jpg)


# Sejam bem-vindos ao meu projeto de portfólio de negócio da empresa Rossmann.


## 1.0 O Problema do Negócio


O time de negócios da Rossmann quer estimar o faturamento de cada loja nas próximas seis semanas, com objetivo de identificar quais lojas teriam faturamento suficiente para realizar novos investimentos.

## 1.1 Contexto do Negócio

Nesse banco de dados iremos encontrar 1.017.209 entradas que datam de 01/01/2013 até 31/07/2015. São dados de mais de 3000 lojas em 7 diferentes países.

## 1.2 Entendimento e Desafio do Problema de Negócio

Com milhares de gerentes individuais prevendo vendas com base em seu contexto, a precisão dos resultados podem sofrer muitas variações, e isso prejudicaria na tomada de decisão do time de negócios.<br>
Diante dessa situação o time de dados ficou encarregado de realizar uma análise e uma previsão, mais precisa possível, para o negócio. 


## 2. Planejamento prévio

### Método CRISP-DS

![Crisp](./img/ciclo.png)


## 2.1 Ferramentas, IDE's e Bibliotecas

* Python 3.10
* Visual Studio Code
* Jupyter Notebook
* PyCharm Community Ed.
* Bibliotecas: Seaborn, Plotly, Plotly Express, Pandas, Numpy, Pickle, Streamlit, Boruta, XGBoost, SKLearn e MatPlotLib
* Deploy final Streamlit Web Apps

## 2.2 Produto final

* Solucionar Insights.
* Desenvolver uma solução rápida e prática, podendo ser acessada de qualquer lugar e de qualquer dispositivo conectado a internet.


## 3.0 Estudo do negócio


As lojas da rede alemã Rossmann, que vendem itens de higiene, comidinhas, coisas para casa, roupas básicas e bebidas, são a companheira para todas as horas de quem viaja para a Alemanha. Filiais estão na estação de metrô e trens de Hannover e pelas ruas. A versão express funciona até tarde da noite. Os preços são motivo extra para entrar a cada passada. Ir a Alemanha e não entrar em uma Rossmann e como não ir à maior economia europeia.

**Fonte:** [ Jornal do Comércio ](https://www.jornaldocomercio.com/_conteudo/especiais/hannover_messe_2019/2019/04/678068-dicas-de-hannover.html)


## 4.0 Dados


##### Estes são dados públicos que foram coletados na página web do [Kaggle](https://www.kaggle.com/c/rossmann-store-sales).

## 4.1 Atributos de origem

 Abaixo segue a descrição para cada um dos 15 atributos:<br><br>
| **Atributos**         |  **Descrição**  |
| ----------------------|------------------------------------------------------------------------------------------|
|  id                   | um Id que representa um (Store, Date) concatenado dentro do conjunto de teste |
|  Store                |  um id único para cada loja |
|  Sales                |  o volume de vendas em um determinado dia |
|  Customers            |  o número de clientes em um determinado dia |
|  Open                 |  um indicador para saber se a loja estava aberta: 0 = fechada, 1 = aberta |
|  StateHoliday         |  indica um feriado estadual. Normalmente todas as lojas, com poucas exceções, fecham nos feriados estaduais. Observe que todas as escolas fecham nos feriados e finais de semana. a = feriado, b = feriado da Páscoa, c = Natal, 0 = Nenhum |
| SchoolHoliday         |  indica se (Store, Date) foi afetada pelo fechamento de escolas públicas |
|  StoreType            |  diferencia entre 4 modelos de loja diferentes: a, b, c, d |
|  Assortment           |  descreve um nível de sortimento: a = básico, b = extra, c = estendido |
|  CompetitionDistance  |  distância em metros até a loja concorrente mais próxima |
|  CompetitionOpenSince |  apresenta o ano e mês aproximados em que o concorrente mais próximo foi aberto |
|  Promo                |  indica se uma loja está fazendo uma promoção naquele dia |
|  Promo2               |  Promo2 é uma promoção contínua e consecutiva para algumas lojas: 0 = a loja não está participando, 1 = a loja está participando |
|  Promo2Since          |  descreve o ano e a semana em que a loja começou a participar da Promo2 |
|  PromoInterval        | descreve os intervalos consecutivos de início da promoção 2, nomeando os meses em que a promoção é iniciada novamente. Por exemplo. "Fev, maio, agosto, novembro" significa que cada rodada começa em fevereiro, maio, agosto, novembro de qualquer ano para aquela loja |

## 4.2 Atributos criados

* competition_open_since_month -> A quantidade de meses desde de que uma loja competidora próxima foi aberta.
* competition_open_since_year -> A quantidade de anos desde de que uma loja competidora próxima foi aberta.
* promo2_since_week -> A quantidade de semanas desde a última promoção categoria 2.
* promo2_since_year -> A quantidade de anos desde a última promoção categoria 2.
* promo_interval -> O intervalo entre promoções na mesma loja
* month_map -> Mapeamento dos meses 1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov' e 12: 'Dec'

## 4.3 Mapa Mental para Criação de Hipóteses/Insights

![MindMap](./img/mind_map_hypothesis.png)

## 5.0 Premissas


- Para as lojas que não possuíam informações de 'Competition Distance', foi considerado a maior distância observada no conjunto de dados.
- Foram consideradas apenas lojas com valores de venda maior que 0.
- Os dias em que as lojas estão fechadas foram retiradas da análise.


## 6.0 Principais Insights


### 1. Lojas com maior sortimentos vendem mais?

-> A hipótese é FALSA. As lojas que possuem maior sortimento VENDEM MENOS no geral.

![h1](./img/h1barplot.png)

### 2. Lojas com competidores mais próximos vendem menos?
-> A hipótese é FALSA. Lojas com COMPETIDORES MAIS PRÓXIMOS VENDEM MAIS.

![h2](./img/h2plot.png)

### 3. Lojas com competidores há mais tempo vendem mais?
->  A hipótese é FALSA. Lojas com competidores há mais tempo VENDEM MENOS.

![h3](./img/h3plot.png)

### 4. Lojas com promoções ativas por mais tempo vendem mais?
-> A hipótese é FALSA. Depois de um certo período de promoção as lojas passam a vender MENOS.

![h4](./img/h4plot.png)

### 5. Lojas com promoções consecutivas vendem mais?
-> A hipótese é FALSA. As lojas com promoções consecutivas vendem MENOS.

![h5](./img/h5plot.png)

### 6. Lojas abertas durante o feriado do Natal vendem mais?
-> A hipótese é FALSA. As lojas abertas durante o feriado do Natal vendem MENOS.

![h6](./img/h6plot.png)

### 7. As lojas estão vendendo mais ao longo dos anos?
-> A hipótese é FALSA. As vendas estão diminuindo ao longo dos anos.

![h7](./img/h7plot.png)

### 8. Lojas vendem menos nos finais de semana?
-> A hipótese é VERDADEIRA. As lojas vendem MENOS nos finais de semana.

![h8](./img/h9plot.png)

### 9. Lojas vendem mais depois do 10º dia do mês?
-> A hipótese é VERDADEIRA. As lojas vendem MAIS depois do 10º do mês.

![h9](./img/h9plot.png)


## 7.0 Modelagem dos dados

Nesta etapa, os dados foram preparados para o início das aplicações dos modelos de machine learning. Foram utilizadas técnicas de Rescaling e Transformation, através de encodings e nature transformation, e também o Boruta para selecionar os melhores atributos para treinar o modelo afim de obter uma melhor acurácia.

## 7.1 Machine Learning Modeling

Nesta etapa,foi relizado testes e treinamento em 5 modelos,Random Forest Regressor,XGBoost Regressor, Linear Regression - Lasso, Linear Regressor e Average Model.<br>
Usamos  o Average Model como base para compararmos os demais modelos  suas respctivas performance e escolha do melhor modelo.<br>
Também foi aplicada a técnica de Cross Validation para garantir a performance real sobre os dados selecionados.<br>
A melhor performace encontrada foi do  Random Forest Regressor, porém escolhemos o modelo XGBoost Regressor. A razão dessa escolha é que o XGBoost é um modelo mais leve para operar em produção e não aparesenta diferença significativa de desempenho.

## Performance

![perform](./img/models_performance.png)

## Cross Validation Performance

![cv](./img/cv_performance.png)

## 8.0 Avaliação do Algorítimo

Hyperparamenter Fine Tunning:

Com o algorítimo XGBoost escolhido na etapa anterior, foi realizada uma análise através do método Randon Search para escolher os melhores valores para cada parâmetro do modelo e encontrar a performance final do XGBoost.

Desempenho dos dados de teste:

![finetune](./img/xgb_tuned.png)

## 8.1 Tradução e interpretação de erros

Nesta etapa o objetivo foi demonstrar o resultado do projeto, onde avaliamos a performance do modelo com viés de negócio, demonstando o resultado financeiro que pode-se esperar do modelo desenvolvido.

![tuned](./img/perform.png)

## Predições do Modelo de Machine Learning

![pred](./img/predictions.png)

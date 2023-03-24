# 1. Problema de Negócio

Parabéns! Você acaba de ser contratado como Cientista de Dados da empresa Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer utilizando dados!

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

## O Desafio

O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:

### Geral

    Quantos restaurantes únicos estão registrados?

    Quantos países únicos estão registrados?

    Quantas cidades únicas estão registradas?

    Qual o total de avaliações feitas?

    Qual o total de tipos de culinária registrados?

### País

    Qual o nome do país que possui mais cidades registradas?

    Qual o nome do país que possui mais restaurantes registrados?

    Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?

    Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?

    Qual o nome do país que possui a maior quantidade de avaliações feitas?

    Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?

    Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?

    Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?

    Qual o nome do país que possui, na média, a maior nota média registrada?

    Qual o nome do país que possui, na média, a menor nota média registrada?

    Qual a média de preço de um prato para dois por país?

### Cidade

    Qual o nome da cidade que possui mais restaurantes registrados?

    Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?

    Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?

    Qual o nome da cidade que possui o maior valor médio de um prato para dois?

    Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?

    Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?

    Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?

    Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

### Restaurantes

    Qual o nome do restaurante que possui a maior quantidade de avaliações?

    Qual o nome do restaurante com a maior nota média?

    Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?

    Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?

    Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?

    Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?

    Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?

    Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

### Tipos de Culinária

    Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?

    Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?

    Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?

    Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?

    Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?

    Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?

    Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?

    Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?

    Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?

    Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?

    Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?

    Qual o tipo de culinária que possui a maior nota média?

    Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez. O CEO precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.

Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as perguntas feitas do CEO e criar o dashboard solicitado
### Os Dados

O conjunto de dados que representam o contexto está disponível na plataforma do Kaggle. O link para acesso aos dados :

https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv

# 2. Premissas do Negócio

    Alguns restaurantes oferecem mais de um tipo de colunaria, para essa análise utilizou-se apenas a sua especialidade sendo esta considerado como o primeiro item da lista.
    Linhas duplicadas e/ou com valores faltantes foram descartados.
    As principais visões de negócio apresentadas foram: visão por país, visão por cidade e visão por restaurantes.

# 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem 3 principais visões de atuação do do modelo de negócio da empresa:

    Visão Países
    Visão Cidades
    Visão Restaurantes

### 1. Home

    Números absolutos do negócio: quantidade de países, cidades, restaurantes, avaliações… ;
    Localização geográfica no mapa dos restaurantes.

### 2. Visão Países

    Quantidade de restaurantes por país por ordem decrescente;
    Quantidade de cidades por país por ordem decrescente;
    Quantidade média de avaliação por país por ordem decrescente;
    Avaliação média por país por ordem decrescente;
    Valor médio do prato por país por ordem decrescente;

### 3. Visão Cidades

    Cidades com maior número de restaurantes cadastrados;
    Cidades com melhores avaliações média por restaurantes;
    Cidades com piores avaliações média por restaurantes;
    Cidades com maior quantidade de culinárias distintas oferecida.

### 4. Visão Restaurantes

    Restaurantes mais bem avaliados nos principais tipos culinários;
    Ranking de restaurantes mais bem avaliados da plataforma;
    Ranking de tipos culinários com melhores avaliações média;
    Ranking de tipos culinários com piores avaliações média;


# 4. Top 3 Insights de dados deste projeto

    1. A maior quantidade média de avaliações ocorre na Indonésia que está na 11ª colocação em quantidade de restaurantes e conta com apenas 3 cidades cadastradas.
    2. Em relação a quantidade de cidades com maior número de culinárias distintas os Estados Unidos encontra-se em terceiro lugar, atrás da Índia e até mesmo do Qatar.
    3. Restaurantes especializados no tipo culinária café estão em segundo lugar na classificação de aceitar pedidos online e fazer entrega.

# 5. O produto final do projeto

Dashboard Online, hospedado em cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O dashboard pode ser acessado através deste link: https://mateuszaidan-fome-zero-home-mzvcy0.streamlit.app/
# 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

Da visão geral podemos verificar uma maior atuação da empresa na Ásia, principalmente Índia, e nos Estados únicos.
# 7. Próximos passos

    Reduzir o número de métricas para as que afetam diretamente o crescimento da empresa
    Criar novos filtros
    Adicionar novas visões de negócio


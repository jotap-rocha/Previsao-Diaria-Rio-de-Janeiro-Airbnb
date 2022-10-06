# Previsao Diaria Rio de Janeiro Airbnb
 Projeto de Data Science com o objetivo de precificar o valor de uma diária no Rio de Janeiro, através de dados do Airbnb

Desafio: Capturei a base de dados do site Airbnb, a qual dispôes de diversas informações a respeito de clientes que são locadores e que alugam, e idealizei prever o preço de uma locação comum, na cidade do Rio de Janeiro, entre os anos de 2018 a 2021, com base em alguns critérios tais como, latitude, longitude, acomodações e outros. Isso nos permite aferir um preço tanto para a pessoa que quer alugar uma diária no Rio de Janeiro, quanto para você que quer iniciar um negócio e dispôr o seu imóvel para locação.

Ferramentas e tecnologias: Para realizar o projeto, utilizeia linguagem de programação Python, que é a melhor linguagem atualmente para um projeto de ciência de dados. Utilizei também conceitos estatísticos como análise exploratória, descritiva e, posteriormente, análise preditiva em cima de algoritmos de inteligência artificial tais como, regressão linear e árvore de decisão, além é claro de bibliotecas de visualização como matplotlib e seaborn para visualizar as informações.

COMO FUNCIONA O PROJETO

Primeiro, recomendo a instalação do python e as IDEs Jupyter e Pycharm;

Python -> https://www.python.org/downloads/

Jupyter -> https://jupyter.org

Pycharm -> https://www.jetbrains.com/pycharm/download/#section=windows

Depois, descompacte as bases de dados para o funcionamento correto do projeto.

O funcionamento começa com o arquivo "Projeto Ciência de Dados.ipynb", executado pelo Jupyter. Nele, eu segui determinados procedimentos, os quais irei citar agora:

- Primeiro de tudo, ler as bases de dados disponíveis através da biblioteca pandas;

- Fiz uma análise qualitativa dos dados para "enxugar" as features (colunas) e tornar a base mais adequada ao objetivo deste projeto, que é precificar o valor de uma diária no Rio de Janeiro. Criei um arquivo chamado "Primeiros_registros.csv";

- Realizei um data cleaning, etapa onde tratamos os dados, lidamos com valores ausentes, etc;

- Após estas etapas, comecei a análise exploratória, com foco em entender os dados, como as features estão se comportando, mapa de correlação, e, claro, tratamento de outliers. Através do mapa de correlação percebi que há uma pequena relação entre o preço e a quantidade de quartos. Realizei a exclusão de outliers das features que sobraram, pois o intuito é precificar imóveis comuns. Excluí as features "guest included", "Minimum night" e "number of reviews", pois são features que não retornam informações concisas;

- No final da análise exploratória, consegui aferir que quanto mais próxima a locação for da praia ou de zonas nobres, mais cara ela será, ou seja, existe uma relação muito forte entre o preço, latitude e longitude;

- Processo de encoding, no qual trata-se a base para que ela fique legível para os modelos de previsão, tornando a base totalmente quantitativa;

- Definição de modelos de regressão, já que quero prever um valor (não categoria), treino e teste dos mesmos;

- Ajustes e melhorias do modelo escolhido;

- Deploy do projeto.

Após executar o arquivo descrito anteriormente, você irá perceber que será criado um arquivo chamado "Modelo.joblib", o qual não foi adicionado ao repositório pois o github não permite (excesso de tamanho do arquivo).

Após a execução, abra o arquivo "DeployProjetoAirbnb.py", com o Pycharm, e siga o passo a passo que disponibilizei dentro do arquivo. Irá abrir uma tela no seu navegador de internet e por meio dela será possível adicionar algumas características de locação e, no final, você receber uma previsão de preço para o lugar que você deseja precificar.

Observação: Para adicionar valores de longitude e latitude no modelo e iniciar a previsão, sugiro ir no google maps, dar um clique com o botão direito do mouse em cima do lugar que você deseja aferir um preço, e copiar a latitude e longitude fornecida.

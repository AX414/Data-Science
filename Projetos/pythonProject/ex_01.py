#mostra o hello world
print("\nHello World!");

#mostra na tela o ds da soma de 30 + 50
soma = 30+50;
print('\nResultado da soma: ', soma);
#--------------------------------------------------


#biblioteca - pandas (tem que instalar)
#função - read_csv()

#carrega o conjunto de dados do kc_house_data.csv
#do HD para a memória

#instalar via terminal com o pip: pip install pandas
import pandas as pd
ds = pd.read_csv('datasets/kc_house_data.csv');

#head: mostra as 5 primeiras linhas
print('\nMostrar as 5 primeiras linhas:\n', ds.head());

#shape: mostra o número de colunas e linhas do conjunto de dados
print('\nMostra o número de colunas e linhas do conjunto de dados:\n',ds.shape);

#columns: mostra na tela o nome das colunas do conjunto de dados
print('\nMostra na tela o nome das colunas do conjunto de dados:\n', ds.columns);

#sort_values: mostrar na tela o conjunto de dados ordenados pela coluna price
print('\nMostrar na tela o conjunto de dados ordenados pela coluna price:\n', ds.sort_values('price'));

#mostrar na tela o conjunto de dados ordenados pela coluna price apresentando ela e o id
print('\nMostrar na tela o conjunto de dados ordenados pela coluna price apresentando ela e o id: \n',
      ds[['id','price']].sort_values('price'));

#mostrar na tela o conjunto de dados ordenados pela coluna price na ordem decrescente, apresentando ela e o id
print('\nMostrar na tela o conjunto de dados ordenados pela coluna price na ordem decrescente, apresentando ela e o id: \n',
      ds[['id','price']].sort_values('price',ascending = False));
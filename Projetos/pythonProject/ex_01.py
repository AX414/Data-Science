# mostra o hello world
#print("Hello World!");

#mostra na tela o resultado da soma de 30 + 50
#soma = 30+50;
#print(soma);

#carrega o conjunto de dados do kc_house_data.csv
#do HD para a memória
#--------------------------------------------------

#biblioteca - pandas (tem que instalar)
#função - read_csv()

import pandas as pd
resultado = pd.read_csv('datasets/kc_house_data.csv');

#mostra as 5 primeiras linhas + o cabeçalho
#print(resultado.head());

#mostra o número de colunas e linhas do conjunto de dados - função shape
#print(resultado.shape);

#mostra na tela o nome das colunas do conjunto de dados
#print(resultado.columns);

#mostrar na tela o conjunto de dados ordenados pela coluna price
#print(resultado.sort_values('price'));

#mostrar na tela o conjunto de dados ordenados pela coluna price apresentando ela e o id
#print(resultado[['id','price']].sort_values('price'));

#mostrar na tela o conjunto de dados ordenados pela coluna price na ordem decrescente, apresentando ela e o id
print(resultado[['id','price']].sort_values('price',ascending = False));
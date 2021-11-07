import pandas as pd;

ds = pd.read_csv('datasets/kc_house_data.csv');

#1-quantas casas estão disponíveis para compra?
disponiveis = len(ds.index);
print('\n1-Quantas casas estão disponíveis para compra?\nR = ',disponiveis);

#2-quantos atributos as casas possuem?
qtdAtributos = (len(ds.columns));
print('\n2-Quantos atributos as casas possuem?\nR = ',qtdAtributos);

#3-quais os atributos das casas?
print('\n3-Quais os atributos das casas?\nR = ',ds.columns);

#4-qual a casa mais cara? (casa com o maior valor de venda)
maisCara = ds.loc[ds['price'].idxmax()];
print('\n4-Qual a casa mais cara? (casa com o maior valor de venda)\n R = ID: %s | Preço: %s'
      % (maisCara['id'],maisCara['price']));

#5-qual a casa com o maior número de quartos?
maxQuartos = ds.loc[ds['bedrooms'].idxmax()];
print('\n5-Qual a casa com o maior número de quartos?\n R = ID: %s | Quantidade de Quartos: %s'
      % (maxQuartos['id'],maxQuartos['bedrooms']));

#6-qual a soma total de quartos do conjunto de dados?
somaQuartos = sum(ds['bedrooms']);
print('\n6-Qual a soma total de quartos do conjunto de dados?\n R = ',somaQuartos);

#7-quantas casas possuem 2 banheiros?
totalCasas = sum(ds['bathrooms'] == 2);
print('\n7-Quantas casas possuem 2 banheiros?\n R = ',totalCasas);

#8-qual o preço médio de todas as casas do conjunto de dados?
precos = sum(ds['price']);
totalCasas = len(ds.index);
media = precos/totalCasas;
print('\n8-Qual o preço médio de todas as casas do conjunto de dados?\n R = %.2f' % (media));

#9-qual o preço médio de casas com 2 banheiros?
precos = sum(ds['price']);
totalCasas = sum(ds['bathrooms'] == 2);
media = precos/totalCasas;
print('\n9-Qual o preço médio de casas com 2 banheiros?\n R = %.2f' % (media));

#10-qual o preço mínimo entre as casas com 3 quartos?
precoMinimoObjeto = ds.loc[ds['price'].where(ds['bedrooms']==3).idxmin()];
print('\n(Versão com o objeto) 10-Qual o preço mínimo entre as casas com 3 quartos?\n R = ID: %s | Preço: %s'
      % (precoMinimoObjeto['id'],precoMinimoObjeto['price']));

precoMinimoApenasValor = min(ds['price'].where(ds['bedrooms']==3));
print('\n(Versão com apenas o valor) 10-Qual o preço mínimo entre as casas com 3 quartos?\n R = Preço:', precoMinimoApenasValor);

#11-quantas casas possuem mais de 300 metros quadrados?
totalSqft = sum(ds['sqft_living']>300);
pegaCasa = ds.loc[ds['sqft_living'].where(ds['sqft_living']<=300).idxmin()];
print('\n11-quantas casas possuem mais de 300 metros quadrados?\n R = ', totalSqft);
print('\n(OBS) Qual a casa com metro quadrado < 300? \nR = ID: %s | Metro Quadrado: %.2f | Preço: %.2f'
      % (pegaCasa['id'],pegaCasa['sqft_living'],pegaCasa['price']));

#12-quantas casas tem mais de 2 andares?
aux = (ds['floors'].where(ds['floors'] > 2));
maisDeDoisAndares = aux.count();
print('\n12-quantas casas tem mais de 2 andares?\n R = ', maisDeDoisAndares);

aux = (ds['floors'].head().where(ds['floors'] > 2));
maisDeDoisAndares = aux.count();
print('\n(OBS) 12-quantas casas tem mais de 2 andares dos 5 primeiros registros?\n R = ', maisDeDoisAndares);

#13-quantas casas tem vista para o mar?
aux = (ds['waterfront'].where(ds['waterfront'] > 0));
qtdVistaMar = aux.count();
print('\n13-Quantas casas tem vista para o mar?\n R = ', qtdVistaMar);

aux = (ds['waterfront'].where(ds['waterfront'] == 0));
qtdNaoTemVistaMar = aux.count();
print('\n(OBS) Quantas casas não tem vista para o mar?\n R = ', qtdNaoTemVistaMar);

#14-das casas com vista para o mar, quantas tem 3 quartos?
aux = (ds['waterfront'].where((ds['waterfront'] > 0 ) & (ds['bedrooms'] == 3)));
qtdVistaMarMaisTresQuartos = aux.count();
print('\n14-Das casas com vista para o mar, quantas tem 3 quartos?\n R = ', qtdVistaMarMaisTresQuartos);

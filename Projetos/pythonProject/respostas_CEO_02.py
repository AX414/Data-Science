import pandas as pd;

ds = pd.read_csv('datasets/kc_house_data.csv');

# Novas perguntas do CEO para voce:
# 1. Crie uma nova coluna chamada: “house_age”
# 	- Se o valor da coluna “date” for maior que 2014-01-01 => “new_house”
# 	- Se o valor da coluna “date” for menor que 2014-01-01 => “old_house”

ds['house_age'] = 'no value';
ds['house_age'] = ds['house_age'].astype('string');
ds['date'] = pd.to_datetime(ds['date']);

ds.loc[ds['date'] > '2014-01-01','house_age'] = 'new_house';
ds.loc[ds['date'] < '2014-01-01','house_age'] = 'old_house';

condicao = ds['house_age'].__eq__('new_house');
print('\n1-Lista das casas novas:\n',ds[['id','date','house_age']].where(condicao == True));
print('\n1-Lista das casas velhas:\n',ds[['id','date','house_age']].where(condicao == False));

# 2. Crie uma nova coluna chamada: “dormitory_type”
# 	- Se o valor da coluna “bedrooms” for igual a 1 => ‘studio’
# 	- Se o valor da coluna “bedrooms” for igual a 2 => ‘apartment’
# 	- Se o valor da coluna “bedrooms” for maior que 2 => ‘house’

ds['dormitory_type'] = 'no value';
ds['dormitory_type'] = ds['dormitory_type'].astype('string');

ds.loc[ds['bedrooms'] == 1,'dormitory_type'] = 'studio';
ds.loc[ds['bedrooms'] == 2,'dormitory_type'] = 'apartment';
ds.loc[ds['bedrooms'] > 2,'dormitory_type'] = 'house';
print('\n2-Tipos de Dormitórios:\n',ds[['id','price','bedrooms','dormitory_type']]);

# 3. Crie uma nova coluna chamada: “condition_type”
# 	- Se o valor da coluna “condition” for menor ou igual a 2 => ‘bad’
# 	- Se o valor da coluna “condition” for igual a 3 ou 4 => ‘regular’
# 	- Se o valor da coluna “condition” for igual a 5 => ‘good’

ds['condition_type'] = 'no value';
ds.loc[ds['condition'] <= 2,'condition_type'] = 'bad';
ds.loc[ds['condition'] == 3,'condition_type'] = 'regular';
ds.loc[ds['condition'] == 4,'condition_type'] = 'regular';
ds.loc[ds['condition'] == 5,'condition_type'] = 'good';
print('\n3-Tipos de Condição:\n',ds[['id','condition','condition_type']]);


# 4. Modifique o TIPO da coluna “condition” para STRING
ds['condition'] = ds['condition'].astype('string');
print('\n4-Modifique o TIPO da coluna “condition” para STRING:\n',ds.dtypes);

# 5.Delete as colunas: “sqft_living15” e “sqft_lot15”
ds = ds.drop('sqft_living15',axis = 1);
ds = ds.drop('sqft_lot15',axis = 1);
print('\n5-Delete as colunas: “sqft_living15” e “sqft_lot15”:\n',ds.columns)

# 6. Modifique o TIPO da coluna “yr_built” para DATE
ds['yr_built'] = pd.to_datetime(ds['yr_built']);
print('\n6-Modifique o TIPO da coluna “yr_built” para DATE:\n',ds.dtypes)

# 7. Modifique o TIPO da coluna “yr_renovated” para DATE
ds['yr_renovated'] = pd.to_datetime(ds['yr_renovated']);
print('\n7-Modifique o TIPO da coluna “yr_renovated” para DATE:\n',ds.dtypes)

# 8. Qual a data mais antiga de construcao de um imovel?
data = ds.sort_values('yr_built', ascending = True);
print('\n8-Qual a data mais antiga de construcao de um imovel?\nR =\n ',data.iloc[0:1,1:15]);

# 9. Qual a data mais antiga de renovacao de um imovel?
data = ds.sort_values('yr_renovated', ascending = True);
print('\n9-Qual a data mais antiga de renovação de um imovel?\nR =\n ',data.iloc[0:1,1:16]);

# 10. Quantos imoveis tem 2 andares?
aux = (ds['floors'].where(ds['floors'] == 2));
doisAndares = aux.count();
print('\n10-Quantos imoveis tem 2 andares?\n R = ', doisAndares);

# 11. Quantos imoveis estao com a condicao igual a “regular”?
aux = (ds['condition_type'].where(ds['condition_type'].__eq__('regular')));
regulares = aux.count();
print('\n11-Quantos imoveis estao com a condicao igual a “regular”?\n R = ', regulares);

# 12. Quantos imoveis estao com a condicao igual a “bad” e possuem “vista para agua”?
bad = ds['condition_type'].__eq__('bad');
waterfront = ds['waterfront'] == 1;
aux = (ds['id'].where((waterfront) & (bad)));
qtdBadWaterfront= aux.count();
print('\n12-Quantos imoveis estao com a condicao igual a “bad” e possuem “vista para agua”?\n R = ', qtdBadWaterfront);

# 13. Quantos imoveis estao com a condicao igual a “good” e sao “new_house”?
good = ds['condition_type'].__eq__('good');
new = ds['house_age'].__eq__('new_house');
aux = (ds['id'].where((good) & (new)));
qtdGoodNew= aux.count();
print('\n13-Quantos imoveis estao com a condicao igual a “good” e sao “new_house”?\n R = ', qtdGoodNew);

# 14. Qual o valor do imovel mais caro do tipo “studio”?
condicao = ds['dormitory_type'].__eq__('studio');
maisCara = ds.loc[ds['price'].where(condicao).idxmax()];
print('\n14-Qual o valor do imovel mais caro do tipo “studio”?\n R = ID: %s | Preço: %s'
      % (maisCara['id'],maisCara['price']));

# 15. Quantos imoveis do tipo “apartment” foram reformados em 2015?
from datetime import time;

data1 = ds['yr_renovated'];
data2 = 2015;
data2 = pd.to_datetime(data2);

condicao1 = data1 == data2;
condicao2 = ds['dormitory_type'].__eq__('apartment');

aux = (ds['yr_renovated'].where((condicao1) & (condicao2)));
qtdRenovados = aux.count();
print('\n15-Quantos imoveis do tipo “apartment” foram reformados em 2015?\n R = ', qtdRenovados);


# 16. Qual o maior numero de quartos que um imovel do tipo “house” possui?

condicao = ds['dormitory_type'].__eq__('house');
aux = ds['bedrooms'].where(condicao);
qtdMaiorNumeroQuartos = max(aux);
print('\n16-Qual o maior numero de quartos que um imovel do tipo “house” possui?\n R = ', qtdMaiorNumeroQuartos);

# 17. Quantos imoveis “new_house” foram reformados no ano de 2014?
data1 = ds['yr_renovated'];
data2 = 2014;
data2 = pd.to_datetime(data2);

condicao1 = data1 == data2;
condicao2= ds['house_age'].__eq__('new_house');

aux = (ds['house_age'].where((condicao1) & (condicao2)));
qtdNovaRenovados = aux.count();
print('\n17-Quantos imoveis “new_house” foram reformados no ano de 2014?\n R = ', qtdNovaRenovados);

# 18. Selecione as colunas: “id”, “date”, “price”, “floors”, “zipcode” pelo metodo:
# 	18.1 – Direto pelo nome das colunas
print('\n18.1–Direto pelo nome das colunas:\n',ds[['id','date','price','floors','zipcode']]);
# 	18.2 – Pelos indices
print('\n18.2–Pelos indices:\n',ds.iloc[0:10,0:21]);
# 	18.3 – Pelos indices das linhas e o nome das colunas
print('\n18.3–Pelos indices das linhas e o nome das colunas:\n',ds.loc[0:10,['id','date','price','floors','zipcode']]);
# 	18.4 – Indices booleanos
colunas = [True, True, True, False, False, False,
       False, True, False, False, False, False,
       False, False, False, False, True,
       False, False, False, False, False];

#print(ds.columns);
print('\n18.4–Indices booleanos:\n',ds.loc[0:10,colunas]);

# 19. Salve um arquivo .csv com somente as colunas do item 18
tamanho = len(ds['id']);
relatorio = ds.loc[0:tamanho,['lat']];
print('\n19-Relatório de Latitudes:\n',relatorio);
relatorio.to_csv('datasets/relatorioLatitudes.csv',index = False);

# 20. Modifique a cor dos pontos no mapa de “pink” para “verde-escuro”

#instalar via terminal com o pip: pip install plotly
import plotly.express as px;

ds_mapa = ds[['id','lat','long','price']];
print('\nDados do mapa de pontos verdes: \n',ds_mapa);

mapa = px.scatter_mapbox(ds_mapa,lat = 'lat' , lon = 'long', hover_name = 'id',
                hover_data = ['price'],
                color_discrete_sequence = ['green'],
                zoom = 3,
                height = 300
                )

mapa.update_layout(mapbox_style = 'open-street-map');

#margin ={right,top,left,bottom}
mapa.update_layout(height = 600,
                   margin = {'r':0, 't':0, 'l':0, 'b':0}
);

#O mapa abre no navegador, não coloquei o mapa.show() por estar tendo problemas
#de conexão recusada no 127.0.0.1 pelo Opera GX, mas com o auto_open = True, ele
#abrirá o mapa a partir do documento que é gerado no write_html, inclusive
#mais rápido (e travou menos aqui também)
mapa.write_html('datasets/mapa_pontos_verdes.html',auto_open=True);
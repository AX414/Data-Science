import pandas as pd;
ds = pd.read_csv('datasets/kc_house_data.csv');


#Mostrar os tipos de variaveis de cada coluna
#print('\nMostrar os tipos de variaveis de cada coluna:\n',ds.dtypes);

#====================================================================================
# Convertendo Variáveis
#====================================================================================

#int -> float
# ds['bedrooms'] = ds['bedrooms'].astype(float);
# print('\nAtualizou bedrooms para float:\n',ds.dtypes);
# print('\n\n',ds[['id','bedrooms']].head(3));
#
# #float -> int
# ds['bedrooms'] = ds['bedrooms'].astype(int);
# print('\nAtualizou bedrooms para int:\n',ds.dtypes);
# print('\n\n',ds[['id','bedrooms']].head(3));
#
# #int -> string
# ds['bedrooms'] = ds['bedrooms'].astype('string');
# print('\nAtualizou bedrooms para string:\n',ds.dtypes);
# print('\n\n',ds[['id','bedrooms']].head(3));
#
# #string -> date
# #trocando a data de object para date
# ds['date'] = pd.to_datetime(ds['date']);
# #data agora é do tipo data
# print('\nAtualizou date para o tipo date:\n',ds.dtypes);

#====================================================================================
# Manipulando Variáveis (Criar, Deletar, Selecionar)
#====================================================================================

#criar uma nova coluna
# ds['nome']= "JP";
# ds['outra_data'] = pd.to_datetime('2021-11-07');
# print(ds.columns);
# print(ds.dtypes);

#deletar uma coluna (axis é o sentido das colunas)
# ds = ds.drop('nome',axis = 1);
# ds = ds.drop('outra_data', axis = 1)
#pode deletar como lista também:

#colunas = ['nome'],['outra_data'];
#ds = ds.drop(colunas, axis = 1);
# print(ds.columns);

#<4 Formas de selecionar dados>
# Forma 1: Direto no nome da coluna
#print(ds[['price','id','date']]);

# ou isso:
#colunas = ['price','id','date'];
#print(ds[colunas]);

# Forma 2: Pelos índices das colunas
#iloc: localiza pelo index
#print(ds.iloc[0:10,0:3]);

# Forma 3: Pelos índices das linhas
#loc: localiza pela coluna
#print(ds.loc[0:10,'price']);

# Forma 4: Pelos índices booleanos (true|false)
# colunas = [True,True,True,True,
#            False,False,False,False,
#            False,False,False,False,
#            False,False,False,False,
#            False,False,False,False,
#            False];
#
# print(ds.loc[0:10,colunas]);



#====================================================================================
# Questões de Negócio
#====================================================================================
#Conceito: o CEO da empresa chegou e pediu esses 5 problemas, tenho que entregar por
# Email(perguntas|respostas) + Anexos(relatório em CSV e mapas)

#1-Qual a data do imóvel mais antigo no portifólio?
ds['date'] = pd.to_datetime(ds['date']);
data = ds.sort_values('date', ascending = True);
print('\n1-Qual a data do imóvel mais antigo no portifólio?\nR =\n ',data.iloc[0:1,0:3]);

#2-Quantos imóveis possuem o número máximo de andares?
ds['floors'] = ds['floors'].astype(float);
numeroMaximo = max(ds['floors']);
aux = (ds['floors'].where(ds['floors'] == numeroMaximo));
total = aux.count();
print('\n2-Quantos imóveis possuem o número máximo de andares?\nR = ', total);

#3-Criar uma classificação para os imóveis, separando-os
#em baixo e alto padrão de acordo com o preço:
# Alto padrão: >540.000
# Baixo padrão: <540.000

#Solução: Criar uma nova coluna no csv chamada "standard" (padrão)
#cada linha eu comparo com o 'price', se maior é high_standard, se não é low_standard

ds['level'] = 'standard';

ds.loc[ds['price'] > 540000,'level'] = 'high_level'
ds.loc[ds['price'] < 540000,'level'] = 'low_level';
print('\n3-Apresentando padrões:\nR = \n',ds.head());


#4-Gostaria de um relatório ordenado pelo preço
# e contendo as seguintes informações:
# (id, data que ficou disponível para comprar,
# número de quartos, tamanho total do terreno, preço,
# classificação do imóvel[alto/baixo padrão])

#Solução: Selecionar as colunas desejadas ou Deletar as indesejadas

relatorio = ds[['id','date','price','bedrooms','sqft_lot','level']];
print('\n5-Relatório:\n',relatorio.head().sort_values('price',ascending = False));
relatorio.to_csv('datasets/relatorio.csv',index = False);

#5-Gostaria de um mapa indicando onde as casas
# estão localizadas geograficamente.

#Solução: Usar uma biblioteca de python que desenhe o mapa,
# usar uma função para desenhar o mapa para as coordenadas.

#Plotly - Biblioteca que armazena uma função
# que desenha mapas, o nome da função é:
# Scatter MapBox, ela desenha o mapa
#parâmetros:


#instalar via terminal com o pip: pip install plotly
import plotly.express as px;

ds_mapa = ds[['id','lat','long','price']];
print('\nDados do mapa: \n',ds_mapa);

mapa = px.scatter_mapbox(ds_mapa,lat = 'lat' , lon = 'long', hover_name = 'id',
                hover_data = ['price'],
                color_discrete_sequence = ['fuchsia'],
                zoom = 3,
                height = 300
                )

mapa.update_layout(mapbox_style = 'open-street-map');

#margin ={right,top,left,bottom}
mapa.update_layout(height = 600,
                   margin = {'r':0, 't':0, 'l':0, 'b':0}
);

#O mapa abre no navegador
mapa.show();
mapa.write_html('datasets/mapa_kc_house_data.html');


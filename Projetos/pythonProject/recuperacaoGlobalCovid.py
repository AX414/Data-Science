import pandas as pd;
import plotly.express as px;


ds = pd.read_csv('datasets/time_series_covid19_recovered_global.csv');

#ds['total'] = 0;

#data = '4/7/21';

ds_mapa = ds[['Province/State','Country/Region','Lat','Long','4/1/21']];

#ds_mapa['total'] = sum(ds_mapa.iloc(0:len(ds_mapa['Province/State'],0:len(ds_mapa.c))));



print('\nDados do mapa: \n',ds_mapa);

mapa = px.scatter_mapbox(ds_mapa,
                lat = 'Lat',
                lon = 'Long',
                hover_name = ds_mapa['Country/Region'],
                hover_data = ['4/1/21'],
                color_discrete_sequence = ['blue'],
                zoom = 3,
                height = 300
                )

mapa.update_layout(title = 'Mapa de Recuperados da Covid:',mapbox_style = 'open-street-map',);

mapa.update_layout(height = 600);

mapa.write_html('datasets/recuperacaoGlobalCovid.html',auto_open=True);
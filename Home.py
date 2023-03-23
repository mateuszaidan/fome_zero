# Libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotly.express as px
import folium
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static



#=========================
#Funções
#=========================

#Preenchimento do nome dos países
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
def country_name(country_id):
    return COUNTRIES[country_id]

#Criação do nome das Cores
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
def color_name(color_code):
    return COLORS[color_code]


#Criação do Tipo de Categoria de Comida
def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

    #Renomear as colunas do DataFrame
def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

#------------------------Início da estrutura lógica do código---------------------
#---------------------------------------------------------------------------------
#Import dataset
#---------------------------------------------------------------------------------
df=df = pd.read_csv('dataset/zomato.csv')
#---------------------------------------------------------------------------------

#Limpeza de Dados

#Removendo as vírgulas da culinária
df['Cuisines'] = df['Cuisines'].astype( str )

df["Cuisines"] = df.loc[:, "Cuisines"].apply(lambda x: x.split(",")[0])


#Não remova 'Has Online delivery', 'Is delivering now', 

#removendo colunas
df = df.drop(['Switch to order menu'], axis = 1)

#Associando os códigos
df['Country'] = df['Country Code'].apply(lambda x: country_name(x), [0])

#Removendo valores vazios

df['Cuisines'] = df['Cuisines'].astype( str )

linha_vazia = df['Cuisines'] != 'nan'
    
df = df.loc[linha_vazia, :]

#Removendo duplicatas

df = df.drop_duplicates() 

#Removendo Outlier
linha = df[df['Average Cost for two'] == 25000017]
df = df.drop(385)

#----------------Copy------------------------
df1 = df.copy()



#================================================
#Barra Lateral
#================================================

st.header('Fome Zero! ')


image_path = 'logo.png'
image = Image.open(image_path)
st.sidebar.image(image, width=120)


st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown('''---''')

st.sidebar.markdown('### Filtros')

country_options = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar os Restaurantes',
    ["India", "Australia", "Brazil", "Canada", "Indonesia", "New Zeland", "Philippines", "Qatar", "Singapure", "South Africa", "Sri Lanka", "Turkey", "United Arab Emirates", "England", "United States of America"],
    default = ["India", "Australia", "Brazil", "Canada", "Indonesia", "New Zeland", "Philippines", "Qatar", "Singapure", "South Africa", "Sri Lanka", "Turkey", "United Arab Emirates", "England", "United States of America"])


#filtro da visão países
linha_selecionada = df1['Country'].isin(country_options)
df1 = df1.loc[linha_selecionada, :]


st.sidebar.markdown('''---''')

st.sidebar.markdown('###### Powered by Mateus')
st.sidebar.markdown('###### Data Scientist @ Comunidade DS')


#====================================================
#Layout do streamlit 
#====================================================


st.subheader('O Melhor lugar para encontrar seu mais novo restaurante favorito!')

st.markdown('Temos as seguintes marcas dentro da nossa plataforma:')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        #st.subheader('Restaurantes Cadastrados')
        registro = df1['Restaurant ID'].nunique()
        col1.metric('Restaurantes Cadastrados', registro)
    with col2:
        cadastro = df1['Country Code'].nunique()
        col2.metric('Países Cadastrados', cadastro)
    with col3:
        cities = df1['City'].nunique()
        col3.metric('Cidades Cadastradas', cities)
    with col4: 
        votos = df1['Votes'].sum()
        col4.metric('Avaliações feitas na Plataforma', votos)
    with col5:
        culinaria = df["Cuisines"].nunique()
        col5.metric('Tipos de Culinária', culinaria)
        
with st.container():
    #df_aux = df1.loc[:, ['City', 'Latitude', 'Longitude']]
    #map = folium.Map()
    #for index, location_info in df_aux.iterrows():
     #   folium.Marker([location_info['Latitude'], location_info['Longitude']], popup=location_info[['City']], icon=folium.Icon(color='green', icon = 'ok-sign'), 
      #             ).add_to(map)
                  
    
    #folium_static(map, width = 1024, height = 600)
    locais = df1[['Latitude', 'Longitude']].values.tolist()

    mapa = folium.Map(location=[121.009787, 14.447615], zoom_start = 5)

    MarkerCluster(locations=locais).add_to(mapa)
    mapa.save('mapa.html')

    folium_static(mapa, width = 1024, height = 600)
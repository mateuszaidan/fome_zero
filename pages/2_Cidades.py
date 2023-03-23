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
df=pd.read_csv('dataset/zomato.csv')
#---------------------------------------------------------------------------------

#Limpeza de Dados

#mudando o nome da coluna restaurante 
df = df.rename(columns={'Restaurant Name': 'Number of Restaurants' })

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

st.header('🏙 Visão Cidades')

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


with st.container():
    st.markdown('''---''')
    cols = ['Restaurant Code', 'City']
    df_aux = df1.loc[:, ['City', 'Number of Restaurants', 'Country']].groupby(['City', 'Country']).count().reset_index()

    df_aux = df_aux.sort_values(['Number of Restaurants'], ascending = False).head(10)
    fig = px.bar(df_aux, x = 'City', y = 'Number of Restaurants', color = 'Country', title = 'TOP 10 CIDADES COM MAIS RESTAURANTES NA BASE DE DADOS')
    st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
    #cidades com nota maior que 4
        nota_maior = df1['Aggregate rating'] > 4.0
        city_max = df1.loc[nota_maior, ['Country','City', 'Aggregate rating']].groupby(['City', 'Country']).count().reset_index()
        df_aux = city_max.sort_values(['Aggregate rating'], ascending = False).head(7)
        fig = px.bar(df_aux, x = 'City', y = 'Aggregate rating', color = 'Country', title = 'Cidades com Restaurantes com média avaliação acima 4 ')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        nota_menor = df1['Aggregate rating'] < 2.5
        city_min = df1.loc[nota_menor, ['Country', 'City', 'Aggregate rating']].groupby(['Country', 'City']).count().reset_index()
        df_aux = city_max.sort_values(['Aggregate rating'], ascending = False).head(7)
        fig = px.bar(df_aux, x = 'City', y = 'Aggregate rating', color = 'Country', title = 'Cidades com Restaurantes com média avaliação abaixo 2.5 ')
        st.plotly_chart(fig, use_container_width=True)
        
with st.container():
    cols = ['Country', 'City', 'Cuisines']

    df_aux = df1.loc[:, cols].groupby(['Country', 'City']).nunique().reset_index()
    df_aux = df_aux.sort_values(['Cuisines'], ascending = False).head(10)
    fig = px.bar(df_aux, x='City', y = 'Cuisines', color = 'Country', title = 'Top 10 Cidades mais restaurantes com tipos culinários distintos')
    st.plotly_chart(fig, use_container_width=True)
        
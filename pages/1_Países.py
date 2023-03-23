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
df = pd.read_csv('dataset/zomato.csv')
#---------------------------------------------------------------------------------

#Limpeza de Dados

#Mudando o nome da coluna do nome do restaurante
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

st.header('🌎Visão Países')
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
    colus = ['Country', 'Number of Restaurants']
    df_aux = df1.loc[:, colus].groupby(['Country']).count().reset_index()
    df_aux = df_aux.sort_values(['Number of Restaurants'], ascending = False).head()
    fig = px.bar(df_aux, x = 'Country', y = 'Number of Restaurants', title="Quantidade de Restaurantes Registrados por País")
    st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    colus = ['Country', 'City']
    df_aux = df1.loc[:, colus].groupby(['Country']).nunique().reset_index()
    df_aux = df_aux.sort_values(['City'], ascending = False).head()
    Países = 'Country'
    fig = px.bar(df_aux, x=Países, y='City', title = 'Quantidade de Cidades Registrados por País')
    st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    col1, col2 =  st.columns(2)
    with col1:
        colus = ['Country', 'Votes']
        df_aux = df1.loc[:, colus].groupby(['Country']).mean().reset_index()
        df_aux = df_aux.sort_values(['Votes'], ascending = False).head()
        fig = px.bar(df_aux, x = 'Country', y ='Votes', color = 'Country', title = 'Média de Avaliações feitas por País')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        colus = ['Country', 'Aggregate rating']
        df_aux = df1.loc[:, colus].groupby(['Country']).mean().reset_index()
        df_aux = df_aux.sort_values(['Aggregate rating'], ascending = False).head()

        fig = px.bar(df_aux, x = 'Country', y = 'Aggregate rating', title = 'Média de Avaliação por país')
        st.plotly_chart(fig, use_container_width=True)

        
with st.container():
    colus = ['Country', 'Average Cost for two']
    df_aux = df1.loc[:, colus].groupby(['Country']).mean().reset_index()
    df_aux = df_aux.sort_values(['Average Cost for two'], ascending = False).head()
    fig = px.bar(df_aux, x = 'Country', y = 'Average Cost for two', title = 'Média de Preço de um prato para duas pessoas por País')
    st.plotly_chart(fig, use_container_width=True)
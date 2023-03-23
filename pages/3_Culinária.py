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

st.header('🍝 Visão Tipos de Culinária')
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

num_city = st.sidebar.slider('Selecione a quantidade de Restaurantes que deseja visualizar', min_value= 1, max_value= 50 )
#linha_selecionada = df1['Restaurant Name']
#df1 = df1.loc[linha_selecionada, :]


#barra de rolagem
#linha_selecionada = df1['Country'].isin(country_options)

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
    st.subheader('Melhores Restaurantes dos Principais tipos Culinários')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("###### American: 5 Napkin Burger")
        nota = 4.9
        st.header("{}/5.0".format(nota))
        
    with col2: 
        st.markdown("###### Italian: Amano Restaurant")
        st.header("{}/5.0".format(nota))
    with col3:
        st.markdown("###### Japonese: Chotto Matte")
        st.header("{}/5.0".format(nota))
    with col4: 
        st.markdown("###### Chinese: Buddakan")
        st.header("{}/5.0".format(nota))
    with col5:
        st.markdown("###### Brazilian: Braseiro da Gávea")
        st.header("{}/5.0".format(nota))
        
        
        
#melhores notas

        #american = df1.loc[culinaria, ['Cuisines', 'Restaurant Name', 'Aggregate rating']].max()
        #col1.metric(american, "American: Zingerman's Roadhouse")

with st.container():
    
    st.markdown('## Top {} Restaurantes'.format(num_city))
    cols = ['Restaurant Name', 'Country', 'City', 'Cuisines', 'Average Cost for two', 'Aggregate rating', 'Votes']
#melhores notas

    df_aux = df1.loc[:, cols].groupby(['Restaurant Name', 'Cuisines']).max().reset_index().sort_values(['Aggregate rating'], ascending = False).head(num_city)
    st.dataframe(df_aux)
    
with st.container():
    col1, col2 = st.columns(2)
    with col1: 
        df_aux = df1.loc[:,['Cuisines', 'Aggregate rating']].groupby(['Cuisines']).mean().reset_index()
        df_aux  = df_aux.sort_values(['Aggregate rating'], ascending = False).head(num_city)

        fig = px.bar(df_aux, x='Cuisines', y='Aggregate rating', title = 'Top {} Melhores Tipos de Culinárias'.format(num_city))
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        df_aux = df1.loc[:,['Cuisines', 'Aggregate rating']].groupby(['Cuisines']).mean().reset_index()
        df_aux  = df_aux.sort_values(['Aggregate rating'], ascending = True).head(10)

        fig = px.bar(df_aux, x='Cuisines', y='Aggregate rating', title = 'Top {} Piores Tipos de Culinárias'.format(num_city))
        st.plotly_chart(fig, use_container_width=True)
        
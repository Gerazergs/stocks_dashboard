import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

button_clicked = st.button("Re-load")



def categorical(palabras:int, listado:list):
    
    return listado[palabras]
    

def create_random_number(numero_1, numero_2):
    return random.randint(numero_1, numero_2)

def create_random_number2(numero_1, numero_2):
    size = numero_2
    rng = default_rng(numero_1)
    return rng.normal(size=size)



df = pd.read_csv('my_new_portfolio.csv')
df.drop('Unnamed: 0', axis = 1, inplace =True)

df2 = pd.read_csv('SPY500_descarga.csv')

df3 = pd.read_csv('SPY500_normalizated.csv')

df4 = pd.read_csv('sectors.csv')

st.write('Mi first app with stramlit : just ploting random samples')

st.table(df.head())

row2_spacer1, row2_spacer3 = st.columns(
    (.1, .03)
    )


lista = df['stocks'].values.tolist()
df4 = df4[df4['Symbol'].isin(lista)]

with row2_spacer1:
    figura = px.bar(
                df4,
                x='Symbol', y='GICS Sector',
            )
    figura.update_layout(height=300, width=600, title_text=f'Sector analysis')
    st.write(figura)
with row2_spacer3:

    figura2= px.bar(
                df4,
                x='Symbol', y='GICS Sub-Industry',
            )
    figura2.update_layout(height=300, width=600, title_text=f'sub Sector analysis')
    st.write(figura2)
# figura2 = px.bar(
#             df4,
#             x='Symbol', y='Headquarters Location',
#         )
# figura2.update_layout(height=300, width=600, title_text=f'radius analysis')


# fig = px.line_polar(df, r="frequency", theta="direction", color="strength", line_close=True,
#                     color_discrete_sequence=px.colors.sequential.Plasma_r,
#                     template="plotly_dark",)



with row2_spacer1:
    for i in lista:
        #with st.echo(code_location='below'):
        #This code is how i made the figure
        
        fig = px.scatter(
            df3,
            x='SPY',
            y=i,
            trendline="ols",
        )
        fig.update_layout(height=300, width=600, title_text=f'Beta and alpha analysis for SPY vs {i}')

        st.write(fig)
        with row2_spacer3:
            fig2 = px.line(
            df2,
            x='Date',
            y=i,
            )
            fig2.update_layout(height=300, width=600, title_text=f'Stock {i} two year performance')
            st.write(fig2)



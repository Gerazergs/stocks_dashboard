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


df = pd.read_csv('my_new_portfolio.csv')
df.drop('Unnamed: 0', axis = 1, inplace =True)

df2 = pd.read_csv('SPY500_descarga.csv')

df3 = pd.read_csv('SPY500_normalizated.csv')

df4 = pd.read_csv('sectors.csv')

df5 = pd.read_csv('Full_procesated_SPY500.csv')
df5.columns =['stocks','std','rendimiento','riesgo','coeficiente_variacion','beta','alfa','Riesgo_sistematico','Riesgo_no_sistematico','sharpie','teynor']


st.write('Mi first app with stramlit : just ploting selected features')

Filter_1 = st.sidebar.selectbox(
    "select greater than this risk percentage",
    ('Min%','0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%')
)

Filter_2 = st.sidebar.selectbox(
    "select lower than this risk percentage",
    ('30%','40%','50%','60%','70%','80%','90%','100%','Max%')
)




st.write('greater than this risk selected:', Filter_1)
st.write('lower than this risk selected:', Filter_2)
if Filter_1 != 'Min%':
    Filter_1 = int(Filter_1.replace('%',''))/100
    df5 =df5[df5['riesgo']>Filter_1]
    df = df5
else:
    df = df5
    
if Filter_2 != 'Max%':
    Filter_2 = int(Filter_2.replace('%',''))/100
    df =df[df['riesgo']<Filter_2]
else:
    df

df = df.sort_values(['sharpie', 'teynor'], ascending = False)
df = df.iloc[0:6,:]

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

x=2
for i in lista:
    if x % 2 == 0:
        with row2_spacer1:
            x+=1
            df3[i]=df3[i].astype('float')
            mean =df3[i].mean()
            std =mean-df3[i].std()
            std_plus =mean+df3[i].std()
            hist = px.histogram(df3, x=i)
            hist.add_shape(type="line",x0=mean, x1=mean, y0 =0, y1=120 , xref='x', yref='y',
                    line = dict(color = 'blue', dash = 'dash'))
            hist.add_shape(type="line",x0=std, x1=std, y0 =0, y1=120 , xref='x', yref='y',
                        line = dict(color = 'red', dash = 'dash'))
            hist.add_shape(type="line",x0=std_plus, x1=std_plus, y0 =0, y1=120 , xref='x', yref='y',
                        line = dict(color = 'red', dash = 'dash'))
            hist.update_layout(height=300, width=600, title_text=f'histogram of {i}')
            st.write(hist)
            
    else:
        with row2_spacer3:
            x+=1
            df3[i]=df3[i].astype('float')
            mean =df3[i].mean()
            std =mean-df3[i].std()
            std_plus =mean+df3[i].std()
            hist = px.histogram(df3, x=i)
            hist.add_shape(type="line",x0=mean, x1=mean, y0 =0, y1=120 , xref='x', yref='y',
                    line = dict(color = 'blue', dash = 'dash'))
            hist.add_shape(type="line",x0=std, x1=std, y0 =0, y1=120 , xref='x', yref='y',
                        line = dict(color = 'red', dash = 'dash'))
            hist.add_shape(type="line",x0=std_plus, x1=std_plus, y0 =0, y1=120 , xref='x', yref='y',
                        line = dict(color = 'red', dash = 'dash'))
            hist.update_layout(height=300, width=600, title_text=f'histogram of {i}')
            st.write(hist)
        

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



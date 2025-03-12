import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_map_estado
from graficos import grafico_rec_mensal, grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedores, grafico_venda_vendedores

st.set_page_config(layout='wide')
st.title("Dashboards de vendas :shopping_trolley:")

aba1, aba2, aba3 = st.tabs(['Receita', 'Vendedores', 'DataSet'])

st.sidebar.title('Filtro de Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores', 
    df['Vendedor'].unique(),

)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

with aba1:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$ '))
        fig = grafico_map_estado()
        st.plotly_chart(fig, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)

    with coluna2:
        st.metric('Quantidade de vendas', format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)
        
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores)

    with coluna2:
        st.plotly_chart(grafico_venda_vendedores)    

with aba3:
    st.dataframe(df)        
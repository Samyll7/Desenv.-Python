import streamlit as st
import pandas as pd
import plotly.express as px

# Dados
dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniela"],
    "cidade": ["SP", "RJ", "SP", "MG"],
    "salario": [3000, 5000, 4000, 3500],
    "categoria_salario": ["Baixo", "Alto", "Médio", "Médio"]
}

df = pd.DataFrame(dados)

# SIDEBAR (filtro)
st.sidebar.title("Filtro")

categoria = st.sidebar.selectbox(
    "Escolha a categoria",
    df["categoria_salario"].unique()
)

df_filtrado = df[df["categoria_salario"] == categoria]

# GRÁFICO
fig = px.bar(
    df_filtrado,
    x="cidade",
    y="salario",
    color="categoria_salario",
    title="Salários por cidade"
)

# EXIBIR
st.title("Dashboard Simples")
st.dataframe(df_filtrado)
st.plotly_chart(fig)
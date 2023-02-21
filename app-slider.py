import streamlit as st

st.title("App con sider")

sidebar = st.sidebar

sidebar.title("Este es el sidebar")
sidebar.write("Datos del sidebar")

st.header ("Informacion sobre el Conjunto de Datos")
st.header ("Descripcion de los datos")

st.write("""
Este es un simple ejemplo de una app para predecir
¡Esta app predice mis datos!
""")

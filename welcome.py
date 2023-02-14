import streamlit as st

def bienvenida(nombre):
    mensaje = "bienvenido /a/e e :" + nombre
    return mymensaje

myname = st.text_input("nombre: ")
if (myname):
    mensaje = bienvenida(myname)
    st.write(" Result : {mensaje}")

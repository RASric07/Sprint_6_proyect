import pandas as pd
import plotly.express as px 
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.checkbox('Histograma') # crear un botón
scatter_button = st.checkbox("Diagrama de dispersion") 

st.header('Practica app web muestra de histograma y dispersion')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
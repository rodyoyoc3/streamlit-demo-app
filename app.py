
# PARTE 0:  IMPORTACIÓN DE LIBRERIAS

import streamlit as st  # Importa la librería Streamlit para crear aplicaciones interactivas
from datetime import datetime  # Importa datetime para trabajar con fechas y horas

#PARTE 1: CREACIÓN SCRIPT INICIAL
# Título y Subtítulos de la Aplicación
# Título principal 
st.title(" MI PRIMERA APLICACIÓN EN STREAMLIT UCG ")

# Subtítulo 
st.subheader("Nombre y Apellido del Estudiante")

# Descripción o introducción
st.write("Funciones principales de Streamlit")
st.write("Universidad Casa Grande")

# PARTE 2: WIDGETS y SIDEBAR

#Implementación de Widgets Interactivos:

# Slider para seleccionar una edad entre 0 y 100 años, se establece como valor inicial 45 
edad = st.slider("Selecciona tu Edad", 0, 100, 45)

# Texto para ingresar nombres y apellidos
nombre_completo = st.text_input("Ingrese su Nombre Completo", placeholder="Escribe aquí...")

# Slider para seleccionar un mes del 1 al 12, se establece como valor inicial 1 (1ER MES)
mes = st.slider("Selecciona un Mes", 1, 12, 1) 

# Checkbox para aceptar términos y condiciones
acepta_terminos = st.checkbox("¿Acepta los Términos y Condiciones?")

# Radio Buttons para seleccionar el género
genero = st.radio("Seleccione su Género", ["Masculino", "Femenino"])

# Selectbox para seleccionar un país de una lista
pais = st.selectbox("Selecciona tu País", ["Argentina", "Brasil", "Chile", "Colombia", "México", "España", "Ecuador", "Perú", "Estados Unidos"])

# Widget para cargar un archivo (CSV, TXT o XLSX)
archivo = st.file_uploader("Cargar un Archivo", type=["csv", "txt", "xlsx"])

# Fecha con valor predeterminado como la fecha actual
fecha = st.date_input("Selecciona una Fecha", value=datetime.now().date())

# Hora con valor predeterminado como la hora actual
hora = st.time_input("Selecciona una Hora", value=datetime.now().time())

# Botón para enviar la información ingresada
if st.button("Enviar Información"):
    # Muestra un mensaje de éxito con la información ingresada
    st.success(f"""
    Información Enviada:
    - Edad: {edad}
    - Nombre Completo: {nombre_completo}
    - Género: {genero}
    - País: {pais}
    - Fecha Seleccionada: {fecha}
    - Hora Seleccionada: {hora}
    """)


# Widgets en la Barra Lateral


# Título para la barra lateral
st.sidebar.title("Barra Lateral Interactiva")

# Breve descripción de la barra lateral
st.sidebar.write("Algunos widgets están disponibles aquí.")

# Slider para seleccionar una edad en la barra lateral
sidebar_edad = st.sidebar.slider("Selecciona tu Edad (Sidebar)", 0, 100, 45)

# Selectbox para seleccionar un país en la barra lateral
sidebar_pais = st.sidebar.selectbox("Selecciona tu País (Sidebar)", ["Argentina", "Brasil", "Chile", "Colombia", "México", "España", "Ecuador", "Perú", "Estados Unidos"])

# Checkbox para aceptar términos en la barra lateral
sidebar_acepta = st.sidebar.checkbox("Acepta los Términos y Condiciones (Sidebar)")

# Botón en la barra lateral para confirmar la información ingresada
if st.sidebar.button("Confirmar en Sidebar"):
    # Muestra un mensaje de éxito en la barra lateral
    st.sidebar.success(f"Información desde la barra lateral:\nEdad: {sidebar_edad}\nPaís: {sidebar_pais}")


# PARTE 3: DOCUMENTACIÓN Y RECURSOS


# Enlace a la documentación oficial página wed de Streamlit
st.markdown("### Documentación Oficial de Streamlit")
st.markdown("[Consulta la API Reference de Streamlit aquí](https://docs.streamlit.io/library/api-reference).")


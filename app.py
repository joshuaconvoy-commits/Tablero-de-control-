import pandas as pd
import streamlit as st

url = 'https://github.com/joshuaconvoy-commits/Curso-de-IA-universidad-de-Medell-n/raw/refs/heads/main/datos_generales_ficticios.csv'
df = pd.read_csv(url, sep=';', encoding= 'latin 1')

st.dataframe(df)

#Crear lista de las columnas de Interes
seleccion_columnas = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
#Actualizo el dataframe -df- con las columnas de interes, ordenadas por fecha y reseteo el indice
df = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

st.dataframe(df)

#convierto la columna FECHA_HECHOS a formato fecha
df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')
# Extraigo solo la fecha (sin la hora)
df['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

#CALCULO DE MUNICIPIO CON MAS DELITOs
max_municipio = df['MUNICIPIO_HECHOS'].value_counts().value_counts().iloc[0]
st.write(f'Municipio TOP Delitos:{max_municipio}')
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]

#CONSTRUIR LA PAGINA
st.set_page_config(page_title="Dasbohard de Delitos - Fiscalía", layout="centered")
st.header("Dasbohard de Delitos - Fiscalía")
#st.markdown(f"<center><h2>Dasbohard de Delitos - Fiscalía</h2></center>", unsafe_allow_html=True)

st.dataframe(df)

st.write(f"### Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} reportes")
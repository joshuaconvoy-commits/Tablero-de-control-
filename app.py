import pandas as pd
import streamlit as st
import plotly.express as px

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
max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
st.write(f'Municipio TOP Delitos:{max_municipio}')
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]

#CALCULO DE LA ETAPA QUE MAS VECES SE PRESENTA
# Ya que value_counts() genera un dataframe ordenada, traigo solo EL PRIMER iNDICE. index[0]
etapa_mas_frecuente = df['ETAPA'].value_counts().index[0]
# Ya que value_counts() genera un dataframe ordenada, traigo solo EL PRIMER iNDICE. iloc[0]
cant_etapa_mas_frecuente = df['ETAPA'].value_counts().iloc[0]
st.subheader('Comportamiento Delitos')
delitos = df['DELITO'].value_counts()
st.write(delitos)
st.bar_chart(delitos)

st.subheader('Comportamiento Departamentos')
departamentos = df['DEPARTAMENTO'].value_counts()
st.write(departamentos)
st.bar_chart(departamentos)

st.subheader('Distribución por departamentos')
fig = px.pie(
    values=departamentos.values,
    names=departamentos.index             
)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(showlegend=False, height=400)
st.plotly_chart(fig)

df_delitos = df.groupby(['DEPARTAMENTO', 'DELITO']).size().reset_index(name='conteo')
fig = px.bar(df_delitos, x='DEPARTAMENTO', y='conteo', color='DELITO', barmode='stack')
st.plotly_chart(fig)
st.write(df_delitos)

st.subheader('Tipo de Delito')
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)

                                            #CONSTRUIR PAGINA
st.set_page_config(page_title="Dashboard Delitos - Fiscalía", layout="wide")
st.markdown(
    """
    <style>
        .block-container {
            padding: 1rem 2rem 2rem 2rem;
            max-width: 1600px;
    }
    </stile>
    """,
    unsafe_allow_html=True
)

st.image('img/Fiscalia.png', use_container_width=True)
st.markdown("#<font color = #3B668C> TITULO </font>", unsafe_allow_html=True)

#Grafico de barras apiladas por departamento y tipó de delito
st.subheader('Delitos por Departamentos')
df_delitos = df.groupby(['DEPARTAMENTO', 'DELITO']).size().reset_index(name='conteo')
fig = px.bar(df_delitos, x='DEPARTAMENTO', y='conteo', color='DELITO', barmode='stack')
st.plotly_chart(fig,key= "bar_departamentos")
fig.update_layout(showlegend=False, height=200)

#CREAR 4 COLUMNAS PARA LAS TARJETAS
col1, col2, col3, col4 = st.columns(4)

with col1:

#TARJETAS
    ## TARJETA 1 - MUNICIPIO CON MAS DELITOS
    st.markdown(f"""<h3 style=
                'color: #F2A88D;
                background-color: #FFF6F5;
                border: 2px solid #F2A88D;
                border-radius: 10px; padding: 10px;
                text-align: center'>
                Municipios con mas delitos: {max_municipio}</h3><br>""",
                unsafe_allow_html=True)

with col2:
    ## tARJETA 2 - cANTIDAD DE DELITOS EN EL MUNICIPIO CON MAS DELITOS
    st.markdown(f"""<h3 style=
                'color: #F2A88D;
                background-color: #FFF6F5;
                border: 2px solid #F2A88D;
                border-radius: 10px; padding: 10px;
                text-align: center'>
                Delitos Repotados<br>{max_cantidad_municipio}</h3><br>""",
                unsafe_allow_html=True)

                    

                    # DATOS VIEJOS

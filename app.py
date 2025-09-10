import pandas as pd
import streamlit as st

url= 'https://github.com/joshuaconvoy-commits/Curso-de-IA-universidad-de-Medell-n/raw/refs/heads/main/datos_generales_ficticios.csv'
df= pd.read_csv(url, sep=';', encoding='utf-8') 

print(df) 


import streamlit as st
st.set_page_config(page_title="Asistente de Investigación", layout="wide")  #  Esta línea va primero
from modulos.react import ejecutar_agente_react
from modulos.nlp_process import summarize_text
from utils.wordcloud import generate_wordcloud
from PIL import Image
from utilis import cargar_api_keys

TAVILY_API_KEY, OPENAI_API_KEY = cargar_api_keys()


# UI
st.title(" Asistente de Investigación Digital")
query = st.text_input("Ingrese un tema de investigación:")

if query:
    st.info("Buscando información...")
    resultado = ejecutar_agente_react(query)
    st.subheader(" Resultados de la búsqueda")
    for res in resultado:
        st.markdown(f"**{res['title']}**\n\n{res['snippet']}\n\n[Ver más]({res['url']})")

    st.subheader("Resumen generado")
    resumen = summarize_text(resultado)
    st.write(resumen)

    st.subheader(" Nube de Palabras")
    imagen = generate_wordcloud(resultado)
    st.image(imagen, use_column_width=True)

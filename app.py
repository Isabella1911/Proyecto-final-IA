
import streamlit as st
from react import ejecutar_agente_react
from nlp_process import summarize_text
from utils.wordcloud import generate_wordcloud
from utilis import cargar_api_keys
from PIL import Image

# Configuración de página (debe ir al principio)
st.set_page_config(page_title="Asistente de Investigación", layout="wide")

# Cargar API Keys
TAVILY_API_KEY, OPENAI_API_KEY = cargar_api_keys()

# UI Mejorada
st.title("🔍 Asistente de Investigación Digital")
st.markdown("---")

# Input de usuario con mejor diseño
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input("Ingrese un tema de investigación:", placeholder="Ej: Últimos avances en inteligencia artificial")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        buscar_btn = st.button("Buscar", type="primary")

# Procesamiento cuando se ingresa una consulta
if buscar_btn and query:
    with st.spinner("Buscando y analizando información..."):
        try:
            # 1. Ejecutar el agente de búsqueda
            resultado = ejecutar_agente_react(query)
            
            # Mostrar resultados en pestañas
            tab1, tab2, tab3 = st.tabs(["📄 Resultados", "📝 Resumen", "☁️ Nube de Palabras"])
            
            with tab1:
                st.subheader("🔎 Resultados de la búsqueda")
                if isinstance(resultado, str):
                    st.markdown(resultado)
                else:
                    st.warning("El formato de resultados ha cambiado. Mostrando respuesta completa:")
                    st.json(resultado)
            
            with tab2:
                st.subheader("Resumen generado")
                resumen = summarize_text(str(resultado))  # Asegurar string
                st.write(resumen)
            
            with tab3:
                st.subheader("Nube de Palabras")
                try:
                    # Asegurarse de que el texto no esté vacío
                    if resultado and str(resultado).strip():
                        # Generar y mostrar el WordCloud
                        wordcloud_img = generate_wordcloud(str(resultado))
                        st.image(wordcloud_img, 
                                use_column_width=True, 
                                caption="Términos más relevantes")
                    else:
                        st.warning("No hay suficiente texto para generar la nube de palabras")
                except Exception as e:
                    st.error(f"Error generando nube de palabras: {str(e)}")
                    
        except Exception as e:
            st.error(f" Error en el procesamiento: {str(e)}")
            st.exception(e)
            
elif buscar_btn and not query:
    st.warning("Por favor ingrese un tema de investigación")

# Notas adicionales
st.markdown("---")
st.caption("Nota: Este asistente utiliza inteligencia artificial para buscar y analizar información en tiempo real.")

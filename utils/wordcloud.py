# utils/wordcloud_gen.py
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

def generate_wordcloud(text):
    """
    Genera una nube de palabras a partir del texto y devuelve una imagen PIL
    """
    try:
        # Configuración del WordCloud
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            max_words=100,
            contour_width=3,
            contour_color='steelblue'
        ).generate(text)
        
        # Crear figura
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        
        # Guardar en un buffer en lugar de archivo
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', bbox_inches='tight')
        plt.close()
        
        # Crear imagen PIL desde el buffer
        img_buffer.seek(0)
        img = Image.open(img_buffer)
        
        return img
        
    except Exception as e:
        print(f"Error generando WordCloud: {str(e)}")
        raise

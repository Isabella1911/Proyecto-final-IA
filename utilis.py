import os
from dotenv import load_dotenv

def cargar_api_keys():
    """
    Carga las claves de API desde el archivo .env
    
    Returns:
        tuple: (TAVILY_API_KEY, OPENAI_API_KEY)
    """
    # Carga las variables de entorno desde el archivo .env
    load_dotenv()
    
    # Obtiene las claves API desde las variables de entorno
    tavily_api_key = os.environ.get("TAVILY_API_KEY")
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    
    # Verificación de claves
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY no encontrada en el archivo .env")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY no encontrada en el archivo .env")
    
    return tavily_api_key, openai_api_key
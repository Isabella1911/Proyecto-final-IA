# Actualiza estas importaciones según las advertencias de deprecación
from langchain_community.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain_community.tools import TavilySearchResults

import os
import sys

# Añadir el directorio raíz al path de Python para importaciones absolutas
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Ahora importar utils como un módulo absoluto
from utils import cargar_api_keys

# Cargar las claves API
TAVILY_API_KEY, OPENAI_API_KEY = cargar_api_keys()

def ejecutar_agente_react(pregunta):
    # LLM
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-4", temperature=0)

    # Tavily tool
    search_tool = TavilySearchResults(api_key=TAVILY_API_KEY)

    tools = [
        Tool(
            name="Tavily Search",
            func=search_tool.run,
            description="Realiza búsquedas actuales en la web para responder preguntas con información reciente"
        )
    ]

    agente = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    respuesta = agente.run(pregunta)
    return respuesta
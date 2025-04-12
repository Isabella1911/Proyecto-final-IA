from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
import os
import sys

# Configuración de paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from utilis import cargar_api_keys

TAVILY_API_KEY, OPENAI_API_KEY = cargar_api_keys()

# Herramienta para respuestas directas
@tool
def responder_pregunta(input: str) -> str:
    """Usa esta herramienta para responder preguntas directamente cuando no necesites buscar información."""
    return input

def ejecutar_agente_react(pregunta: str) -> str:
    # 1. Configurar el LLM
    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name="gpt-4",
        temperature=0,
        max_tokens=2000
    )

    # 2. Configurar herramientas
    tools = [
        TavilySearchResults(api_key=TAVILY_API_KEY, name="BuscadorWeb"),
        responder_pregunta
    ]

    # 3. Plantilla de prompt CORREGIDA (incluye agent_scratchpad)
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Eres un asistente inteligente. Responde preguntas usando las herramientas disponibles.
        
        Instrucciones:
        1. Para preguntas sobre información actual (fechas, noticias, etc.) usa BuscadorWeb
        2. Para conocimiento general usa responder_pregunta"""),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")  # Variable requerida
    ])

    # 4. Crear el agente
    agent = create_tool_calling_agent(llm, tools, prompt)

    # 5. Configurar ejecutor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=3
    )

    # 6. Ejecutar
    try:
        respuesta = agent_executor.invoke({"input": pregunta})
        return respuesta["output"]
    except Exception as e:
        return f"Error: {str(e)}"
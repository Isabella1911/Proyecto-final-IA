# utils/nlp_processing.py
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def summarize_text(text_list):
    joined_text = "\n\n".join(text_list)
    
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Resume el siguiente texto en un párrafo conciso:\n\n{text}"
    )
    
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-4", temperature=0.5)
    chain = LLMChain(llm=llm, prompt=prompt)

    summary = chain.run({"text": joined_text})
    return summary

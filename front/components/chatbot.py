import os
import requests
import dotenv
import json
import time

from pathlib import Path
import streamlit as st

# Cargar variables de entorno
dotenv.load_dotenv()


def show():
  st.title("Chabot")
  
  document_title = st.text_input("Titulo del documento")
  document_type = "documento-tabla"
  query_text = st.text_input("Ingrese la pregunta al documento")
  
  if st.button("Preguntar a la tabla", key="procesar"): 
    url = f"http://{os.getenv('API_HOST')}:{os.getenv('API_PORT')}/"
    endpoint = "rag-tables/api/v1/ask"
    with st.spinner("Procesando pregunta..."):
      payload = {
        "title": document_title,
        "document_type": document_type,
        "query": query_text
      }

      headers = {"Content-Type": "application/json"}
      
      response = requests.post(
        url + endpoint,
        json=payload,
        headers=headers
      )
    
    if response.status_code in [200, 201]:
      st.success(f"Request exitoso- {response.status_code}")
      for key, value in response.json().items():
        st.write(f"{key}: {value}")
    else:
      st.error(
        f"Request fallido con status code {response.status_code}: {response.text}"
      )
    

  
  

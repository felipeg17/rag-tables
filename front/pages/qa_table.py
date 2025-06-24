import os
import requests
import base64
import dotenv
import time
import io

from pathlib import Path
import streamlit as st
import pandas as pd

# Cargar variables de entorno
dotenv.load_dotenv()


def show():
  st.title("Cargar documento tipo tabla en .CSV o .XLSX")
  doc_file = st.file_uploader("Cargar archivo CSV o XLSX", type=["csv", "xlsx"])
  if doc_file:
    file_name = doc_file.name
    ext = os.path.splitext(file_name)[1].lower()
    
    # doc_bytes = doc_file.read()
    document_title = st.text_input("Titulo del documento")
    document_type = "documento-tabla"
    
    if ext == ".csv":
      doc_bytes = doc_file.read()
    elif ext == ".xlsx":
      df = pd.read_excel(doc_file)
      csv_buffer = io.StringIO()
      df.to_csv(csv_buffer, index=False)
      doc_bytes = csv_buffer.getvalue().encode('utf-8')
    else:
      st.error("Solo se permiten archivos .csv o .xlsx")
      return
    
    
    if st.button("Cargar documento", key="procesar"): 
      url = f"http://{os.getenv('API_HOST')}:{os.getenv('API_PORT')}/"
      endpoint = "rag-tables/api/v1/upload"
      with st.spinner("Procesando documento..."):
        payload = {
          "title": document_title,
          "document_type": document_type,
          "document_bytes": base64.b64encode(doc_bytes).decode('utf-8')
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


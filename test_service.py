import logging
import pdb
import base64
import requests
import dotenv

from pathlib import Path

# Cargar variables de entorno
dotenv.load_dotenv()

# Configuracion de logging
logging.basicConfig(
  level=logging.INFO, 
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
  DOCS_PATH = Path(__file__).parent 
  folder_path = DOCS_PATH / "documents"
  file_name = "wa-tax-table.csv"
  document_title = "wa-tax-table"
  file_path = str(folder_path / file_name)
  
  try:
    with open(file_path, 'rb') as file:
      pdf_bytes = file.read()
      logging.info(f"Archivo {file_path} cargado correctamente")
  except Exception as e:
    logging.error(f"Error al cargar el archivo {file_path}:::{e}")

  url = "http://localhost:8108/rag-tables/api/v1/upload"
  headers = {
    "Content-Type": "application/json"
  }
  payload = {
    "title": document_title,
    "document_type": "documento-tabla",
    "document_bytes": base64.b64encode(pdf_bytes).decode('utf-8')
  }
  pdb.set_trace()

  response = requests.post(
    url,
    headers=headers,
    json=payload
  )

  if response.status_code in [200, 201]:
    logging.info(f"Respuesta exitosa: {response.status_code}")
    logging.info(f"Contenido de la respuesta: {response.json()}")
  else:
    logging.error(f"Error en la solicitud: {response.status_code}")
    logging.error(f"Contenido de la respuesta: {response.text}")
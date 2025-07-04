FROM python:3.10-slim

WORKDIR /app

# Crear requirements específicos para frontend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código del frontend
COPY . /app/

EXPOSE 8501

# Configurar Streamlit
RUN mkdir -p /root/.streamlit
RUN echo '\
[server]\n\
port = 8501\n\
address = "0.0.0.0"\n\
headless = true\n\
enableCORS = false\n\
enableXsrfProtection = false\n\
' > /root/.streamlit/config.toml

CMD ["streamlit", "run", "front.py", "--server.port=8501", "--server.address=0.0.0.0"]
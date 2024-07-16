# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para o diretório de trabalho
COPY . .

# Defina a variável de ambiente para o Django
ENV DJANGO_SETTINGS_MODULE=goldenraspberry.settings

# Execute as migrações e o servidor de desenvolvimento
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

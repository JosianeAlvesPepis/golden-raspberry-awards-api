# API Golden Raspberry Awards

Esta API permite obter informações sobre os vencedores do prêmio de Pior Filme do Golden Raspberry Awards.

## Como Rodar a Aplicação

### Usando Docker

1. Clone o repositório:
    ```bash
    git clone JosianeAlvesPepis/golden-raspberry-awards-api
    cd golden-raspberry-awards-api
    ```

2. Construa a imagem Docker:
    ```bash
    docker-compose build
    ```

3. Inicie os serviços Docker:
    ```bash
    docker-compose up
    ```

4. Acesse a aplicação:
    Abra o navegador e acesse `http://localhost:8000/awards/intervalos/` para verificar os intervalos de prêmios.

### Usando o Terminal da Máquina

1. Clone o repositório:
    ```bash
    git clone JosianeAlvesPepis/golden-raspberry-awards-api
    cd golden-raspberry-awards-api
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv env
    source env/bin/activate  # No Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

4. Carregue os dados do CSV:
    Por padrão, o arquivo `movielist.csv` na raiz do projeto será carregado ao iniciar o servidor. Para usar um arquivo CSV diferente, defina a variável de ambiente `CAMINHO_CSV` com o caminho para o novo arquivo CSV.

5. Inicie o servidor de desenvolvimento:
    - Usando o arquivo `movielist.csv` padrão:
      ```bash
      python manage.py runserver
      ```

    - Usando um arquivo CSV diferente:
      - No Windows:
        ```bash
        set CAMINHO_CSV=caminho/para/novo_movielist.csv
        python manage.py runserver
        ```
      - No Linux ou macOS:
        ```bash
        export CAMINHO_CSV=caminho/para/novo_movielist.csv
        python manage.py runserver
        ```

6. Acesse a aplicação:
    Abra o navegador e acesse `http://localhost:8000/awards/intervalos/` para verificar os intervalos de prêmios.

## Executando Testes

### Usando Docker

Para executar os testes, rode:
```bash
docker-compose run web python manage.py test
```

### Usando Terminal
```bash
python manage.py test
```

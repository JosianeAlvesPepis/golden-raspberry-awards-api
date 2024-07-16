import csv
import re
import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from awards.models import Filme

@receiver(post_migrate)
def carregar_filmes(sender, **kwargs):
    """
    Manipulador do sinal post_migrate para carregar filmes a partir de um arquivo CSV.
    
    Lê o arquivo CSV e insere os dados no banco de dados após as migrações.
    """
    if sender.name == 'awards':
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_csv = os.getenv('CAMINHO_CSV', os.path.join(base_dir, 'movielist.csv'))
        
        if not os.path.exists(caminho_csv):
            print(f"Arquivo CSV não encontrado: {caminho_csv}")
            return

        with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')  # Atualize conforme o delimitador do CSV
            for row in reader:
                produtores = re.split(r'\s*,\s*|\s*and\s*', row['producers'])
                for produtor in produtores:
                    Filme.objects.get_or_create(
                        titulo=row['title'],
                        produtor=produtor.strip(),
                        ano=int(row['year']),
                        vencedor=row['winner'].strip().lower() == 'yes'
                    )
        print('Filmes carregados com sucesso')

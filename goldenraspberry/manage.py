import os
import sys

def main():
    """
    Ponto de entrada do script de gerenciamento do Django.
    Define o módulo de configurações do Django, define o caminho para o arquivo CSV
    e executa o comando de gerenciamento do Django especificado nos argumentos da linha de comando.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "goldenraspberry.settings")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.environ.setdefault('CAMINHO_CSV', os.path.join(base_dir, 'movielist.csv'))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Você tem certeza de que ele está instalado e "
            "disponível na variável de ambiente PYTHONPATH? Você esqueceu de ativar um ambiente virtual?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()

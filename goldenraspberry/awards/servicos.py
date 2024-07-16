from awards.models import Filme

def calcular_intervalos_premios():
    """
    Calcula os intervalos de prêmios para os produtores.

    Retorna um dicionário contendo os produtores com os menores e maiores intervalos entre prêmios consecutivos.
    """
    vencedores = Filme.objects.filter(vencedor=True).order_by('ano')
    intervalos = {'min': [], 'max': []}
    intervalos_produtores = {}

    # Agrupa os filmes vencedores por produtor
    for filme in vencedores:
        produtores = [prod.strip() for prod in filme.produtor.split(',')]
        for produtor in produtores:
            if produtor not in intervalos_produtores:
                intervalos_produtores[produtor] = []
            intervalos_produtores[produtor].append(filme.ano)

    # Calcula os intervalos para cada produtor
    for produtor, anos in intervalos_produtores.items():
        if len(anos) > 1:
            lista_intervalos = [(anos[i+1] - anos[i], anos[i], anos[i+1]) for i in range(len(anos)-1)]
            intervalo_min = min(lista_intervalos, key=lambda x: x[0])
            intervalo_max = max(lista_intervalos, key=lambda x: x[0])
            intervalos['min'].append({
                'producer': produtor,
                'interval': intervalo_min[0],
                'previousWin': intervalo_min[1],
                'followingWin': intervalo_min[2]
            })
            intervalos['max'].append({
                'producer': produtor,
                'interval': intervalo_max[0],
                'previousWin': intervalo_max[1],
                'followingWin': intervalo_max[2]
            })

    # Verifica se há intervalos mínimos e máximos para evitar IndexError
    resultado = {
        'min': [],
        'max': []
    }
    if intervalos['min']:
        intervalo_min = sorted(intervalos['min'], key=lambda x: x['interval'])[0]
        resultado['min'].append(intervalo_min)
    if intervalos['max']:
        intervalo_max = sorted(intervalos['max'], key=lambda x: x['interval'], reverse=True)[0]
        resultado['max'].append(intervalo_max)

    return resultado

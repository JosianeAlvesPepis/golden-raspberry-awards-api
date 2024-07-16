from rest_framework.views import APIView
from rest_framework.response import Response
from awards.servicos import calcular_intervalos_premios

class IntervalosPremiosView(APIView):
    """
    View para obter os intervalos de prêmios dos produtores.
    """
    def get(self, request, *args, **kwargs):
        """
        Manipulador para requisições GET.

        Retorna os produtores com os menores e maiores intervalos entre prêmios consecutivos.
        """
        intervalos = calcular_intervalos_premios()
        return Response(intervalos)

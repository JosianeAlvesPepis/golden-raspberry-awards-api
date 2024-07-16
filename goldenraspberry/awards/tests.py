from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from awards.models import Filme

class IntervalosPremiosTestCase(TestCase):
    """
    Testes para a API de Intervalos de Prêmios.
    """

    def setUp(self):
        """
        Configuração inicial dos testes.

        Cria filmes de teste no banco de dados.
        """
        self.client = APIClient()
        Filme.objects.create(titulo="Filme 1", produtor="Produtor 1", ano=2000, vencedor=True)
        Filme.objects.create(titulo="Filme 2", produtor="Produtor 1", ano=2002, vencedor=True)
        Filme.objects.create(titulo="Filme 3", produtor="Produtor 2", ano=2001, vencedor=True)
        Filme.objects.create(titulo="Filme 4", produtor="Produtor 2", ano=2005, vencedor=True)

    def test_calcular_intervalos_premios(self):
        """
        Testa a função calcular_intervalos_premios.

        Verifica se a função retorna os intervalos corretos para os produtores.
        """
        response = self.client.get(reverse('intervalos-premios'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        intervalos = response.json()
        self.assertEqual(len(intervalos['min']), 2)
        self.assertEqual(len(intervalos['max']), 2)

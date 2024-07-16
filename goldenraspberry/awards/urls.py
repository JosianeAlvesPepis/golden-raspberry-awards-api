from django.urls import path
from awards.views import IntervalosPremiosView

"""
Módulo de URLs para os prêmios Golden Raspberry.

Este módulo define as URLs para os endpoints relacionados aos prêmios Golden Raspberry.
"""

urlpatterns = [
    path('intervalos/', IntervalosPremiosView.as_view(), name='intervalos-premios')
]

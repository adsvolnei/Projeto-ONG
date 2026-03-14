from django.shortcuts import render
from django.contrib.auth.decorators import login_required # <-- Importamos o cadeado
from .models import Familia

# Colocamos o cadeado bem em cima da função
@login_required
def home(request):
    lista_familias = Familia.objects.all()
    return render(request, 'index.html', {'familias': lista_familias})
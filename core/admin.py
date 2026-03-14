from django.contrib import admin
from .models import Familia

# Mantém o registro da sua tabela (não apague isso!)
admin.site.register(Familia)

# Adiciona as configurações de nome logo abaixo
admin.site.site_header = "Administração"
admin.site.site_title = "Administração"
admin.site.index_title = "Painel de Controle"
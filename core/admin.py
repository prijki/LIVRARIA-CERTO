from django.contrib import admin

from core.models import Autor, Categoria,Editora, Livro

admin.site.register(Categoria)

def __str__(self):
        return self.descricao

admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
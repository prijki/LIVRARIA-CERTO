from django.contrib import admin

from core.models import Autor, Categoria, Livro, Editora

admin.site.register(Categoria)

def __str__(self):
        return self.descricao

admin.site.register(Livro)
admin.site.register(Editora)
admin.site.register(Autor)

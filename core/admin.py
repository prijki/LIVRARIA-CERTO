from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Autor, Categoria, Livro, Editora, Usuario

admin.site.register(Categoria)

def __str__(self):
        return self.descricao

admin.site.register(Livro)
admin.site.register(Editora)
admin.site.register(Autor)

class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "cpf", "telefone", "data_nascimento")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(Usuario, UsuarioAdmin)
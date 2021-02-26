from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):  # herda de UserAdmin do User Model padrão
    add_form = CustomUsuarioCreateForm  # formulário de criação
    form = CustomUsuarioChangeForm  # formulário de modificação
    model = CustomUsuario  # User Model do projeto
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')  # campos da tabela de usuários cadastrados
    fieldsets = (
        (None, {'fields': ('email', 'password')}),  # nome da sessão e campos que pertencem a ela
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )  # configura e separa por categoria os itens da página de visualização de dados do usuário

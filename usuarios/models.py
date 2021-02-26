from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    """
    Gerenciador do Usuário personalizado criado para o sistema.
    """
    use_in_migrations = True  # define que esse model deve gerar tabela no banco de dados

    def _create_user(self, email, password, **extra_fields) -> object:
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)  # model é um atributo da classe BaseUserManager
        # que faz referência ao modelo que ela gerencia
        user.set_password(password)  # criptografa senha
        user.save(using=self._db)  # _db faz referência ao banco de dados do projeto
        return user

    def create_user(self, email, password=None, **extra_fields) -> object:
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields) -> object:
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser = True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff = True')

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'  # define e-mail como nome de usuário'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self) -> str:
        return self.email

    objects = UsuarioManager()  # define que os objetos da classe serão gerenciados por UsuarioManager

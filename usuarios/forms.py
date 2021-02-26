from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuario


class CustomUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuario  # define o model
        fields = ('first_name', 'last_name', 'fone')  # define campos necessários para a criação de um usuário
        labels = {'username': 'Username/Email'}  # altera o rótulo de username

    def save(self, commit=True) -> object:
        user = super().save(commit=False)  # recupera model recebido no form sem salvá-lo no banco de dados
        user.set_password(self.cleaned_data["password1"])  # criptografa senha
        user.email = self.cleaned_data["username"]  # define email como username
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')

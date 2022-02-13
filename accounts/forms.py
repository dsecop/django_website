from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'username', 'user_type')
        labels = {
            'email': 'Adres Email',
            'username': 'Nazwa użytkownika',
            'user_type': 'Rejestruję się jako',
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].label = 'Hasło'
        self.fields['password1'].help_text = ''

        self.fields['password2'].label = 'Powtórz hasło'
        self.fields['password2'].help_text = ''


class UserChangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'photo', 'username', 'postcode', 'address', 'user_type')
        labels = {
            'email': 'Adres Email',
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'photo': 'Zdjęcie profilowe',
            'username': 'Nazwa użytkownika',
            'postcode': 'Kod pocztowy',
            'address': 'Adres zamieszkania',
            'user_type': 'Typ użytkownika',
        }

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = 'Hasło'
        self.fields['password'].help_text = ''

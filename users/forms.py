from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """
    Класс для формы регистрации приложения Users.
    """

    class Meta:
        model = User
        fields = ('avatar', 'phone', 'country', 'email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    """
    Класс для формы просмотра профиля пользователя.
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'phone', 'country')

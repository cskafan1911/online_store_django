import random

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


# def generate_new_password(request):
#     new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
#     send_mail(
#         subject='Смена пароля',
#         message=f'Ваш новый пароль: {new_password}',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[request.user.email],
#     )
#     request.user.set_password(new_password)
#
#     return redirect(reverse_lazy('users'))

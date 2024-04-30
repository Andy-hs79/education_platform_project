from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = "__all__"  # ('email', 'first_name',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"  # ('email', 'first_name',)

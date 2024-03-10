from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "password",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in [
            "username",
            "password",
        ]:
            self.fields[field_name].widget.attrs.update(
                {
                    "class": "h-10 shadow-md md:h-12 lg:h-14 text-xl lg:text-2xl rounded-full p-4"
                }
            )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]:
            self.fields[field_name].widget.attrs.update(
                {
                    "class": "h-10 shadow-md md:h-12 lg:h-14 text-xl lg:text-2xl rounded-full p-4"
                }
            )

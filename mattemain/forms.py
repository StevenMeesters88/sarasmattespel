from django import forms
from django.core.exceptions import ValidationError

# https://docs.djangoproject.com/en/5.0/ref/validators/


def validate_input(value):
    try:
        value = int(value)
    except ValueError:
        raise ValidationError(
            "%(value)s is not an even number",
            params={"value": value},
        )


class AnswerForm(forms.Form):
    # svaret = forms.CharField(label='Skriv svaret :-)')
    svaret = forms.CharField(validators=[validate_input], widget=forms.TextInput(attrs={'placeholder': 'Svar', 'style': 'width: 200px; height: 50px; font-size: xx-large;', 'class': 'form-control'}))

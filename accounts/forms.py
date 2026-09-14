from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm,PasswordChangeForm
from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = "" 
            field.widget.attrs.update({'class':'inputtxt'})
        self.fields['username'].widget.attrs.update({'onkeydown': 'check(event)'})
        self.fields['password1'].widget.attrs.update({'onkeyup': 'pass(event)'})
        self.fields['age'].widget.attrs.update({'class': 'inputnum'})
        self.fields['email'].required = True
        self.fields['email'].help_text = "please enter a valid email"
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if get_user_model().objects.filter(email=email).exists():
                raise forms.ValidationError('use anothor email.this email is in use')
        return email
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = "" 
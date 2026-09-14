from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView
from django.contrib.auth.views import PasswordResetView

from .forms import CustomUserCreationForm, CustomPasswordChangeForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
class PasswordChangeView(FormView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "registration/password_change_form.html"
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
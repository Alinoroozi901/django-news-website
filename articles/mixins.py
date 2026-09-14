from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin

class CustomLoginNeededMixin:
    login_url = "/accounts/login/"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)
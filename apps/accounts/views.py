from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
class AdnLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AuthenticationForm

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        auth_login(self.request, user)
        return redirect(reverse_lazy('dashboard:home'))

class AdnSignUpView(CreateView):
    pass

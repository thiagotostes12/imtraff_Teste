from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.shortcuts import redirect
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('bi_page')  # URL da página de sucesso

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            messages.error(self.request, 'Usuário ou senha incorretos')
            return self.form_invalid(form)

class BIView(LoginRequiredMixin, TemplateView):
    template_name = 'bi.html'
    login_url = reverse_lazy('login')  # URL para onde redirecionar se não estiver logado

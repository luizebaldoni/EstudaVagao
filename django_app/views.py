from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse_lazy
from django.views import View


def index(request_iter):
    return render(request_iter, 'index.html')


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

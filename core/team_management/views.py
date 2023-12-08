from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User

# Create your views here.

class MemberList(ListView):
    model = User
    template_name = 'list.html'

class MemberAdd(CreateView):
    model = User
    fields = '__all__'
    template_name = 'add.html'
    success_url = '/'

class MemberEdit(UpdateView):
    model = User
    fields = '__all__'
    template_name = 'edit.html'
    success_url = '/'

class MemberDelete(DeleteView):
    model = User
    success_url = '/'
    template_name = 'delete.html'

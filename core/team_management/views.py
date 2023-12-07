from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import User
from .forms import UserForm

# Create your views here.

class MemberList(View):
    def get(self, request):
        users = User.objects.all()
        context = {'members':users, 'num_members': len(users)}
        return render(request, 'list.html', context)

class MemberAdd(View):
    def get(self, request):
        form = UserForm
        return render(request, 'add.html', {'form': form})
    
    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('members'))
        else:
            return render(request, 'add.html', {'form': user_form})

class MemberEdit(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        form = UserForm(instance=user)
        context = {'form':form, 'user_id': id}
        return render(request, 'edit.html', context)

    def post(self, request, id):
        user = User.objects.get(id=id)
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('members'))
        else:
            return render(request, 'edit.html', {'form': user_form, 'user_id':id})

class MemberDelete(View):
    def get(self, request, id):
        return redirect(reverse('members'))

    def post(self, request, id):
        user = User.objects.get(id=id)
        user.delete()
        return redirect(reverse('members'))

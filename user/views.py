from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import View, TemplateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from user.forms import RegisterForm
from user.models import Profile
from core.views import OwnerOnlyMixin

User = get_user_model()


class Register(View):
    form = RegisterForm()
    def get(self, request, *args, **kwargs):
        return render(request, 'user/register.html', {'form': self.form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        return render(request, 'user/profile.html', {'user': user})



class UpdateProfile(LoginRequiredMixin, OwnerOnlyMixin, UpdateView):
    model = Profile
    fields = ('fname', 'lname', 'image', 'about_me', 'location')
    success_url = 'profile'


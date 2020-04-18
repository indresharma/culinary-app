from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic import View, TemplateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from user.forms import RegisterForm
from user.models import Profile

user = get_user_model()


class Register(View):
    form = RegisterForm()
    def get(self, request, *args, **kwargs):
        return render(request, 'user/register.html', {'form': self.form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ('fname', 'lname', 'image', 'about_me', 'location')
    success_url = 'profile'


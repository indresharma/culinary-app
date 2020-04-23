from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, TemplateView, UpdateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from user.forms import RegisterForm
from user.models import Profile
from core.views import OwnerOnlyMixin

User = get_user_model()


class Register(CreateView): 
    model = User
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        user = form.save()
        user.profile.first_name = first_name
        user.profile.last_name = last_name
        user.save()
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        return render(request, 'user/profile.html', {'user': user})


class UpdateProfile(LoginRequiredMixin, OwnerOnlyMixin, UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'image', 'about_me', 'location')
    success_url = 'profile'


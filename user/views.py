from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login
from django.views.generic import CreateView, TemplateView, UpdateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse

from user.forms import RegisterForm
from user.models import Profile
from user.tokens import TokenGenerator
from core.views import OwnerOnlyMixin


User = get_user_model()
account_activation_token = TokenGenerator()


class Register(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user.profile.first_name = first_name
            user.profile.last_name = last_name
            user.save()
            #messaging
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('user/user_activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            messages.success(request, 'Activation link sent to you email address. Please activate your account to complete registration')
            return redirect('user:login')
        return redirect('user:register')

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success('Your account has been activated successfully')
        return redirect('core:recipes')
    else:
        messages.error('Activation link is invalid!')
        return redirect('user:register')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        return render(request, 'user/profile.html', {'user': user})


class UpdateProfile(LoginRequiredMixin, OwnerOnlyMixin, UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'image', 'about_me', 'location')



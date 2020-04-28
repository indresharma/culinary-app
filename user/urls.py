from django.urls import path
from django.contrib.auth import views as auth_views

from user import views as user_views


app_name = 'user'

urlpatterns = [
    path('register/', user_views.Register.as_view(), name='register'),
    path('profile/<int:pk>/', user_views.ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('update-profile/<int:pk>/', user_views.UpdateProfile.as_view(), name='update-profile'),
    path('activate/<uidb64>/<token>', user_views.activate_account, name='activate'),

]
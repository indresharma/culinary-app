from django.urls import path


from .views import *

app_name = 'sales'

urlpatterns = [
    path('billing/', OrderCreateView.as_view(), name="billing"),

]
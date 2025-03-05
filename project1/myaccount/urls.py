from django.urls import path
from .views import *
urlpatterns=[ path('Login',Loginview),
    path('Register',Registerview),

]
from django.urls import path
from .views import *
urlpatterns=[ path('Login',Loginview),
    path('Register',Registerview),
    path('verify_email/<uidb64>/<token>/',verify_email),

]
from django.urls import path
from .views import loginView, signup, logOut

app_name = 'authentication'

urlpatterns = [
    path('', loginView, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logOut, name="logout")
]
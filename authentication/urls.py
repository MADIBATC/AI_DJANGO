from django.urls import path
from .views import login, signup

app_name = 'authentication'

urlpatterns = [
    path('', login, name='login'),
    path('signup/', signup, name='signup')
]
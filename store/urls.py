from django.urls import path
from .views.home import Home
from .views.signup import Signup
from .views.login import Login
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
]

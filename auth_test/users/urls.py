from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', home_view, name='home'),
    path('register/',register_view, name='register'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),

]

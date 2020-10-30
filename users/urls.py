"Define URL patterns for users"

from django.urls import path, include

from . import view 

app_name = 'users'
urlpatterns = [
    # Include default auth urls
    path('', include('django.contrib.auth.urls')), 
    # Registration page. 
    path('register/', view.register, name='register')   
]
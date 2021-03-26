from django.urls import path
from . import views

urlpatterns = [
    path('',views.showregForm),
    path('signup/',views.showregForm,name='signup'),
    path('login/',views.showloginForm,name="login"),
 
   
    
]
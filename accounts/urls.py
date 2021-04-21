from django.urls import path
from . import views

urlpatterns=[
   path('Mumbai',views.Mumbai,name='destination1'),
   path('Bengaluru',views.Bengaluru,name='destination2'),
   path('Jaipur',views.Jaipur,name='destination3'),
   path('Delhi',views.Delhi,name='destination4'),
   path('contact', views.contact, name='contact'),
   path('home', views.home, name='home'),
   path('register', views.register , name='register'),
   path('login', views.login , name='login'),
   path('logout',views.logout, name='logout')
]
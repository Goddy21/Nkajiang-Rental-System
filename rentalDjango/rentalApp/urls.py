from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('rent', views.rent, name='rent'),
    path('sales', views.sales, name='sales'),
    #path('services', views.sevices, name='services'),
    #path('contacts', views.contacts, name='contacts')
]

urlpatterns += staticfiles_urlpatterns()
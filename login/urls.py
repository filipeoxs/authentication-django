from django.urls import path
from . import views

urlpatterns= [
    path('registration/', views.registration_user, name='registration'),
    path('login/', views.login_user, name='login'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('deleteuser/<int:id>/', views.delete_user, name='delete_user'),
    path('updateuser/<int:id>/', views.update_user, name='update_user')
]
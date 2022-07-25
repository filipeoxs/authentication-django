from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns= [
    path('registration/', views.registration_user, name='registration'),
    path('login/', views.login_user, name='login'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('deleteuser/<int:id>/', views.delete_user, name='delete_user'),
    path('updateuser/<int:id>/', views.update_user, name='update_user'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='login/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="login/registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='login/registration/password_reset_complete.html'), name='password_reset_complete'),      
]
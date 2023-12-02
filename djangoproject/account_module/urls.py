from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register_page'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('logout', views.LogoutView.as_view(), name='logout_page'),
    path('forget-pass', views.Forget_passwordView.as_view(), name='forget_pass_page'),
    path('reset-pass/<active_code>', views.ResetpasswordView.as_view(), name='reset_pass_page'),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name='activate_account'),
]

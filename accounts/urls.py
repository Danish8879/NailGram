from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import login_page,registerPage,activate_email

urlpatterns = [
    path('login/',login_page,name="login"),
    path('register/',registerPage, name='register'),
    path('activate/<email_token>',activate_email,name="activate_email"),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

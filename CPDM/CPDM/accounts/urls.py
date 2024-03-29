from django.urls import path

from CPDM.accounts.views import LoginUserView, RegisterUserView, LogoutUserView, logout_view

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('logout/', logout_view, name='logout_user'),
    path('logout1/', LogoutUserView.as_view(), name='logout_user1'),
)

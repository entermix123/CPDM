from django.urls import path

from CPDM.accounts.views import LoginUserView, RegisterUserView
from CPDM.web.views import index, about

urlpatterns = (
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
)

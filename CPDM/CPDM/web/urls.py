from django.urls import path

from CPDM.web.views import index

urlpatterns = (
    path('', index, name='index'),
)

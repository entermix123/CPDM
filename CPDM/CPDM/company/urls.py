from django.urls import path

from CPDM.company.views import CreateCompanyView, CompanyListView, UpdateCompanyView

urlpatterns = (
    path('create/', CreateCompanyView.as_view(), name='company_create'),
    path('list/', CompanyListView.as_view(), name='company_list'),
    path('update/', UpdateCompanyView.as_view(), name='company_update'),
)

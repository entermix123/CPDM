from django.urls import path

from CPDM.company.views import CreateCompanyView, CompanyListView, company_details, company_delete, company_update

urlpatterns = (
    path('create/', CreateCompanyView.as_view(), name='company_create'),
    path('list/', CompanyListView.as_view(), name='company_list'),
    path('details/<company_id>/', company_details, name='company_details'),
    path('update/<company_id>/', company_update, name='company_update'),
    path('delete/<company_id>/', company_delete, name='company_delete'),
)

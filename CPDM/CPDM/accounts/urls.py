from django.urls import path

from CPDM.accounts.views import logout_view, ProfileDetailView, UpdateProfileView

urlpatterns = (
    path('details/', ProfileDetailView.as_view(), name='profile_details'),
    path('logout/', logout_view, name='logout_user'),
    path('update/', UpdateProfileView.as_view(), name='update_profile'),
)

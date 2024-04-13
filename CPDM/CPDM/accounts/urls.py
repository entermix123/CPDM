from django.urls import path

from CPDM.accounts.views import logout_view, ProfileDetailView, UpdateProfileView, DeleteUserView, \
    UserApiUpdateView, ProfileApiUpdateView, UserApiDeleteView

urlpatterns = (
    path('details/', ProfileDetailView.as_view(), name='profile_details'),
    path('logout/', logout_view, name='logout_user'),
    path('update/', UpdateProfileView.as_view(), name='update_profile'),
    path('delete/', DeleteUserView.as_view(), name='delete_user'),
    path('update_user/', UserApiUpdateView.as_view(), name='api_update_user'),
    path('delete_user/', UserApiDeleteView.as_view(), name='api_delete_user'),
    path('update_profile/', ProfileApiUpdateView.as_view(), name='api_update_profile'),
)

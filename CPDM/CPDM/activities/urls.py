from django.urls import path

from CPDM.activities.views import CreateActivityView, UpdateActivityView, ListActivityView, DetailsActivityView, \
    activity_details, activity_update, ActivityDeleteView

urlpatterns = (
    path('create/', CreateActivityView.as_view(), name='activity_create'),
    path('list/', ListActivityView.as_view(), name='activity_list'),
    # path('update/<int:activity_id>/', UpdateActivityView.as_view(), name='activity_update'),
    # path('details/<int:activity_id>/', DetailsActivityView.as_view(), name='activity_details'),
    path('details/<int:activity_id>/', activity_details, name='activity_details'),
    path('update/<int:activity_id>/', activity_update, name='activity_update'),
    path('delete/<int:activity_id>/', ActivityDeleteView.as_view(), name='activity_delete'),
)

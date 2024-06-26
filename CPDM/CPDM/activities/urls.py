from django.urls import path

from CPDM.activities.views import CreateActivityView, UpdateActivityView, ListActivityView, DetailsActivityView, \
    activity_details, activity_update, ActivityDeleteView, delete_activity, ActivityCreateApiView, ActivityListApiView, \
    ActivityDetailsUpdateDeleteApiView

urlpatterns = (
    path('create/', CreateActivityView.as_view(), name='activity_create'),
    path('list/', ListActivityView.as_view(), name='activity_list'),
    path('details/<int:activity_id>/', DetailsActivityView.as_view(), name='activity_details'),
    # path('details/<int:activity_id>/', activity_details, name='activity_details'),
    path('update/<int:activity_id>/', UpdateActivityView.as_view(), name='activity_update'),
    # path('update/<int:activity_id>/', activity_update, name='activity_update'),
    path('delete/<int:activity_id>/', ActivityDeleteView.as_view(), name='activity_delete'),
    # path('delete/<int:activity_id>/', delete_activity, name='activity_delete'),

    path('create_activity/', ActivityCreateApiView.as_view(), name='api_activity_create'),
    path('list_activity/', ActivityListApiView.as_view(), name='api_activity_list'),
    path('details_activity/<int:pk>/', ActivityDetailsUpdateDeleteApiView.as_view(), name='api_activity_details'),
    path('update_activity/<int:pk>/', ActivityDetailsUpdateDeleteApiView.as_view(), name='api_activity_update'),
    path('delete_activity/<int:pk>/', ActivityDetailsUpdateDeleteApiView.as_view(), name='api_activity_delete'),
)

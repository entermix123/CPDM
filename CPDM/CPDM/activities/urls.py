from django.urls import path

from CPDM.activities.views import CreateActivityView, UpdateActivityView, ActivityListView

urlpatterns = (
    path('create/', CreateActivityView.as_view(), name='activity_create'),
    path('list/', ActivityListView.as_view(), name='activity_list'),
    path('update/', UpdateActivityView.as_view(), name='activity_update'),
)

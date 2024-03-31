from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CPDM.web.urls')),
    path('profile/<int:pk>/', include([
        path('', include('CPDM.accounts.urls')),
        path('company/', include('CPDM.company.urls')),
        path('employees/', include('CPDM.employees.urls')),
        path('departments/', include('CPDM.departments.urls')),
        path('activities/', include('CPDM.activities.urls')),
        path('processes/', include('CPDM.processes.urls')),
        path('procedures/', include('CPDM.procedures.urls')),
        path('instructions/', include('CPDM.instructions.urls')),
        path('software/', include('CPDM.software.urls')),
        path('risk_matrix/', include('CPDM.risk_matrix.urls')),
    ])),
]

# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

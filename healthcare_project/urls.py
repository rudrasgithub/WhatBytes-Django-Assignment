"""
URL configuration for healthcare_project.
"""

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def custom_404(request, exception):
    """Return JSON response for 404 errors."""
    return JsonResponse(
        {
            'error': True,
            'status_code': 404,
            'message': 'The requested endpoint was not found.',
        },
        status=404,
    )


def custom_500(request):
    """Return JSON response for 500 errors."""
    return JsonResponse(
        {
            'error': True,
            'status_code': 500,
            'message': 'An internal server error occurred. Please try again later.',
        },
        status=500,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    path('api/mappings/', include('mappings.urls')),
]

# Custom error handlers
handler404 = 'healthcare_project.urls.custom_404'
handler500 = 'healthcare_project.urls.custom_500'

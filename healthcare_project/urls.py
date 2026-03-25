"""
URL configuration for healthcare_project.
"""

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def api_root(request):
    """Welcome view for the root URL with API documentation."""
    return JsonResponse({
        'message': 'Welcome to the Healthcare Backend API',
        'version': '1.0',
        'endpoints': {
            'auth': {
                'register': '/api/auth/register/ [POST]',
                'login': '/api/auth/login/ [POST]',
            },
            'patients': {
                'list_create': '/api/patients/ [GET, POST]',
                'detail': '/api/patients/<id>/ [GET, PUT, DELETE]',
            },
            'doctors': {
                'list_create': '/api/doctors/ [GET, POST]',
                'detail': '/api/doctors/<id>/ [GET, PUT, DELETE]',
            },
            'mappings': {
                'create': '/api/mappings/ [POST]',
                'list_all': '/api/mappings/list/ [GET]',
                'by_patient': '/api/mappings/<patient_id>/ [GET]',
                'delete': '/api/mappings/delete/<id>/ [DELETE]',
            },
        },
    })


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
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    path('api/mappings/', include('mappings.urls')),
]

# Custom error handlers
handler404 = 'healthcare_project.urls.custom_404'
handler500 = 'healthcare_project.urls.custom_500'


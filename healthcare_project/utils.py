from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """
    Global exception handler for DRF.
    Returns consistent JSON error responses for all exceptions.
    """
    response = exception_handler(exc, context)

    if response is not None:
        # Wrap DRF's default error response in a consistent format
        custom_data = {
            'error': True,
            'status_code': response.status_code,
        }

        if isinstance(response.data, dict):
            custom_data['message'] = response.data.get('detail', response.data)
        elif isinstance(response.data, list):
            custom_data['message'] = response.data
        else:
            custom_data['message'] = str(response.data)

        response.data = custom_data
        return response

    # Handle unexpected exceptions (500 errors)
    return Response(
        {
            'error': True,
            'status_code': 500,
            'message': 'An unexpected error occurred. Please try again later.',
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )

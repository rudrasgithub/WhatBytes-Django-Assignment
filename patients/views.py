from rest_framework import viewsets

from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """
    CRUD ViewSet for Patient records.
    - Users can only see and manage their own patients.
    - Automatically sets created_by to the authenticated user.
    """

    serializer_class = PatientSerializer

    def get_queryset(self):
        """Return patients belonging to the authenticated user."""
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        """Set the created_by field to the current user."""
        serializer.save(created_by=self.request.user)

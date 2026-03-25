from rest_framework import viewsets

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """
    CRUD ViewSet for Doctor records.
    - All authenticated users can view all doctors.
    - Automatically sets created_by to the authenticated user on creation.
    """

    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    def perform_create(self, serializer):
        """Set the created_by field to the current user."""
        serializer.save(created_by=self.request.user)

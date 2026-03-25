from rest_framework import generics, status
from rest_framework.response import Response

from patients.models import Patient

from .models import PatientDoctorMapping
from .serializers import MappingDetailSerializer, MappingSerializer


class MappingCreateView(generics.CreateAPIView):
    """
    POST /api/mappings/
    Assign a doctor to a patient.
    """

    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer


class MappingListView(generics.ListAPIView):
    """
    GET /api/mappings/
    Retrieve all patient-doctor mappings.
    """

    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingDetailSerializer


class MappingByPatientView(generics.ListAPIView):
    """
    GET /api/mappings/<patient_id>/
    Get all doctors assigned to a specific patient.
    """

    serializer_class = MappingDetailSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)

    def list(self, request, *args, **kwargs):
        patient_id = self.kwargs['patient_id']

        # Verify the patient exists
        if not Patient.objects.filter(id=patient_id).exists():
            return Response(
                {"error": f"Patient with id {patient_id} not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return super().list(request, *args, **kwargs)


class MappingDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/mappings/<id>/
    Remove a doctor from a patient.
    """

    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer

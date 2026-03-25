from rest_framework import serializers

from doctors.serializers import DoctorSerializer
from patients.serializers import PatientSerializer

from .models import PatientDoctorMapping


class MappingSerializer(serializers.ModelSerializer):
    """Serializer for PatientDoctorMapping model."""

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate(self, attrs):
        """Check that this mapping doesn't already exist."""
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')

        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError(
                "This patient-doctor mapping already exists."
            )
        return attrs


class MappingDetailSerializer(serializers.ModelSerializer):
    """Serializer with nested patient and doctor details for read operations."""

    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'created_at']
        read_only_fields = ['id', 'created_at']

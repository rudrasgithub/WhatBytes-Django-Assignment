from django.urls import path

from .views import (
    MappingByPatientView,
    MappingCreateView,
    MappingDeleteView,
    MappingListView,
)

urlpatterns = [
    path('', MappingCreateView.as_view(), name='mapping-create'),
    path('list/', MappingListView.as_view(), name='mapping-list'),
    path('<int:patient_id>/', MappingByPatientView.as_view(), name='mapping-by-patient'),
    path('delete/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]

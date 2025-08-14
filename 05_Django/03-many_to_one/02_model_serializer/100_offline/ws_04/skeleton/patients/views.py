from .models import Patient
from .serializers import PatientSerializer, PatientListSerializer, PatientDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET", "POST"])
def patient_list_create(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        serializer = PatientListSerializer(patients, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET",])
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    serializer = PatientDetailSerializer(patient)
    return Response(serializer.data)

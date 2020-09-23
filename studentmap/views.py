from rest_framework import permissions
from rest_framework import viewsets
from django.shortcuts import render
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import *

# Create your views here.


def MapView(request):
    return render(request, 'index.html')


class StudentAPI(viewsets.ModelViewSet):
    queryset = StudentLocation.objects.all()
    serializer_class = StudentLocationSerilizer

    # studentID = []
    # hMunicipality = []
    # hBarangay = []
    # studentName = []
    # studentAge = []
    # studentPhoneNumber = []
    # studentCourse = []
    # studentYear = []
    # hLat = []
    # hLong = []

    # for i in qs:
    #     studentID.append(i['stud_id'])
    #     hMunicipality.append(i['municipality'])
    #     hBarangay.append(i['barangay'])
    #     studentName.append(i['stud_name'])
    #     studentAge.append(i['stud_age'])
    #     studentPhoneNumber.append(i['stud_pnumber'])
    #     studentCourse.append(i['stud_course'])
    #     studentYear.append(i['stud_year'])
    #     hLat.append(i['hlat'])
    #     hLong.append(i['hlong'])

    # context = {
    #     'id': studentID,
    #     'municipality': hMunicipality,
    #     'barangay': hBarangay,
    #     'name': studentName,
    #     'age': studentAge,
    #     'phone': studentPhoneNumber,
    #     'course': studentCourse,
    #     'year': studentYear,
    #     'lat': hLat,
    #     'long': hLong,
    # }

from .models import *
from rest_framework import serializers


class StudentLocationSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentLocation
        fields = ['stud_id', 'municipality', 'barangay',
                  'stud_name', 'stud_age', 'stud_pnumber', 'stud_course', 'stud_year', 'hlat', 'hlong']

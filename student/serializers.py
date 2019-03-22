from rest_framework import serializers
from .models import submissiondata

class answersserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = submissiondata
        fields = (
            'q1',
            'q2',
            'q3',
            'q4',
            'q5',
            'q5text',
            'url'
        )

from rest_framework import serializers
from .models import questions

class questionsserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = questions
        fields = (
            'fq1',
            'fq2',
            'fq3',
            'topic1',
            'topic2',
            'topic3',
            'topic4',
            'topic5',
            'url'
        )

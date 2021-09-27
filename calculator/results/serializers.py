import ast

from rest_framework import serializers
from .models import Results


# Results Serializer
class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'


from rest_framework import serializers
from .models import complainRequest
class complainserializer(serializers.ModelSerializer):
    class Meta:
        model = complainRequest
        fields = '__all__'
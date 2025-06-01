from rest_framework.serializers import ModelSerializer
from .models import Lugat

class LugatListSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'unique_identificator', 'language']
        model = Lugat

class LugatDetailSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Lugat

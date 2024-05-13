from rest_framework import serializers
from .models import Project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'area', 'description', 'ubication', 'date', 'user')
        read_only_fields = ('date',)
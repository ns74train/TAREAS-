from rest_framework import serializers
from .models import Tareas


class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = ('idTarea', 'title', 'created_at', 'status')

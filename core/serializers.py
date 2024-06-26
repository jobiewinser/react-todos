from rest_framework import serializers
from core.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "details", "deadline", "created_on"]

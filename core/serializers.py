import datetime
from rest_framework import serializers
from core.models import Todo


# class TodoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     details = serializers.CharField(required=False, allow_blank=True)
#     deadline = serializers.DateField(required=False, allow_blank=True)

#     def create(self, validated_data):
#         """
#         Create and return a new `Todo` instance, given the validated data.
#         """
#         return Todo.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Todo` instance, given the validated data.
#         """
#         instance.deadline = validated_data.get('deadline', instance.deadline)
#         instance.title = validated_data.get('title', instance.title)
#         instance.details = validated_data.get('details', instance.details)
#         instance.edited_by = self.request.user
#         instance.edited_on = datetime.datetime.now()
#         instance.save()
#         return instance

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'details', 'deadline']
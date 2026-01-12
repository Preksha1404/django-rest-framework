from rest_framework import serializers
from .models import Task

# Using Serializer
# class TaskSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=500)
#     status = serializers.CharField()
#     duration = serializers.DurationField()

#     def create(self, validated_data):
#         return Task.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('name', instance.title)
#         instance.status = validated_data.get('status',instance.status)
#         instance.duration = validated_data.get('duration',instance.duration)
#         instance.save()
#         return instance

# Using ModelSerializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
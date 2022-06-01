from typing import OrderedDict
from rest_framework import serializers

from .models import *

# todo cruds


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ['id', 'first_name', 'last_name', 'phone', 'email']


class currentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ['id', 'first_name', 'last_name']


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects)

    def create(self, validated_data):
        task = Tasks.objects.create(**validated_data)
        return task

    def update(self, instance, validated_data):
        instance.stageOfExecution = validated_data.get('stageOfExecution')
        instance.startTime = validated_data.get('startTime')
        instance.endTime = validated_data.get('endTime')
        instance.task = validated_data.get('task')
        instance.user = validated_data.get('user')
        instance.save()
        print(instance)
        return instance

    class Meta:
        model = Tasks
        depth = 2
        fields = '__all__'

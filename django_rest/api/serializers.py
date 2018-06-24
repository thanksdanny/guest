from django.contrib.auth.models import User, Group
from rest_framework import serializers


"""
Serializers 用于定义API的表现形式，如返回哪些字段、返回怎样的格式等
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Event, Guest

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

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'name', 'address', 'start_time', 'limit', 'status')


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'realname', 'phone', 'email', 'sign', 'event')

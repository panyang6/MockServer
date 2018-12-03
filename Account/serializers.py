# encoding: utf-8
'''
@author: yaopengfei
@email: yaopengfei@pxn.one
@file: serializers.py
@time: 2018/12/3 9:46 PM
@desc:
'''

from rest_framework import serializers
from Account.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
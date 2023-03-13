from rest_framework import serializers
from .models import MyUser
class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=MyUser
        fields='__all__'
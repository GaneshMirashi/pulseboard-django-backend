from rest_framework import serializers
from .models import Update


class UpdateSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Update
        fields = [
            'id',
            'user',
            'user_email',
            'team',
            'content',
            'status',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['user']
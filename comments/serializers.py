from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_email', 'update', 'text', 'created_at']
        read_only_fields = ['user']
from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'create_at', 'update_at', 'photo', 'is_publish')

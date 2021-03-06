from rest_framework import serializers
from status.models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            
        ]


    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        if content is None:
            raise serializers.ValidationError("content is required")
        return data
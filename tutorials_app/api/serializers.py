from rest_framework import serializers 
from tutorials_app.models import Tutorial

class TutorialSrializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Tutorial
        fields='__all__'
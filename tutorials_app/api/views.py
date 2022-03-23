from rest_framework import generics
from tutorials_app.api.serializers import TutorialSrializer
from tutorials_app.models import Tutorial
from django_filters.rest_framework import DjangoFilterBackend


class TutorialList(generics.ListAPIView):
    #queryset= Tutorial.objects.all()
    serializer_class=TutorialSrializer
    def get_queryset(self):
        return Tutorial.objects.filter(is_published=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'is_published']
    
 
 
class TutorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Tutorial.objects.all()
    serializer_class=TutorialSrializer
    
        
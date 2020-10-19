from superheroes.models import SuperHeroe, Publisher
from rest_framework import viewsets
from rest_framework import permissions
from superheroes.serializers import SuperHeroeSerializer, PublisherSerializer

class SuperHeroeViewSet(viewsets.ModelViewSet):
    queryset = SuperHeroe.objects.all()
    serializer_class = SuperHeroeSerializer
    permission_classes = [permissions.IsAuthenticated]

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticated]

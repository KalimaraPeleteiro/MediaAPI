from rest_framework import viewsets, generics
from MediaApp.models import Video
from MediaApp.serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoEspecificoViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(id = self.kwargs['pk'])
        return queryset
    serializer_class = VideoSerializer
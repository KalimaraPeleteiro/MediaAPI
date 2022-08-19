from rest_framework import viewsets, generics, filters
from MediaApp.models import Video, Categoria
from MediaApp.serializers import VideoSerializer, CategoriaSerializer



class VideoViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    search_fields = ['titulo']


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class VideoEspecificoViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(id = self.kwargs['pk'])
        return queryset
    serializer_class = VideoSerializer


class CategoriaEspecificaViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Categoria.objects.filter(id = self.kwargs['pk'])
        return queryset
    serializer_class = CategoriaSerializer


class VideosDaCategoriaViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(categoriaId = self.kwargs['id'])
        return queryset
    serializer_class = VideoSerializer
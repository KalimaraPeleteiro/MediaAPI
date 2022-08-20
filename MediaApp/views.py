from rest_framework import viewsets, generics, filters
from MediaApp.models import Video, Categoria
from MediaApp.serializers import VideoSerializer, CategoriaSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication



class VideoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    search_fields = ['titulo']


class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class VideoEspecificoViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    def get_queryset(self):
        queryset = Video.objects.filter(id = self.kwargs['pk'])
        return queryset
    serializer_class = VideoSerializer


class CategoriaEspecificaViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    def get_queryset(self):
        queryset = Categoria.objects.filter(id = self.kwargs['pk'])
        return queryset
    serializer_class = CategoriaSerializer


class VideosDaCategoriaViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    def get_queryset(self):
        queryset = Video.objects.filter(categoriaId = self.kwargs['id'])
        return queryset
    serializer_class = VideoSerializer


class VideosLivresViewSet(generics.ListAPIView):
    queryset = Video.objects.filter(id = 100)
    serializer_class = VideoSerializer
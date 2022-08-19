from django.test import TestCase
from MediaApp.models import Video, Categoria
from MediaApp.serializers import VideoSerializer, CategoriaSerializer


class VideoSerializerTestCase(TestCase):

    def setUp(self):
        self.modelCategoria = Categoria(200, "Teste", "Sem Cor")
        self.model = Video(id = 15, 
                           categoriaId = self.modelCategoria, 
                           titulo = "Teste", 
                           descricao = "Descrição Teste", 
                           url = "https://youtube.com/Teste")
        self.serializer = VideoSerializer(instance=self.model)
    
    def test_verifica_campos_serializados(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'categoriaId', 'titulo', 'descricao', 'url']))
    
    def test_verifica_conteudo_serializado(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.model.id)
        self.assertEqual(data['categoriaId'], self.modelCategoria.id)
        self.assertEqual(data['titulo'], self.model.titulo)
        self.assertEqual(data['descricao'], self.model.descricao)
        self.assertEqual(data['url'], self.model.url)


class CategoriaSerializerTestCase(TestCase):

    def setUp(self):
        self.model = Categoria(200, "Teste", "Sem Cor")
        self.serializer = CategoriaSerializer(instance=self.model)
    
    def test_verifica_campos_serializados(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'titulo', 'cor']))
    
    def test_verifica_conteudo_serializado(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.model.id)
        self.assertEqual(data['titulo'], self.model.titulo)
        self.assertEqual(data['cor'], self.model.cor)
    
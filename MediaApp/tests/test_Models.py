from django.test import TestCase
from MediaApp.models import Video, Categoria


class VideoTestCase(TestCase):

    def setUp(self):
        self.modelCategoria = Categoria(200, "Teste", "Sem Cor")
        self.model = Video(id = 15, 
                           categoriaId = self.modelCategoria, 
                           titulo = "Teste", 
                           descricao = "Descrição Teste", 
                           url = "https://youtube.com/Teste")
    
    def test_verifica_conteudo_campos(self):
        self.assertEqual(self.model.id, 15)
        self.assertEqual(self.model.categoriaId, self.modelCategoria)
        self.assertEqual(self.model.titulo, "Teste")
        self.assertEqual(self.model.descricao, "Descrição Teste")
        self.assertEqual(self.model.url, "https://youtube.com/Teste")


class CategoriaTestCase(TestCase):
    def setUp(self):
        self.model = Categoria(200, "Teste", "Sem Cor")
        self.modelDefault = Categoria(cor="Sem Cor")
    
    def test_verifica_conteudo_campos(self):
        self.assertEqual(self.model.id, 200)
        self.assertEqual(self.model.titulo, "Teste")
        self.assertEqual(self.model.cor, "Sem Cor")
    
    def test_verifica_default_values(self):
        self.assertEqual(self.modelDefault.id, 1)
        self.assertEqual(self.modelDefault.titulo, "LIVRE")

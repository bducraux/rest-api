from django.test import TestCase
from .models import Demanda
from user.models import User


class DemandTests(TestCase):

    def test_demanda_is_not_none(self):
        user = User.objects.create("test@test.com", "senha123")

        demanda = Demanda(descricao="Demanda teste", endereco="endereco teste", contato="contato teste", anunciante=user)

        self.assertIs(demanda is not None, True)

        return demanda

    def test_anunciante_is_not_none(self):
        demanda = self.test_demanda_is_not_none()

        self.assertIs(demanda.anunciante is not None, True)

    def test_descricao(self):
        demanda = self.test_demanda_is_not_none()

        expected_descricao = f'{demanda.descricao}'

        self.assertEquals(expected_descricao, 'Demanda teste')
        self.assertTrue(isinstance(demanda, Demanda))

    # todo Testar endpoints

from faker import Faker
import random
import unittest
from src.logica.coleccion import Coleccion
from src.modelo.album import Album, Medio
from src.modelo.cancion import Cancion, AlbumCancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import Session


class InterpreteTestCase(unittest.TestCase):
    def setUp(self):
        '''Crea una colección para hacer las pruebas'''
        self.coleccion = Coleccion()

        '''Abre la sesión'''
        self.session = Session()

        '''Crea una instance de Faker'''
        self.data_factory = Faker()

        '''Se programa para que Faker cree los mismos datos cuando se ejecuta'''
        Faker.seed(1000)

        '''Genera 10 datos en data y creamos los álbumes'''
        self.data = []
        self.interprete = []
        for i in range(0, 10):
            self.data.append((
                self.data_factory.unique.name(),
                self.data_factory.text()))
            self.interprete.append(
                Interprete(
                    nombre=self.data[-1][0],
                    texto_curiosidades=self.data[-1][1],

                ))
            self.session.add(self.interprete[-1])

        self.session.commit()


    def tearDown(self):
        self.session = Session()
        busqueda = self.session.query(Interprete).all()

        for interprete in busqueda:
            self.session.delete(interprete)

        self.session.commit()
        self.session.close()

    def test_constructor(self):
        for interprete, dato in zip(self.interprete, self.data):
            self.assertEqual(interprete.nombre, dato[0])
            self.assertEqual(interprete.texto_curiosidades, dato[1])

    def test_agregar_interprete(self):
        '''Prueba la adición de un interprete'''

        self.data.append((
            self.data_factory.unique.name(),
            self.data_factory.text()))
        resultado = self.coleccion.agregar_interprete(
            nombre=self.data[-1][0],
            texto_curiosidades=self.data[-1][1])
        self.assertEqual(resultado, True)
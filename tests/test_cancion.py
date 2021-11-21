from faker import Faker
import random
import unittest
from src.logica.coleccion import Coleccion
from src.modelo.album import Album, Medio
from src.modelo.cancion import Cancion, AlbumCancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import Session

class CancionTestCase(unittest.TestCase):
    def setUp(self):
        '''Crea una colección para hacer las pruebas'''
        self.coleccion = Coleccion()

        '''Abre la sesión'''
        self.session = Session()

        '''Crea una instance de Faker'''
        self.data_factory = Faker ( )

        '''Se programa para que Faker cree los mismos datos cuando se ejecuta'''
        Faker.seed ( 1000 )

        '''Genera 10 datos en data y creamos los álbumes'''
        self.data = [ ]
        self.canciones = [ ]
        for i in range ( 0 , 10 ) :
            self.data.append ( (
                self.data_factory.unique.name ( ) ,
                self.data_factory.random_int ( 0 , 4) ,
                self.data_factory.random_int (0, 60 ) ,
                self.data_factory.unique.name ( ) ))
            self.canciones.append (
                Cancion(
                    titulo=self.data[-1][0],
                    minutos=self.data[-1][1],
                    segundos=self.data[-1][2],
                    compositor=self.data[-1][3],
                    albumes=[],
                    interpretes=[]
                ) )
            self.session.add ( self.canciones[ -1 ] )

        '''Persiste los objetos
        En este setUp no se cierra la sesión para usar los albumes en las pruebas'''
        self.session.commit ( )

    def tearDown(self) :
        self.session = Session ( )
        busqueda = self.session.query ( Cancion ).all ( )

        for cancion in busqueda :
            self.session.delete ( cancion )

        self.session.commit ( )
        self.session.close ( )

    def test_constructor(self):
        for cancion, dato in zip(self.canciones, self.data):
            self.assertEqual(cancion.titulo, dato[0])
            self.assertEqual(cancion.minutos, dato[1])
            self.assertEqual(cancion.segundos, dato[2])
            self.assertEqual(cancion.compositor, dato[3])

    def test_agregar_cancion ( self ) :
        '''Prueba la adición de un álbum'''

        self.data.append((
            self.data_factory.unique.name(),
            self.data_factory.random_int(0, 4),
            self.data_factory.random_int(0, 60),
            self.data_factory.unique.name()))
        resultado = self.coleccion.agregar_cancion (
            titulo=self.data[-1][0],
            minutos=self.data[-1][1],
            segundos=self.data[-1][2],
            compositor=self.data[-1][3], )
        self.assertEqual ( resultado , True )
import random
import unittest
from src.logica.coleccion import Coleccion
from src.modelo.album import Album, Medio
from src.modelo.cancion import Cancion, AlbumCancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import Session

class CancionTestCase(unittest.TestCase):
    def setUp(self):
        '''Crea una colección para hacer las pruebas'''
        self.coleccion = Coleccion()

        '''Abre la sesión'''
        self.session = Session()

        '''Crea una instance de Faker'''
        self.data_factory = Faker ( )

        '''Se programa para que Faker cree los mismos datos cuando se ejecuta'''
        Faker.seed ( 1000 )

        '''Genera 10 datos en data y creamos los álbumes'''
        self.data = [ ]
        self.canciones = [ ]
        for i in range ( 0 , 10 ) :
            self.data.append ( (
                self.data_factory.unique.name ( ) ,
                self.data_factory.random_int ( 0 , 4) ,
                self.data_factory.random_int (0, 60 ) ,
                self.data_factory.unique.name ( ) ))
            self.canciones.append (
                Cancion(
                    titulo=self.data[-1][0],
                    minutos=self.data[-1][1],
                    segundos=self.data[-1][2],
                    compositor=self.data[-1][3],
                    albumes=[],
                    interpretes=[]
                ) )
            self.session.add ( self.canciones[ -1 ] )

        '''Persiste los objetos
        En este setUp no se cierra la sesión para usar los albumes en las pruebas'''
        self.session.commit ( )

    def tearDown(self) :
        self.session = Session ( )
        busqueda = self.session.query ( Cancion ).all ( )

        for cancion in busqueda :
            self.session.delete ( cancion )

        self.session.commit ( )
        self.session.close ( )

    def test_constructor(self):
        for cancion, dato in zip(self.canciones, self.data):
            self.assertEqual(cancion.titulo, dato[0])
            self.assertEqual(cancion.minutos, dato[1])
            self.assertEqual(cancion.segundos, dato[2])
            self.assertEqual(cancion.compositor, dato[3])

    def test_agregar_cancion ( self ) :
        '''Prueba la adición de un álbum'''

        self.data.append((
            self.data_factory.unique.name(),
            self.data_factory.random_int(0, 4),
            self.data_factory.random_int(0, 60),
            self.data_factory.unique.name()))
        resultado = self.coleccion.agregar_cancion (
            titulo=self.data[-1][0],
            minutos=self.data[-1][1],
            segundos=self.data[-1][2],
            compositor=self.data[-1][3], )
        self.assertEqual ( resultado , True )
import datetime
import unittest
import random

from faker import Faker

from src.logica.coleccion import Coleccion
from src.modelo.album import Album,Medio
from src.modelo.cancion import Cancion,AlbumCancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import Session
from fake_providers import AlbumTituloProvider,AlbumAnioProvider,AlbumDescripcionProvider,AlbumMedioProvider

class AlbumTestCaseFake(unittest.TestCase):
    def setUp ( self ) :
        self.logica = Coleccion()
        self.session = Session ( )
        self.data_factory = Faker ( )

        # Generación de datos con libreria Faker
        self.data_factory.add_provider ( AlbumTituloProvider )
        self.data_factory.add_provider ( AlbumAnioProvider )
        self.data_factory.add_provider ( AlbumDescripcionProvider )
        self.data_factory.add_provider ( AlbumMedioProvider )

        self.data=[]
        self.albumes=[]
        for i in range ( 0 , 2 ) :
            self.data.append(
                (
                    self.data_factory.unique.albumTitulo ( ),
                    self.data_factory.albumAnio ( ),
                    self.data_factory.albumDescripcion ( ),
                    self.data_factory.albumMedio ()
                )
            )
            self.albumes.append(
                Album(
                    titulo = self.data[ -1 ][ 0 ] ,
                    anio = self.data[ -1 ][ 1 ] ,
                    descripcion = self.data[ -1 ][ 2 ] ,
                    medio = self.data[ -1 ][ 3 ] ,
                    canciones = [ ]
                )
            )
            self.session.add ( self.albumes[ -1 ] )

        '''
            Persiste los objetos
            En este setUp no se cierra la sesión para usar
            los albumes en las pruebas
        '''
        self.session.commit ( )
        #self.session.close()

    def tearDown ( self ) :
        self.session = Session ( )

        busqueda_album = self.session.query ( Album ).all ( )
        for album in busqueda_album :
            self.session.delete ( album )

        self.session.commit()
        self.session.close()

    def test_constructor ( self ) :
        for album , dato in zip ( self.albumes , self.data ) :
            self.assertEqual ( album.titulo , dato[ 0 ] )
            self.assertEqual ( album.anio , dato[ 1 ] )
            self.assertEqual ( album.descripcion , dato[ 2 ] )
            self.assertEqual ( album.medio , dato[ 3 ] )

    def test_agregar_album ( self ) :
        albumTitulo=self.data_factory.unique.albumTitulo ( )
        albumAnio=self.data_factory.albumAnio ( )
        albumDescripcion=self.data_factory.albumDescripcion ( )
        albumMedio=self.data_factory.albumMedio()

        resultado=self.logica.agregar_album(albumTitulo,albumAnio,albumDescripcion,albumMedio)

        self.assertEqual ( resultado , True )

    def test_agregar_album1 ( self ) :
        self.data.append (
            (
                self.data_factory.unique.albumTitulo ( ) ,
                self.data_factory.albumAnio ( ) ,
                self.data_factory.albumDescripcion ( ),
                self.data_factory.albumMedio()
            )
        )

        resultado = self.logica.agregar_album (
            titulo = self.data[ -1 ][ 0 ] ,
            anio = self.data[ -1 ][ 1 ] ,
            descripcion = self.data[ -1 ][ 2 ] ,
            medio = self.data[ -1 ][ 3 ] )
        self.assertEqual ( resultado , True )
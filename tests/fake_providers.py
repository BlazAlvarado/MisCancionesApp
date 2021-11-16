import random
import unittest
from datetime import datetime
from datetime import timedelta
from src.modelo.album import Medio
from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from faker import Faker
from faker.providers import BaseProvider

class AlbumTituloProvider(BaseProvider):
    def albumTitulo(self):
        albumesTitulo = ['Latin Jazz Compilation', 'Bandas sonoras famosas', 'The Dark Side of the Moon', 'The Bodyguard', 'Rumours', 'Saturday Night Fever', 'El fantasma de la ópera', 'Come on Over']
        return random.choice(albumesTitulo)

class AlbumAnioProvider(BaseProvider):
    def albumAnio(self):
        anio = [2018, 2019, 2020, 2021]
        return random.choice(anio)

class AlbumDescripcionProvider(BaseProvider):
    def albumDescripcion(self):
        descripcion = ["Album original", "Compilación"]
        return random.choice(descripcion)

class AlbumMedioProvider(BaseProvider):
    def albumMedio(self):
        self.medios = [ Medio.CD , Medio.CASETE , Medio.DISCO ]
        return random.choice(self.medios)

class AlbumFechaProvider(BaseProvider):
    def AlbumFecha(self):
        new_date = datetime(2019, 2, 28, 00, 00, 00, 00000)
        fecha = [new_date, new_date + timedelta(days=-1), new_date + timedelta(days=-2)]
        return random.choice(fecha)

class CancionTituloProvider(BaseProvider):
    def cancionTitulo(self):
        cancionTitulo = ['Happier', 'Duele Amor', 'Cant Hold Us', 'La chata']
        return random.choice(cancionTitulo)

class CancionMinutosProvider(BaseProvider):
    def cancionMinutos(self):
        min = [1, 2, 3, 4]
        return random.choice(min)

class CancionSegundosProvider(BaseProvider):
    def cancionSegundos(self):
        seg = [range(1,60)]
        return random.choice(seg)

class CancionCompositorProvider(BaseProvider):
    def cancionCompositor(self):
        self.compo = [ 'mashmello','FernandoBalbin','Maklemore','Elchato' ]
        return random.choice(self.compo)



class InterpreteNombreProvider(BaseProvider):
    def interpreteNombre(self):
        interpreteNombre = ['BadBony', 'Baarrera', 'JustinBabier', 'El chatin']
        return random.choice(interpreteNombre)

class InterpreteTextoCuriosidadesProvider(BaseProvider):
    def interpreteTexto(self):
        interpreteTextoCuriosidades = ['Canta Bien en la nota menor', 'Canta?', 'Canta como los dioses', 'Me agacho para escucharlo']
        return random.choice(interpreteTextoCuriosidades)
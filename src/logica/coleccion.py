from src.modelo.declarative_base import engine, Base, session
from src.modelo.album import Album
from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete

class Coleccion():
    def _init_(self):
        Base.metadata.create_all(engine)

    def agregar_album(self, titulo, anio, descripcion, medio):
        busqueda = session.query(Album).filter(Album.titulo == titulo).all()
        if len(busqueda) == 0:
            album = Album(titulo=titulo, anio=anio, descripcion=descripcion, medio=medio)
            session.add(album)
            session.commit()
            return True
        else:
            return False

    def dar_medios(self):
        return [medio.name for medio in Medio]

    def editar_album(self, album_id, titulo, anio, descripcion, medio):
        busqueda = session.query(Album).filter(Album.titulo == titulo, Album.id != album_id).all()
        if len(busqueda) == 0:
            album = session.query(Album).filter(Album.id == album_id).first()
            album.titulo = titulo
            album.anio = anio
            album.descripcion = descripcion
            album.medio = medio
            session.commit()
            return True
        else:
            return False

    def eliminar_album(self, album_id):
        try:
            album = session.query(Album).filter(Album.id == album_id).first()
            session.delete(album)
            session.commit()
            return True
        except:
            return False

    def dar_album_por_id(self, album_id):
        return session.query(Album).get(album_id)._dict_

    def agregar_cancion ( self , titulo , minutos , segundos , compositor ) :
        busqueda = session.query ( Cancion ).filter ( Cancion.titulo == titulo ).all ( )
        if len ( busqueda ) == 0 :
            cancion = Cancion ( titulo = titulo , minutos = minutos , segundos = segundos , compositor = compositor )
            session.add ( cancion )
            session.commit ( )
            return True
        else :
            return False



    def agregar_interprete(self, nombre, texto_curiosidades):
        busqueda = session.query(Interprete).filter(Interprete.nombre == nombre).all()
        if len(busqueda) == 0:
            interprete = Interprete(nombre=nombre, texto_curiosidades=texto_curiosidades)
            session.add(interprete)
            session.commit()
            return True
        else:
            return False
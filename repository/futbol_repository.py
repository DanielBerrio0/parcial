from extensions import db
from models.futbol_model import Paises

class PaisRepository:

    def get_all_paises(self):
        return Paises.query.all()

    def get_pais_by_id(self, pais_id: int):
        return Paises.query.get(pais_id)

    def create_pais(self, nombre_pais: str):
        nuevo_pais = Paises(nombre_pais=nombre_pais)
        db.session.add(nuevo_pais)
        db.session.commit()
        return nuevo_pais

    def update_pais(self, pais_id: int, nombre_pais: str):
        pais = self.get_pais_by_id(pais_id)
        if not pais:
            return None
        pais.nombre_pais = nombre_pais
        db.session.commit()
        return pais

    def delete_pais(self, pais_id: int):
        pais = self.get_pais_by_id(pais_id)
        if not pais:
            return None
        db.session.delete(pais)
        db.session.commit()
        return pais

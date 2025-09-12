from models.futbol_model import Paises


class PaisRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_all_paises(self):
        return self.db.query(Paises).all()

    def get_pais_by_id(self, pais_id: int):
        return self.db.query(Paises).filter_by(id=pais_id).first()

    def create_pais(self, nombre_pais: str):
        nuevo_pais = Paises(nombre_pais=nombre_pais)
        self.db.add(nuevo_pais)
        self.db.commit()
        self.db.refresh(nuevo_pais)  # Para que el objeto tenga el ID asignado
        return nuevo_pais

    def update_pais(self, pais_id: int, nombre_pais: str):
        pais = self.get_pais_by_id(pais_id)
        if not pais:
            return None
        pais.nombre_pais = nombre_pais
        self.db.commit()
        self.db.refresh(pais)
        return pais

    def delete_pais(self, pais_id: int):
        pais = self.get_pais_by_id(pais_id)
        if not pais:
            return None
        self.db.delete(pais)
        self.db.commit()
        return pais
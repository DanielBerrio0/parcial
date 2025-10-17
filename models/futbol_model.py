from extensions import db  # Importa db desde extensions.py

class Paises(db.Model):  # Hereda de db.Model
    __tablename__ = 'paiss'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_pais = db.Column(db.String(255), nullable=False)
    
    mundiales = db.relationship(
        'Mundiales',
        back_populates='pais',
        cascade='all, delete-orphan'
    )

class Mundiales(db.Model):  # Hereda de db.Model
    __tablename__ = 'mundial'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('paiss.id'))
    
    # Relación inversa
    pais = db.relationship('Paises', back_populates='mundiales')

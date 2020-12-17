from typing import Dict
from pydantic import BaseModel
from datetime import date
from datetime import datetime


class ReservasInDB(BaseModel):
    id_reserva: int
    id_habitacion: int
    id_usuario: int
    nom_usuario: str
    correo_usuario: str
    telefono_usuario: int
    fecha_llegada: str
    fecha_salida: str
    num_dias: int
    num_huespedes: int
    precio_total: int
    estado: str


db_reservas = [{"id_reserva": 10,
                "id_habitacion": 555,
                "id_usuario": 1016097241,
                "nom_usuario": "nicolas beltran alvarez",
                "correo_usuario": "beltran.alvarez70@gmail.com",
                "telefono_usuario": 3102784039,
                "fecha_llegada": "20/12/2020",
                "fecha_salida": "21/12/2020",
                "num_dias":1,
                "num_huespedes": 1,
                "precio_total": 200000,
                "estado": "reservado"
                }]



#llamado --> GET

def get_reserva_id(id: int):

    for reserva in db_reservas:  
        if reserva["id_reserva"] == id:
            return reserva

def get_reserva_cc(cc: int):
    
    for reserva in db_reservas:  
        if reserva["id_usuario"] == cc:
            return reserva

#insertado --> POST

def save_reserva(rese_in_db: ReservasInDB):

    db_reservas.append(rese_in_db.dict())
    return rese_in_db

#actualizado --> PUT

def update_reserva(reserva: ReservasInDB):

    for p_reserva in range(len(db_reservas)):
        if db_reservas[p_reserva]["id_reserva"] == reserva["id_reserva"]:

            db_reservas[p_reserva] = reserva

            return reserva

#borrado --> DELETE


def delete_reserva(id: int):
    contador = 0
    pos = 1000000
    for p in range(len(db_reservas)):
        if db_reservas[p]["id_reserva"] == id:
            pos = contador
        else:
            contador = contador+1
    try:
        db_reservas.pop(pos)
        return True
    except:
        return None

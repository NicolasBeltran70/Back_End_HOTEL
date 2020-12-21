from typing import Dict
from pydantic import BaseModel
from datetime import date
from datetime import datetime

class CalendarioInDB(BaseModel):
    id_calendario: int
    id_habitacion: int
    fecha: str
    disponibilidad: bool
    precio: int


db_calendario = [{"id_calendario": 1111,
                  "id_habitacion": 555,
                  "fecha": "2020/12/20",
                  "disponibilidad": True,
                  "precio": 50000},

                 {"id_calendario": 1112,
                  "id_habitacion": 555,
                  "fecha": "2020/12/21",
                  "disponibilidad": True,
                  "precio": 50000},

                 {"id_calendario": 1113,
                  "id_habitacion": 555,
                  "fecha": "2020/12/22",
                  "disponibilidad": True,
                  "precio": 50000},

                 {"id_calendario": 1114,
                  "id_habitacion": 555,
                  "fecha": "2020/12/23",
                  "disponibilidad": True,
                  "precio": 50000},

                  {"id_calendario": 1115,
                  "id_habitacion": 555,
                  "fecha": "2020/12/24",
                  "disponibilidad": False,
                  "precio": 60000}

                   ]


#llamado --> GET

def all_calendario():#trae todo el calendario
    return db_calendario 


def get_calendario(id : int):
    
    for calen in db_calendario:#for por habitacion
        if calen["id_calendario"] == id:
            return calen


#insertado --> POST
def save_calendario(cal_in_db: CalendarioInDB):

    db_calendario.append(cal_in_db.dict())
    return cal_in_db

#actualizado --> PUT


def update_calendario(calendario: CalendarioInDB):

    # for por posicion habitacion
    for p_calendario in range(len(db_calendario)):
        if db_calendario[p_calendario]["id_calendario"] == calendario["id_calendario"]:

            db_calendario[p_calendario] = calendario

            return calendario


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
                  "fecha": "20/12/2020",
                  "disponibilidad": True,
                  "precio": 50000},

                 {"id_calendario": 1112,
                  "id_habitacion": 555,
                  "fecha": "21/12/2020",
                  "disponibilidad": True,
                  "precio": 50000},

                 {"id_calendario": 1113,
                  "id_habitacion": 555,
                  "fecha": "22/12/2020",
                  "disponibilidad": True,
                  "precio": 50000},

                 {"id_calendario": 1114,
                  "id_habitacion": 555,
                  "fecha": "23/12/2020",
                  "disponibilidad": False,
                  "precio": 50000}

                   ]


#llamado --> GET
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

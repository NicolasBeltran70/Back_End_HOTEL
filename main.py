from db.habitaciones_db import HabitacionesInDB
from db.habitaciones_db import get_habitacion, update_habitacion, delete_habitacion, save_habitacion

from db.calendario_db import CalendarioInDB
from db.calendario_db import get_calendario, update_calendario, save_calendario

from db.reservas_db import ReservasInDB
from db.reservas_db import get_reserva_id, get_reserva_cc, update_reserva, save_reserva, delete_reserva

from models.habitaciones_models import HabitacionInf,HabitacionReserva
from models.reservas_models import ReservaCon,ReservaInf

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()
###########################################      GETS     ##################################################

@api.get("/info/habitacion/consulta")#llamado habitacion info
async def get_habi_info(id: int):

    habi_in_db = get_habitacion(id)#validacion de existencia
    if habi_in_db == None:
        raise HTTPException(status_code=404, detail="la habitacion no existe")

    habi_inf = HabitacionInf(**habi_in_db)#si existe muestre la  info de la habitacion
    return habi_inf#retorne la habitacion info

@api.get("/info/reserva/cc")  
async def get_rese_cc(cc: int):

    rese_in_db = get_reserva_cc(cc)  # validacion de existencia
    if rese_in_db == None:
        raise HTTPException(status_code=404, detail="la reserva no existe")

    # si existe muestre la  reserva 
    rese_fun = ReservaCon(**rese_in_db)
    return rese_fun  # retorne la reserva


@api.get("/info/calendario/id")  # llamado habitacion info
async def get_cal(id: int):

    cale_in_db = get_calendario(id)  # validacion de existencia
    if cale_in_db == None:
        raise HTTPException(status_code=404, detail="el calendario no existe")

    # si existe muestre la  info de la habitacion
    cale_fun = CalendarioInDB(**cale_in_db)
    return cale_fun  # retorne la habitacion info

###########################################      PUTs        #########################################################

@api.put("/update/habitacion")#actualizacion base de datos
async def make_habi(habitacion : HabitacionInf):

    #validacion de existencia
    habi_in_db = get_habitacion(habitacion.id_habitacion)
    if habi_in_db == None:
        raise HTTPException(status_code=404, detail="la habitacion no existe")

    update_habitacion(habitacion.dict())
    upd_habitacion = HabitacionInf(**habitacion.dict())
    return upd_habitacion

@api.put("/update/reserva")#actualizacion base de datos
async def make_rese(reserva: ReservaInf):

    #validacion de existencia
    rese_in_db = get_reserva_id(reserva.id_reserva)
    if rese_in_db == None:
        raise HTTPException(status_code=404, detail="la reserva no existe")

    update_reserva(reserva.dict())
    upd_reserva = ReservaInf(**reserva.dict())
    return upd_reserva


@api.put("/update/calendario")  # actualizacion base de datos
async def make_calen(calendario: CalendarioInDB):

    #validacion de existencia
    cale_in_db = get_calendario(calendario.id_calendario)
    if cale_in_db == None:
        raise HTTPException(status_code=404, detail="el calendario no existe")

    update_calendario(calendario.dict())
    upd_calendario = CalendarioInDB(**calendario.dict())
    return upd_calendario

##########################################       DELETES      ########################################################

@api.delete("/borrar/habitacion")
async def borrar_habi(id: int):

    #validacion de existencia
    habi_in_db = get_habitacion(id)
    if habi_in_db == None:
        raise HTTPException(status_code=404, detail="la habitacion no existe")

    delete_habitacion(id)
    return True

#########################################       POST       ######################################################

@api.post("/crear/calendario")
async def create_calendario(calendario: CalendarioInDB):
    cale_in_db = get_calendario(calendario.id_calendario)
    if cale_in_db == None:
        save_calendario(calendario)
        new_calendario = CalendarioInDB(**calendario.dict())
        return new_calendario
    return None

@api.post("/crear/reserva")
async def create_reserva(reserva: ReservaInf):
    rese_in_db = get_reserva_id(reserva.id_reserva)
    if rese_in_db == None:
        save_reserva(reserva)
        new_reserva = ReservaInf(**reserva.dict())
        return new_reserva
    return None


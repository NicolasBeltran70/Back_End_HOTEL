from db.habitaciones_db import *

from db.calendario_db import *

from db.reservas_db import *

from models.habitaciones_models import HabitacionInf,HabitacionReserva
from models.reservas_models import ReservaCon,ReservaInf

from datetime import *

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()
########################################### CONSULTA DE CALENDARIO #########################################
@api.get("/info/calendario")
async def Consulta_calendario(f_ini: str, f_fin: str,t_habitacion: str,n_personas: int):
    fi=datetime.strptime(f_ini,"%Y/%m/%d")
    ff=datetime.strptime(f_fin,"%Y/%m/%d")
    f3=fi-ff
    n_days=abs(f3.days)+1#numero de dias + 1 para que cuente el mismo dia
    print("*********n dias********",n_days)
    id_hab=get_Idhabitacion(t_habitacion)#id habitacion
    n_camas=get_camas_habi(id_hab)#numero de camas por habitacion
    cal=all_calendario()# base de datos calendario

    l=["fecha","disponibilidad"]#lista para extraccion
    calendario=[]#lista vacia de calendario
    cont=0


    for x in cal:#se escanea todo el calendario y saca solo por el tipo de habitacion 
        if(x["id_habitacion"]==id_hab and x["disponibilidad"]==True):
            y=list(map(x.get,l))
            calendario.append(y)
    ###### calendario=[["21/12/2020","True"],["22/12/2020","False"]]
    print("*******calendario por habitacion*********",calendario)
    for j in calendario:
        ##### j[0]="fecha"
        f_1=datetime.strptime(j[0],"%Y/%m/%d")#transforma la el str en fecha
         ##### j[1]="disponibilidad"
        if (f_1>=fi and f_1<=ff and j[1]==True):
            print("********* fecha que cumple**********",j[0])
            cont=cont+1
    print("******** contador ***********",cont)


#si calendario no existe-> no hay disponibilidad para esa habitacion
#si cont no exist-> no hay ninguna fecha disponible para ese habitacion
#si contador no es igual a las fechas-> no todos los dias estan disponibles
#si numero_personas > numero_camas -> hay mas personas que camas por habitacion
    if(not calendario):
        raise HTTPException(status_code=404, detail="no hay disponibilidad para esa habitacion en esas fechas")
    else:
        if(not cont):
            raise HTTPException(status_code=404, detail="no hay ninguna habitacion disponible")
        else:
            if(cont < n_days):
                raise HTTPException(status_code=404, detail="no todos los dias estan disponibles")
            else:
                if(n_personas > (n_camas*2)):
                    raise HTTPException(status_code=404, detail="hay mas personas que camas por habitacion")
                else:
                    print("Si hay disponibilidad")
                    return("si hay disponibilidad para la habitacion: ",t_habitacion," en la fecha inicial: ",f_ini," y fecha final: ",f_fin,"para: ",n_personas," personas")

######################################      DILIGENCIA RESERVA      ###########################################

@api.post("/crear/reserva")
async def create_reserva(reserva: ReservaInf):
    rese_in_db = get_reserva_id(reserva.id_reserva)
    if rese_in_db == None:
        save_reserva(reserva)
        new_reserva = ReservaInf(**reserva.dict())
        return new_reserva
    return None


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


#######################################################################################################################

origins=[
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080"
    ]

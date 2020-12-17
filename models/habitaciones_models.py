from pydantic import BaseModel
from datetime import datetime

class HabitacionInf(BaseModel):

    id_habitacion: int 
    tipo_habitacion: str
    num_camas_habitacion: int
    descrip_habitacion: str


class HabitacionReserva(BaseModel):
    id_habitacion: int 
    tipo_habitacion: str
    num_camas_habitacion: int

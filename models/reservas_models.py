from pydantic import BaseModel
from datetime import datetime

class ReservaInf(BaseModel):
    
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

class ReservaCon(BaseModel):

    id_reserva: int 
    id_habitacion: int
    nom_usuario: str
    precio_total: int
    estado: str

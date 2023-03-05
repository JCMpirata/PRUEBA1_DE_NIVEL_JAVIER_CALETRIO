from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, validator
import BDVehiculo as bdv
import FBicicleta as fbi
import FCoche as fco
import FFurgoneta as ffu
import FMotocicleta as fmo
import helpers as hlp

headers = {"content-type": "charset=utf-8"}

class ModeloVehiculo(BaseModel):
    modelo: constr(min_length=3, max_length=3)
    marca: constr(min_length=2, max_length=30)
    ruedas: int
    color: constr(min_length=2, max_length=30)
    precio: float
    velocidad: int
    cilindrada: int
    tipo: constr(min_length=2, max_length=30)
    carga: int


class ModeloCrearVehiculo(ModeloVehiculo):
    @validator("modelo")
    def validar_modelo(cls, modelo):
        if not hlp.modelo_valido(modelo, bdv.Vehiculos.lista):
            raise ValueError("Vehiculo ya existente o modelo incorrecto")
        return modelo
    

app = FastAPI(
    title="API del Gestor de vehiculos",
    description="Ofrece diferentes funciones para gestionar los vehiculos.")

@app.get("/vehiculos/", tags=["Vehiculos"])
async def vehiculos():
    content = [vehiculo.to_dict() for vehiculo in bdv.Vehiculos.lista]
    return JSONResponse(content=content, headers=headers)
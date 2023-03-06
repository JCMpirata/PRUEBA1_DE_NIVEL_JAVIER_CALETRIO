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
    modelo: constr(min_length=2, max_length=30)
    vehiculo: constr(min_length=2, max_length=30)
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

@app.get("/vehiculos/buscar/{modelo}/", tags=["Vehiculos"])
async def vehiculos_buscar(modelo: str):
    vhc = bdv.Vehiculos.buscar(modelo=modelo)
    if not vhc:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return JSONResponse(content=vhc.to_dict(), headers=headers)

@app.post("/vehiculos/crear/", tags=["Vehiculos"])
async def vehiculos_crear(datos: ModeloCrearVehiculo):
    if datos.vehiculo == "bicicleta":
        vhc = fbi.Bicicletas.crear_bici(datos.modelo, datos.vehiculo, datos.marca, datos.ruedas, datos.color, datos.precio, datos.velocidad)
    elif datos.vehiculo == "coche":
        vhc = fco.Coches.crear_coche(datos.modelo, datos.vehiculo, datos.marca, datos.ruedas, datos.color, datos.precio, datos.velocidad, datos.cilindrada)
    elif datos.vehiculo == "furgoneta":
        vhc = ffu.Furgonetas.crear_coche(datos.modelo, datos.vehiculo, datos.marca, datos.ruedas, datos.color, datos.precio, datos.velocidad, datos.carga)
    elif datos.vehiculo == "motocicleta":
        vhc = fmo.Motocicletas.crear_moto(datos.modelo, datos.vehiculo, datos.marca, datos.ruedas, datos.color, datos.precio, datos.velocidad, datos.cilindrada)
    if vhc:
        return JSONResponse(content=vhc.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Vehiculo no creado")

@app.put("/vehiculos/modificar/{modelo}/", tags=["Vehiculos"])
async def vehiculos_modificar(datos: ModeloVehiculo):
    if bdv.Vehiculos.buscar(datos.modelo):
        if datos.vehiculo == "bicicleta":
            vhc = fbi.Bicicletas.modificar_bici(datos.modelo, datos.vehiculo, datos.marca, datos.ruedas, datos.color, datos.precio, datos.velocidad)
        elif datos.vehiculo == "coche":
            vhc = fco.Coches.modificar_coche(datos.modelo, datos.vehiculo, datos.marca, datos.ruedas, datos.color, datos.precio, datos.velocidad, datos.cilindrada)
        elif datos.vehiculo == "furgoneta":
            vhc = ffu.Furgonetas.modificar_coche(datos.modelo, datos.vehiculo, datos.marca, datos.ruedas, datos.color, datos.precio, datos.velocidad, datos.carga)
        elif datos.vehiculo == "motocicleta":
            vhc = fmo.Motocicletas.modificar_moto(datos.modelo, datos.vehiculo, datos.marca, datos.ruedas, datos.color, datos.precio, datos.velocidad, datos.cilindrada)
        if vhc:
            return JSONResponse(content=vhc.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")

@app.delete("/vehiculos/borrar/{modelo}/", tags=["Vehiculos"])
async def vehiculos_borrar(modelo: str):
    if bdv.Vehiculos.buscar(modelo):
        vhc = bdv.Vehiculos.borrar(modelo)
        if vhc:
            return JSONResponse(content=vhc.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")

print("API del Gestor de vehiculos")
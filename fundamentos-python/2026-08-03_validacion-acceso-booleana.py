def validar_acceso(usuario:dict,recurso:dict):
    val=(usuario["activo"]==True) and (usuario["bloqueado"]==False)and((usuario["rol"]=="admin") or(usuario["id"] == recurso["owner_id"] and not recurso["privado"]==True))
    return val
#no hace falta poner en activo o bloqueado ==true solo con ponerlo vale, es mas limpio y pro.
usuario= {"id": 1, "rol": "user", "activo": True, "bloqueado": False}
recurso = {"owner_id": 1, "privado": False}
valido=validar_acceso(usuario,recurso)
print(valido)
from ldap3 import Server, Connection, ALL
from fastapi import FastAPI,Response, status
from typing import Union
import os
from dotenv import load_dotenv
from app.model.request import LoginRequest


app = FastAPI()
load_dotenv()

server :str = os.getenv('SERVER')
port :int = int(os.getenv('PORT'))
domain :str = os.getenv('DOMAIN')

@app.post("/api/login", status_code=200)
def login(request: LoginRequest, response: Response):
    print("Username: ",request.username)
    try :
        print("Iniciando Conexion")
        s = Server(server, port=port, get_info=ALL)    

        c = Connection(s, user=request.username+domain, password=request.password)
        print("Coneccion realizada")
        if c.bind():
            print('Login Exitoso!\n', c.result)
            response.status_code = status.HTTP_200_OK    
        else :
            print('Login Fallido!\n', c.result)
            response.status_code = status.HTTP_401_UNAUTHORIZED
        
        return c.result
    except:
            print(c.result)
            response.status_code =status.HTTP_500_INTERNAL_SERVER_ERROR
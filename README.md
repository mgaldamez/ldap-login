<h1 align="center">Servicio Rest para hacer login via ldap</h1>

_Servicio Rest que se utiliza para hacer login via Ldap._

### Requisitos 📋

```
* docker
```

### Ejecucion 🔧


_Paso 1_

```
dentro de la carpeta raiz del proyecto renombrar el archivo .env-dev a .env y luego ejecutar el siguiente comando.
docker build -t ldap-login .
```

_Paso 2_

```
una vez creada la imagen ejecutamos el siguiente comando para correr un contenedor que expone en el puerto 8000.

docker run -d --name ldap-login -p 8000:80 ldap-login.
```

_Paso 3_

```
ir a la documentacion http://localhost:8000/docs
```


## Construido con 🛠️

* [python3](https://www.python.org/) - Python is a programming language that lets you work more quickly and integrate your systems more effectively.
* [FastApi](https://fastapi.tiangolo.com/) - FastAPI framework, high performance, easy to learn, fast to code, ready for production.
* [ldap3](https://ldap3.readthedocs.io/) - ldap3 is a pure Python LDAP 3 client library strictly conforming to RFC4510.


## Autor ✒️

* **Marvin Galdamez** - [mgaldamez](https://github.com/mgaldamez/)
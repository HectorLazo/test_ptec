# [Prueba Tecnica API][docs]


Prueba Técnica desarrollando una API de usuarios en Python.

## Tabla de contenidos:
---

- [Requerimientos](#requerimientos)
- [Instalación](#instalación)
- [Herramientas utilizadas](#herramientas-utilizadas)
- [Endpoints](#endpoints)
- 	[Listar usuarios](#listar-usuarios)

---

## Requerimientos

* Python (3.9)
* Django (3.2)
* Django REST Framework


## Instalación

Clonamos el proyecto desde github... 

    git clone https://github.com/HectorLazo/pro
    
Instalamos mediante `pip` django y django rest framework cuyas versiones las tenemos en el archivo requirements.txt
    
    python manage.py pip install -r requirements.txt
    
Hacemos las migraciones de nuestro proyecto con los siguientes comandos

    python manage.py makemigrations
    
    python manage.py migrate

Y por último, ejecutamos el servidor...

    python manage.py runserver
    
## Herramientas utilizadas

* [Python](https://www.python.org/) - Lenguaje de programación
* [Django](https://www.djangoproject.com/) - Framework Para Python
* [DjangoRESTFramework](https://www.django-rest-framework.org/) - Framework para crear API REST

## Endpoints


### Listar Usuarios
Update the profile for a specific user account.

`GET /api/usuario-list/{userId}/`


#### Parámetros
- **id** - Identifier for current user

#### Cuerpo
- **username** - Username to update to
- **email** - E-mail address to update to

#### Response
- **userId** - Identifier for the user

#### Errors
- **ErrorCode1** - Caused by missing identifier
- **ErrorCode2** - Username was not given
- **ErrorCode3** - Server exploded

#### Request de ejemplo
`GET /account/1692/`

```javascript
{
	username: "NewUsername",
	email: "Email@Email.com"
}
```





#### Example Response
`200 OK`

```javascript
{
	userId: 1692
}
```

### Editar Usuario

Si el request es correcto, se devuelve una instancia 'Usuario', dados los datos validados.

`GET /api/usuario-detail/{id}/`


#### Parámetros
- **id** - Identificador UUID del usuario

#### Response
- **usuario** - Usuario con cada uno de sus campos

#### Errores
- **400** - Causado por un id inválido.

#### Request de ejemplo
`GET /api/usuario-detail/e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40`

#### Example Response
`200 OK`

```javascript
{
  "id": "e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40",
  "nombre": "Juan",
  "apellido": "Astorga",
  "email": "jastorga@gmail.com",
  "fecha_nacimiento": "1980-12-10"
}
```

### Editar Usuario

Si el request es correcto, se edita una instancia 'Usuario', dado su id.

`PUT /api/usuario-update/{id}/`
`PATCH /api/usuario-update/{id}/`

#### Parámetros
- **id** - Identificador UUID del usuario

#### Response
- **usuario** - Usuario con cada uno de sus campos

#### Errores
- **400** - Causado por un id inválido o porque faltan datos

#### Request de ejemplo
`PATCH /api/usuario-update/e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40`

`PUT /api/usuario-update/e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40`

#### Cuerpo (PATCH)
Con `PATCH` se puede actualizar parcialmente un Usuario
Se puede actualizar uno o varios campos

- **nombre** - nombre nuevo de usuario

#### Cuerpo (PUT)

Con `PUT` se actualizan todos los campos del usuario menos el id (se deben ingresar todos los campos en el cuerpo).

- **nombre** - "new Juan",
- **appellido** - "new Astorga",
- **email** - "newjastorga@gmail.com",
- **fecha_nacimiento** - "1980-12-10",


#### Example Response
`200 OK`

```javascript
{
  "id": "e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40",
  "nombre": "new Juan",
  "apellido": "new Astorga",
  "email": "newjastorga@gmail.com",
  "fecha_nacimiento": "1980-12-10"
}
```


### Eliminar Usuario

Si el request es correcto, se elimina una instancia 'Usuario', dado su id.

`DELETE /api/usuario-delete/{id}/`


#### Parámetros
- **id** - Identificador UUID del usuario

#### Response
- **message** - Mensaje de borrado exitoso.

#### Errores
- **400** - Causado por un id inválido

#### Request de ejemplo
`GET /api/usuario-delete/e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40`


#### Example Response
`200 OK`

```javascript
{
    "message": "El usuario con id e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40 se ha eliminado exitosamente"
}
```

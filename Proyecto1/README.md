# Proyecto 1 - Telematica (PIBL)
Con el fin de afianzar los conceptos trabajados en clase, en el presente proyecto
práctico desarrollamos y desplegamos un proxy inverso con balanceador de carga a partir del uso de
sockets, en lo siguiente explicaremos como gestionamos la concurrencia y persistencia del proxy.
discutiremos aspectos como el porqué del desarrollo del PIBL en python3, el uso de threads y sus ventajas, además de una explicación concisa de como ejecutar el proxy y los servidores desde AWS.

## Arquitectura del proyecto
![Arquitectura](https://i.postimg.cc/hGs4QMpH/project1-image.jpg)

## Desarrollo
El proyecto fue desplegado siguiendo una arquitectura cliente/Servidor, tal que el proxy inverso se encargue de recibir
las peticiones del cliente y funcione como tercero redirigiendo dicha petición a uno de los servidores, de manera inversa,
el mismo proxy recibe la respuesta del servidor y la entrega al cliente.

**Cliente:** quien solicita el recurso web, ya sea desde un browser, desde una terminarl de la máquina local o una plataforma
de API (ej. Postman).

**Servidor**: en terminos prácticos es la máquina que se encarga de procesar la petición del cliente y quien envía una respuesta
respecto al recurso solicitado por el cliente.

**Proxy**: el proxy inverso con balanceador de carga (PIBL) es quien funciona como mediador entre el cliente y el servidor.

Entrando más en detalle respecto a la infraestructura implementada, se crearon tres instancias en EC2 que sirven como servidores,
todas tres corriendo el mismo recurso (replicado), en el puerto 8080; una página sencilla tipo formulario gestionada con node.js.

![Formulario prueba](https://i.postimg.cc/LsR10wpJ/mycompanytk.png)

para correr los servidores es necesario seguir la ruta a continuación dentro de la instancia:

```
  ubuntu@ip-instance:~/st0255-2022/LabWebService N4/WebApp-Node/api
```
y ejecutar el siguiente comando:

```
  $ sudo node index.js
```

## Proxy
El proxy inverso con balanceo de carga fue implementado con python3, haciendo uso específicamente 
de las siguientes librerias:

* *socket* --> para poder generar las conecciones basadas en sockets.
* *configparser* --> para gestionar el archivo de configuración '.ini'.
* *_thread* --> para poder hacer multithreading, con el fin de soportar varios request de manera concurrente.
* *time* --> para gestionar el TTL.

El PIBL recibe la petición del cliente por medio de un socket, seteado por default en el puerto 8080, para así
realizar la verificación en caché de si el recurso solicitado ha sido requerido anteriormente, en caso de que si
se procede a calcular la diferencia de tiempo entre el último request de dicho tipo y el tiempo actual para verificar
si su ttl no se ha vencido, en caso de que no, se entrega como response al cliente el recurso desde caché, en caso contrario (que
el ttl se haya vencido) se procede a enviar el request a algún server por medio de un nuevo socket, a qué server se enviará la
petición se calcula por medio de Round Robin, que es fácil de implementar indexando las ips de los servidores en una lista.
Cuando se hace una petición que termina siendo gestionada por algún servidor, se guarda una copia del response en
caché.

Para correr el proxy es necesario ubicarse en el directorio root de la instancia y ejecutar el siguiente comando:
```
  $ python3 parser.py
```
Esto generará un archivo con los settings por default. son los siguientes:
* *port:* puerto en el que las terminarles se van a comunicar (8080 por default).
* *max_conn:* máxima conección que soportarán los sockets (5 por default). 
* *buffer_size:* tamaño del buffer para las peticiones HTTP (8192 por default).
* *ttl:* tiempo de vida de los recursos (20 segundos por default).
* *ip_serverX:* dirección IP pública v4 del servidor X (X de 1 a 3).

```
  [DEFAULT]
  port = 8080
  max_conn = 5
  buffer_size = 8192
  ttl = 180
  ip_server1 = 54.152.81.179
  ip_server2 = 52.23.107.62
  ip_server3 = 3.232.160.126
```

En caso de querer cambiar algún valor, desde la dirección root de la instancia ejecutar:
```
  $ nano parser.ini
```
Efectuar los cambios y guardar.

Es necesario ejecutar primero el parser para poder generar el archivo de configuración,
seguidamente se puede el proxy. Para ello desde dirección root ejecutar:
```
  $ python3 proxy.py
```
Aparecerá en consola lo siguiente:
```
  [*] Init socket... Done.
  [*] socket binded successfully...
  [*] Server started successfully [8080]
```
Lo cual significa que el proxy está escuchando peticiones en el puerto 8080, la data traída
de cada response será visible en consola, antecedida por una descripción como:
```
  [*] Request done: 181.136.32.82 => 0.2587890625.3s <= 54.152.81.179
```
IP del cliente => tiempo de ejecución <= IP del servidor.
En caso de que la respuesta sea desde caché, se verá lo siguiente antes de la data:
```
  [*] Request done. Cache response to => 181.136.32.82
```

## Python y threads
Como equipo desarrollador de la práctica escogimos implementar el proxy en Python dado que 
tenemos mayor dominio del lenguage en comparación a Rust y C, sería una práctica significativa
migrar nuestra implementación a un lenguage como C a modo de reto. En terminos de la estructura
del proxy, usamos la estrategia de multithreading para darle robustes en cuanto a la capacidad de
respuesta, ya que si extrapolamos la práctica al mundo real, el servicio del proxy debe soportar
petición simultaneas con un nivel de carga  bastante alto. 

## Referencias
* https://www.geeksforgeeks.org/python-time-module/
* https://yasoob.me/2013/08/06/python-socket-network-programming/
* https://www.geeksforgeeks.org/multithreading-python-set-1/
* https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
* https://docs.python.org/3.10/library/_thread.html?highlight=thread#module-_thread

## Autores
- [@jjsanchezc](https://github.com/jjsanchezc)
- [@Isaac1502](https://github.com/Isaac1502)
- [@DJara14](https://github.com/DJara14)

# Proyecto 
Implementar un Proxy Inverso + Balanceador de carga (PIBL) 
1. Debe permitir peticiones, que las procese y la envie a uno de los 3 servidores para poder retornar la respuesta al cliente
2. Se debe emplear la API Sockets
3. Se debe soportar peticiones de fomr aconcurrente desde diferentes tipos de clientes que envien peticiones
4. Se requiere que se procesen peticiones para HTTP/1.1
5. Se requiere que el sevidor escuche peticiones en el puerto 8080. Una vez se reciba la peticón de un cliente, se debe inicar un nuevo socket cliente para comunicarse con el servidor web destino elegido
6. Una vez envié la petición al servidor, debe esperar la respuesta y enviarla al cliente web que la solicito que solicite el recurso web
7. Se requiere que la aplicación PIBL implemente un proceso 'log' donde se registren todas las peticiones que recibe. El log debe permitir registrar todas las peticiones que se reciben y debe visualizar la petición que se hace y la respuesta que se entrega. Esto se debe visualizar por la salida estándar, y de igual forma, se debe implementar el registro en un archivo
8. La función de proxy debe permitir el caché para los diferentes recursos que se esoliciten por parte de los clientes. Para esto debe considerar lo siguiente:
  - para todos los recursos solicitados en las peticiones hecha por los clientes, la respuesta debe ser almacenada en un archivo en el disco del servisor. De esta forma se garantiza que el cachpe perissta en caso tal que se presente una falla en el servidor PIBL. Así, la próxima vez que se realice la petición de este recurso, se debe acceder al disco y enviar la respuesta desde aquí hacia el cliente
  - Los recursos para almacenar en el caché deben ser localizados en el derectorio donde se ejecuta la aplicación principal del PIBL.
  - Se debe implementar un mecanismo para un TTL para cada recurso que se mantenga en el caché. Esto debe ser un pará metro que se pase al momento de lanzar una aplicación.
9. Para efectos de destribución de la carga de las peticiones, se debe implementar *Round Robin*
10. El PIBL debe tener un archovo de confuguración que permita parametrizar el puerto en el que se ejecuta (ej: el puerto predeterminado es el 8080) así como icluir la lista de servidores que contestan peticiones

## ¿Qué se debe desplegar?
- Servidor PIBL
- 3 Servidores de aplicacion web
  - la aplicacion debe replicar en los tres servidores
## Recursos
- Todo se debe desplegar usando AWS 

## Datos importantes para la entrega
La entrega se debe realizar por el buzón de entrega por interactiva virtual. La
documentación se debe incluir en el repo en un archivo README.md. En este
archivo se requiere que usted incluya los detalles de implementación donde como
mínimo se esperan las siguientes secciones:

- Introducción.
- Desarrollo
- Conclusiones
- Referencias
## Versión:
- Fecha de Creación: septiembre 26.
- Fecha de primera actualización: octubre .

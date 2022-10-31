# Proyecto 2 Telematica

##  Despliegue aplicacion y NGINX

En este proyecto podemos ver un desarollo de una aplicacion web en wordpress con el fin de dar a conocer los productos de una empresa y la opinion de las personas a cerca de esos productos con una cantidad maxima de 150 caracteres. 
para poder hacer esto utilizamos wordpress para la modificacion y creacion de la pagina web, NGINX como servidor proxy inverso y configuramos el balanceador de carga tambien desde NGINX

##  Configuracion Proxy

Esta es la configuracion que usamos para el proxy de NGNX :
```
upstream php-handler {

        server unix:/var/run/php/php7.4-fpm.sock;  
}

server {

        listen 80;
        server_name proyectotelematica2.tk www.proyectotelematica2.tk;
        root /var/www/wordpress;
        index index.php;

        location / {
                try_files $uri $uri/ /index.php?$args;
        }

        location ~ .php$ {
                include snippets/fastcgi-php.conf;
                fastcgi_pass php-handler;
        }
} 
```
## Configuracion del balanceador de cargas

Siguiendo los siguientes comandos entramos a la configutacion del balanceador de carga:

```
cd /etc/nginx/sites-enabled
```
abrimos el wordpress.conf, podemos ver que dentro de upstream php-handler hay diferentes servidores


## Desarrollo
para empezar creamos la instancia HostMiCompany E2C en aws el cual tiene almacenado la base de datos de la pagina, la configuracion de la pagina desarollada en wordpress, la configuracion del NGINX como proxy y dentro del mismo aws configuramos un target group para si poder realizar un balanceador de carga
ademas de tener la configuracion de los DNS  primario y secundario dentro de esta misma instancia.

El proyecto cuenta con una infraestructura de nube IasS
imagen del modelo IasS: https://postimg.cc/xXXrRR2V

## Prueba de pagina
```
cd /etc/nginx/sites-available  

sudo mysql -u root -p

contraseña de la bas de datos proyecto2

use paginaP2_db

SELECT post_content FROM wp_posts;
```
Antes de que empiecen las lineas blancas que aparecen, están los datos que los usuarios han montado

## Referencias 
- https://www.youtube.com/watch?v=hq8kWcpGUvw
- https://www.youtube.com/watch?v=Zv15U50oGbw
- https://www.chakray.com/es/configura-nginx-loadbalancer-cluster-dos-nodos-wso2-ei/#:~:text=El%20balanceador%20de%20carga%20distribuye,de%20integraci%C3%B3n%20de%20c%C3%B3digo%20abierto.
- https://www.redhat.com/es/topics/cloud-computing/what-is-iaas
- https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-a-private-network-dns-server-on-centos-7

## Autores

- Isaac Tadina
- Juan José Sanchez
- Daniel Jaramillo



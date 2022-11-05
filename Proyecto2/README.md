# Proyecto 2 Telematica

# Prueba 1

##  Despliegue aplicacion y NGINX

En este proyecto podemos ver un desarollo de una aplicacion web en wordpress con el fin de dar a conocer los productos de una empresa y la opinion de las personas a cerca de esos productos con una cantidad maxima de 150 caracteres. 
para poder hacer esto utilizamos wordpress para la modificacion y creacion de la pagina web, NGINX como servidor proxy inverso y configuramos el balanceador de carga 

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
Para empezar creamos la instancia HostMiCompany E2C en aws el cual tiene almacenado la base de datos de la pagina, la configuracion de la pagina desarollada en wordpress, la configuracion del NGINX como proxy y dentro del mismo aws configuramos un target group para si poder realizar un balanceador de carga
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
## Pagina Web:
- http://proyectotelematica2.tk/home/

# Prueba 2 "corrección"

## Despliegue de aplicación

Para la corrección del proyecto anteriror hicimos una pagina de prueba en en wordpress

## Proxy + Load Balancer 

El proxy esta hecho en apache2 y el balanceador de carga esta configurado desde la opcion de balanceador de aws

### Configuración del load balancer

```
o<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/wordpress

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```
## Desarrollo 

Como en la prueba 1 hicimos las configuraciones de las instancias E2C los dos host, los DNS y su balanceador de carga, los dns estan configurados con bind9 y el proxy con apache2 como en el proyecto anteriror, ademas de la app web de prueba que desarrollamos en wordpress con direccion a loadBalancerWS-1193972895.us-east-1.elb.amazonaws.com



## Referencias 

- https://www.youtube.com/watch?v=hq8kWcpGUvw
- https://www.youtube.com/watch?v=Zv15U50oGbw
- https://www.chakray.com/es/configura-nginx-loadbalancer-cluster-dos-nodos-wso2-                                                        ei/#:~:text=El%20balanceador%20de%20carga%20distribuye,de%20integraci%C3%B3n%20de%20c%C3%B3digo%20abierto.
- https://www.redhat.com/es/topics/cloud-computing/what-is-iaas
- https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-a-private-network-dns-server-on-centos-7
- https://www.fosslinux.com/7631/how-to-install-and-configure-dns-on-ubuntu.htm
- https://www.youtube.com/watch?v=4IuNKK2y49s
- https://www.youtube.com/watch?v=8Uofkq718n8


## Autores

- Isaac Tadina
- Juan José Sanchez
- Daniel Jaramillo



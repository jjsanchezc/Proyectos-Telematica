**Despliegue e Integración de Servicios Proyecto II** 

**Telemática** 

1. **Objetivo** 

Desarrollar  habilidades  en  la  configuración,  así  como  despliegue  de  aplicaciones  y servicios en red, particularmente las que requieren de una arquitectura cliente/servidor. 

2. **Problemática** 

La  empresa  MiCompany  S.A.,  requiere  de  un  mecanismo  basado  en  tecnologías  de información (TI) que le permita capturar la opinión de los consumidores en relación con los diferentes productos que tienen en el mercado.  

En este sentido, le han solicitado a su empresa de soluciones de TI, que implemente una estrategia que le permita recolectar lo que piensan los usuarios de los productos. En la actualidad, la empresa cuenta con un catálogo de cincuenta (50) productos. Básicamente, lo que se requiere es que el usuario pueda expresar lo que piensa de uno o varios productos en particular, en no mas de ciento cincuenta caracteres (150). Tenga en cuenta que, la única intención de la empresa es que, posterior al proceso de recolección de datos, se puedan aplicar técnicas de minería de texto sobre la información recolectada (p.ej, sentiment  analysis,  topic  detection,  etc)  con  el  fin  de  extraer  información  de  cómo perciben los productos los clientes. 

El director de TI de su empresa, ha decido para satisfacer la necesidad, implementar y desplegar una aplicación web para este proyecto. Al respecto, se ha definido que la aplicación debe contar con un proceso de registro de usuarios el cual captura: nombre, edad, ciudad, dirección, correo electrónico, entre otros datos relevantes (información sociodemográfica  de  los  usuarios).  De  igual  forma,  la  aplicación  debe  permitir  la visualización de cada uno de los productos que tiene la compañía en el mercado y le debe permitir al usuario seleccionar el producto para que este pueda dar su opinión de este. Vale resaltar que un usuario, puede seleccionar uno o varios productos con el fin de dar su opinión de este.  

Su área es la encargada de tanto del desarrollo como el despliegue de la aplicación web. Para esto se requiere que usted realice todo el proceso de diseño de la aplicación, la implementación, pruebas y puesta en producción de esta. Con respecto al proceso de despliegue,  su  empresa  ha  decidido  que  ésta  se  desplegada  considerando  una infraestructura de TI robusta y escalable para soportar la operación de la aplicación. Todo esto con el fin de garantizar como mínimo una disponibilidad de 99.5%. Tenga en cuenta que  la  aplicación  debe  desarrollarse  que  soporte  de  manera  concurrente  miles  de usuarios al igual que debe permitir escalar de manera horizontal. 

En este sentido, desde la perspectiva del desarrollo de software a nivel de tecnologías, usted puede considerar cualquiera de los Manejadores de Contenido (CMS por sus siglas en inglés)  disponibles en la actualidad (Drupal o Wordrpess), con el fin de desarrollar la aplicación para satisfacer la problemática planteada. Para efectos de la persistencia de datos,  se  debe  considerar  utilizar  bases  de  datos  propias  que  emplean  este  tipo  de soluciones.   

Por otro lado, en los aspectos relacionados con el despliegue, se ha decidido que la aplicación  web  debe  desplegarse  utilizando  un  proveedor  de  computación  en  nube, utilizando el modelo de infraestructura como servicio (IasS). Tenga en cuenta que para desplegar la aplicación se requiere que usted considere elementos como balanceadores de carga para lograr un buen despliegue de la solución, de tal forma, que el balanceador de  carga  sea  configurado  para  distribuir  las  peticiones  entrantes  entre  diferentes servidores web que se tienen y los usuarios puedan tener acceso a la aplicación web desplegada. Es importante resaltar que, para acceder la aplicación usted debe tener un gestionar y conseguir un dominio público gratis de tal forma que la aplicación debe accederse a través de una URL, como, por ejemplo, http://www.micompany.tk 

Finalmente se requiere por parte de sus servicios que configure un servidor DNS primario y secundario que sea capaz de resolver los diferentes recursos de registros como: 

- www.micompany.tk para el servicio web. 
- nsprimary.micompany.tk para el servidor primario DNS 
- nssecondary.micompany.tk para el servidor DNS secundario. 
- Y los demás que se requieran para poner en funcionamiento los servicios web y de resolución de nombres para la compañía. 
3. **Recursos**: 

Toda la arquitectura detallada en el ítem anterior debe ser desplegada en la nube de Amazon Web Services utilizando la cuenta que se le ha asignado en el curso. Para esto debe utilizar emplear instancias EC2 para la instalación y configuración de su solución. 

4. **Aspectos por considerar para el desarrollo de la práctica:** 

Para efectos de la evaluación de la práctica se requieren los siguientes entregables:** 

1. Dado que se implementó un producto software, se debe entregar la documentación propia de estos productos para el software desarrollado por el equipo de trabajo. 
1. Se requiere que se entregue, así como se explique en detalle la vista arquitectónica de despliegue de la aplicación.  
1. Se requiere la documentación detallada del proceso de configuración del despliegue de  los  servicios  implementados  (p.ej.,  servidor  web,  balanceador  de  carga (NGINX/Apache/HAPROXY). 
4. Se requiere la documentación del proceso de configuración del servicio de resolución de nombres. 
4. El despliegue de la aplicación debe hacerse utilizando Amazon Web Services (AWS) a través  de  la  cuenta  de  educate.  Puede  implementar,  para  efectos  de  prueba, escenario  en  máquinas  locales.  Pero  la  entrega,  así  como  sustentación  es  en  el ambiente de AWS 
5. **Grupos de trabajo:** 

a.  El proyecto II debe ser desarrollado en grupos de tres personas. 

6. **Fechas:** 
   1. **Fecha de inicio:** 26/27 de septiembre.** 
   1. **Fecha de entrega:** viernes 28 de octubre hasta las 23:59.** 
   1. **Sustentaciones:** A partir del viernes 29 de octubre. Cada equipo dispondrá de 35 minutos para la presentación de los detalles de su proyecto.** 
6. **Mecanismo de Entrega:** 

El procedimiento para la entrega del trabajo es el siguiente:** 

1. Se debe entregar vía el servicio de entrega de trabajos de EAFIT interactiva.  
1. Se  debe  entregar  un  documento  maestro  donde  describa  todos  los  aspectos necesarios para la configuración y despliegue del servicio propuesto. 
1. El archivo se debe entregar en formato PDF. El nombre del archivo debe estar conformado por el primer apellido de los integrantes del grupo. 
1. Se debe realizar la sustentación del trabajo propuesto. En esa fecha deben llevar el escenario desplegado. 
8. **Versión:** 
1. **Fecha de Creación:** septiembre 26.** 
1. **Fecha de primera actualización:** octubre 2 .** 

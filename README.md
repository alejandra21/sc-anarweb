# Anar Web
Repositorio de la página web del ANAR con todos sus componentes y funcionalidades. 

## Autores
Estudiantes de la Universidad Simón Bolívar que cursan el servicio comunitario.

## Instalación
Las instrucciones de instalación están disponibles [aquí](INSTALL.md).

## Configuración con Web Server Apache2
Los archivos de configuración para que el servidor web funcione correctamente son:
- `django.wsgi` (nexo entre apache y django-Python): `/home/server/AnarWeb/anar/django.wsgi`
- `apache2.conf` (archivo de configuración general del apache): `/etc/apache2/apache2.conf`
- `default` (archivo del virtualhost por default usado por apache actualmente configurado para sistema ANAR) `/etc/apache2/sites-available/default`

## Realización de respaldos
Primeramente, debe ingresar como usuario postgres y ejecutar `pg_dump anardb`. 
Éste creará un archivo `BackupXXXX-XX-XX.backup` con un volcado en SQL del esquema más el contenido de la base de datos.

NOTA: Las imágenes no son respaldadas por el compando `pg_dump`, éste solo guarda las rutas a éstas en la carpeta `upload`.

## Servidor
La carpeta de proyecto del sistema ANAR se encuentra en `/home/server/AnarWeb`

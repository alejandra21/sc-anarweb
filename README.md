###PASOS PARA INSTALAR EL SISTEMA ANAR DESDE CERO###

1) Instalar postgresql (version actual para el sistema ANAR = 9.1.9)

2) convertirse en usuario postgres: <sudo -i -u postgres>

3) crear usuario anar: <createuser -s -P anar>

4) introducir password <anarpass>

5) Crear base de datos (como usuario postgres) : <createdb anardb>

6) volver a ser superusuario: <logout>

7) instalar libpq-dev

8) instalar requirements.pip <sudo pip install -vr requirements.pip> (ojo con esto verificar bien que se instale todo lo necesario, si es necesario uno por uno.)
***8.1) Si hay problemas con Pil éste puede instalarse de panera separada utilizando el comando <sudo apt-get install python-pil>
***8.2) Eliminar Pil en el requirements.pip
***8.3) Volver a ejecutar <sudo pip install -vr requirements.pip>

9) En caso que psycopg2 no se instale correctamente haga lo siguiente:

***9.1) Es necesario instalar psycopg2 sin la herramienta pip, de la siguiente manera: <sudo apt-get install python-psycopg2>

***9.2) Ejecutar de nuevo el <sudo pip install -vr requirements.pip> para terminar de instalar los paquetes restantes

	OJO En caso que ejecute el comando y ya esten instalados todo los paquetes, saldra el mensaje "Requirement already satisfied"

10)A ese nivel, ya se deberia poder ver la interfaz del sistema. Probar con: python manage.py runserver y visitando: localhost:8000

11) En la carpeta del proyecto sincronizar la base de datos python manage.py syncdb (si pide usuario y password, puede usar usuario: anar y password: anarpass, igual como esta estipulado en el settings.py)

12) Migrar la base de datos python manage.py migrate

13) Como usuario postgres(punto 2), asegurarse de estar en la carpeta de respaldos </home/server/Anarweb/respaldos/> accesar a la base de datos asi: <psql anardb> y luego ejecutar BackupXXXX-XX-XX.backup asi: <\i BackupXXXX-XX-XX.backup>
(ojo XXXX-XX-XX es la fecha mas recente del Respaldo)

14)[NO OBLIGATORIO] Reconstruir indice de busqueda <python manage.py rebuild_index>  (Para las busquedas aun no implementadas completamente) 

15) Status del servidor Web Apache2 : <service apache2 status> en caso de NO estar corriendo activarlo con: <service apache2 start> con esto el sitio deberia estar disponible desde la direccion IP del servidor para cualquier IP externa.



####INFO SERVIDOR###
la carpeta de proyecto del sistema ANAR se encuentra en "/home/server/AnarWeb"
###INFO CONFIG APACHE###
lo archivos de configuracion para que el servidor web funcione correctamente son:
<django.wsgi> (nexo entre apache y django-Python): "/home/server/AnarWeb/anar/django.wsgi"
<apache2.conf> (archivo de configuracion general del apache): "/etc/apache2/apache2.conf"
<default> (archivo del virtualhost por default usado por apache actualmente configurado para sistema ANAR) "/etc/apache2/sites-available/default"


### INFO PARA RESPALDOS ###
hacer respaldos: 
1)Convertirse en usuario postgres: <sudo -i -u postgres>

2)Para respaldar -> lanzar "pg_dump" : <pg_dump anardb> esto creara un archivo "BackupXXXX-XX-XX.backup" con un volcado en SQL del esquema + data, en caso de necesitar algo distindo revisar documentacion de "pg_dump" OJO importante esto no respaldara imagenes, la DB solo almacena rutas a estas imagenes en la carpeta "upload" dentro de la carpeta principal del sistema ANAR, para respaldarla es necesario copiarla.

3)Para insertar respaldo repetir pasos 2 , 5 y 13 en ese orden.

### INFO GIT ###
tener cuidado al actualizar el servidor con GIT ya que este cambia los permisos de acceso a las carpetas lo que impide agregar archivos. en caso de que esto ocurra cambiar los permisos para la carpeta "upload" para permitir la lectura y escritura de archivos de otros usuarios.

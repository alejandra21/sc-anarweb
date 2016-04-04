#Instrucciones para la instalación del sistema ANAR.

### 1. Instalar pip.
Para instalarlo, ejecute el siguiente comando:
```
sudo apt-get install python-pip
```

### 2. Prepare la base de datos.

El sistema ANAR utiliza PostgreSQL versión 9.1.9. Puede conseguir las instrucciones de 
instalación [aquí](http://www.postgresql.org/download/)

Ingrese como usuario postgres utilizando:
```
sudo service postgresql start
sudo sudo -u postgres psql
```

Seguidamente, cree el usuario y la contraseña para la base de datos del sistema.
```sql
CREATE USER anar WITH PASSWORD 'anarpass';
CREATE DATABASE anardb OWNER anar;
```

Se puede conectar a la base de datos creada ejecutando:
```
sudo sudo -u postgres psql -d anardb
```

Para que la aplicación trabaje conjuntamente con postgreSQL, debe instalar `python-dev`, `libpq-dev` y
`psycopg2` con los siguientes comandos:
```
sudo apt-get install python-dev
sudo apt-get install libpq-dev
sudo apt-get install python-psycopg2
```

### 3. Instale los requerimientos del sistema

Ejecute el siguiente comando:
```
sudo pip install -vr requirements.pip
```
NOTA: Es importante verificar la correcta instalación de cada requerimiento. En caso de fallos, debe 
proceder a una instalación manual de cada uno.

### 4. Sincronizar y migrar la base de datos
Debe ejecutar los siguientes comandos con usuario `anar` y contraseña `pass`:
```
python manage.py syncdb
python manage.py migrate
````

Seguidamente, conéctese a la base de datos como usuario postgres y ejecute el siguiente comando (sustituyendo XXXX-XX-XX con la fecha más reciente del respaldo):
```
\i BackupXXX-XX-XX.backup
```

### 5. Reconstruir índice de búsqueda (No obligatorio)
```
python manage.py rebuild_index
```

### 6. Ejecute la aplicación
```
python manage.py runserver
```
Luego, visite el sitio: `localhost:8000`

NOTA: para verificar el estatus del servidor Web Apache2 ejecute 
`service apache2 status` y para activarlo ejecute `service apache2 start`

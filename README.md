Este trabajo es un proyecto de Django en el que se va a gestionar las tareas y los usuarios.
Para ello se crea primero el proyecto de Django con sus respectivas apps.
Después de eso hay que modificar los ajustes y las urls de la app principal.

1. En ajustes se añaden las apps secundarias creadas anteriormente, es decir, tareas y usuarios. De esta forma va a servir para que se pueda mostrar la información creada de cada app.
Después se añade información de la BBDD. En ella hay que poner la conexión con la BBDD creada con PostgreSQL.
Otra cosa que hay que hacer es añadir las rutas en las urls porque así se podrá visualizar en el navegador lo que se ha creado.

2. Una vez configurada la app principal, se hace la app de tareas, que ahi se va a crear los atributos que se quieren usar, las funciones de crear tarea, cómo se crea, cómo se almacena,
   para que tipo de usuario va dirigida, la validación, si está completada o no...
   
3. Cuando se haya acabado con las tareas, se hace lo mismo pero con usuarios. En este caso va a crear usuario, segun su rol, registrarlo, loguearlo,listarlo, que pueda crear tareas...

4. Hay un apartado que se llama templates. En él se encuentran los ficheros HTML. Va a haber un fichero de tarea de los alumnos, otro de tarea de profesor, el registro del usuario,
   el inicio de sesion, un listado...

5. Para configurar la BBDD con Django hay instalar una librería especial para que permita conectarse con la BBDD. Esa librería es psycopg2-binary.
   
6. Una vez terminado de programar el proyecto hay ejecutarlo para comprobarlo. Pero antes hay que hacer unas migraciones con los siguientes comandos. (python -m manage.py makemigrations /
   python -m manage.py migrate). Y para arrancar el servidor hay que poner el siguiente comando (python -m manage runserver)

7. Ahora se comprobará en el navegador de que funciona correctamente.

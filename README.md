# Task queue software
Una cola de tareas es una estructura de datos mantenida por un programador de trabajos que contiene trabajos para ejecutar. El software de cola de tareas también administra el trabajo en segundo plano que debe ejecutarse fuera del ciclo habitual de solicitud-respuesta de HTTP.


Están diseñados para operaciones asíncronas, es decir, las operaciones se ejecutan en un modo sin bloqueo, lo que permite que la operación principal continúe procesando.


Resumen: Permite la ejecución de tareas en segundo plano sin bloquear el proceso de petición http normal

## Ejemplos
- Celery
- Redis Queue
- Taskmaster
- Huey
- tasq

# Message broker
Un intermediario de mensajes permite que las aplicaciones, los sistemas y los servicios se comuniquen e intercambien información entre sí. Ahora, con un software de cola de tareas en segundo plano, la aplicación web necesita conocer el estado del trabajo en curso, además de cualquier error que pueda ocurrir y el resultado de la mejora. Un intermediario de mensajes facilita este proceso, ya que está diseñado para hacer procesos independientes, es decir, "hablar entre sí".

## Ejemplos
- IBM MQ
- Beanstalk
- RabbitMQ
- Redis
- Gearman
- Solace

## Celery and Rabbitmq
La cola de tareas asíncrona de Celery permite la ejecución de tareas y su concurrencia lo hace
útil en varios sistemas de producción pero la ejecución de tareas necesita intermediarios de mensajes para funcionar sin problemas.


RabbitMQ es la mejor opción, ya que garantiza la entrega de mensajes, es tolerante a fallas, admite la replicación síncrona, lo que permite que SSL establezca una conexión cifrada y es excelente para aplicaciones en tiempo real.

# Instalar requirements.txt
Ingresar al entorno virtual
`pip install -r requirements.txt`
Con eso instalaras celery junto a otras dependencias del proyecto

# Instalar rabbitmq
`sudo apt-install rabbitmq-server`

## Añadir y configurar usuario específico para rabbitmq
`sudo rabbitmqctl add_user myuser(nombre usuario) mypassword(contraseña)`

## Añadir host virtual
`sudo rabbitmqctl add_vhost myvhost(nombre de host)`

## Configurar permisos
`sudo rabbitmqctl set_permissions -p myvhost(tu host) myuser(tu usuario) ".*" ".*" ".*"`

- .*: el primero da al usuario ermisos para configurar entidades
- .*: el segundo da permisos de escritura sobre cada entidad
- .*: el tercero da permisos de lectura

# Archivo .env conf. necesaria
## Datos de la conf. del brocker rabbitmq
`CELERY_BROKER_URL=amqp://myuser:mypassword@localhost/myvhost`
## Datos de la db a usar
`CELERY_BACKEND_URL=db+sqlite:///test.db`


# Ejecución de celery worker
`celery -A app worker -l info`
app: archivo donde se encuentra la conf de celery

# Ejecución de flask server
`flask run --debug`

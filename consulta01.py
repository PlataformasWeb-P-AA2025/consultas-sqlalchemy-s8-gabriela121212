
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from clases import *
from config import cadena_base_datos
# Crea una conexión con la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

entregas = (
    #con el join unimos las tablas ejemplo entrega-estudiante como la relacion que esta en el modelo de datos para acceder a los datos del estudiante que hizo la entrega
    #asi con las demas tablas entrega-tarea para saber la tarea a la que corresponde esa esa entrega
    session.query(Entrega).join(Entrega.estudiante).join(Entrega.tarea).join(Tarea.curso).join(Curso.instructor).join(Curso.departamento)
    #filtra los departamentos cuyo nombre del curso sea igual Arte y all ejecutamos la consulta
    .filter(Departamento.nombre == "Arte").all()
)
# Recorremos cada objeto
for entrega in entregas:
    # Imprimimos el título de la tarea y asi imprimimos los demas resultadoslas demas
    print(f"Tarea: {entrega.tarea.titulo}")
    print(f"Estudiante: {entrega.estudiante.nombre}")
    print(f"Instructor: {entrega.tarea.curso.instructor.nombre}")
    print(f"Departamento: {entrega.tarea.curso.departamento.nombre}")
    print(f"Calificación: {entrega.calificacion}")
    print(f"Fecha envío: {entrega.fecha_envio}")

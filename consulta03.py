from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from clases import *
from config import cadena_base_datos
# Crea una conexión con la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy import func

# Consulta para obtener departamentos con entregas con calificación <= 0.3

#creamos un array con los nombres que se pide para la consulta
nombres_estudiantes = [
    "Jennifer Bolton",
    "Elaine Perez",
    "Heather Henderson",
    "Charles Harris"
]

tareas = (
    # Seleccionamos la tabla Tarea
    session.query(Tarea)
    # Relación unimos las tablas con el join Entrega y esztudiante relacion en la tabla
    .join(Entrega).join(Estudiante)
    # Filtramos estudiantes cuyo nombre este en este array
    .filter(Estudiante.nombre.in_(nombres_estudiantes)).all()
)

# Mostrar resultados
for tarea in tareas:
    #imprimos tareas asignadas
    print(f"Tarea: {tarea.titulo}")
    #imprimos el numero de entregas que tiene con len
    #print(f"número de entregas: {len(tarea.entrega)}")
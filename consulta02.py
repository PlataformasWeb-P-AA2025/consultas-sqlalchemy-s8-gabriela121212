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



departamentos = (
    # Seleccionamos el nombre del departamento
    # Contamos la cantidad de cursos que tiene el departamento
    session.query(Departamento)
    # Relación unimos las tablas departamento-curso segun su relacion en la tabla
    .join(Curso).join(Tarea).join(Entrega)
    # Filtramos entregas con calificación menor o igual a 0.3 y ejecutamos la consulta
    .filter(Entrega.calificacion <= 0.3).all()
)

# Mostrar resultados
for departamento in departamentos:
    #imprimos el curso y el numero de cursos
    print(f"Departamento: {departamento.nombre}")
    print(f"Departamento: {len(departamento.cursos)}")
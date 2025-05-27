from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from clases import *
from config import cadena_base_datos
# Crea una conexión con la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy import func

# Obtener todos los cursos
cursos = session.query(Curso).all()



for curso in cursos:
    #se consulta todas la entregas haciendo un una union con tarea y filtramos accediendo al curso a traves de su id y lo compramos y ejecutamos
    entregas = session.query(Entrega).join(Tarea).filter(Tarea.curso_id == curso.id).all()
    
    #evita que se aplica nulo a funcion sum evitando errores
    if entregas:
        #aqui promediamos sumando todas las calificacciones de entregas usando la funcion sum y dividivos para el numero de entregas
        promedio = sum(entrega.calificacion for entrega in entregas) / len(entregas)
        
        #imprimos el curso
        print(f"Titulo Curso: {curso.titulo}")
        #imprimos la calificacion y formateo el elemento para dos decimales
        print(f"Promedio de calificaciones: {promedio:.2f}")

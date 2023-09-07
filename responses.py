from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hola"):
        return "Hola soy un chatbot de autorrespuesta, escoge la pregunta que quieras hacer \n\n1)Pregunta 1 \n2)Pregunta 2 \n3)Pregunta 3 \n4)Pregunta 4 \n5)Pregunta 5 \n6)Pregunta 6 \n7)Contactanos"
    
    if user_message in ("1) ¿Cuándo inician las inscripciones?"):
        return "Cordial saludo La Universidad convocará semestralmente la inscripción de aspirantes para ingresar a sus diferentes programas académicos, mediante aviso en un periódico de circulación nacional y regional, en las carteleras de la Institución y en otros medios masivos de comunicación, anunciando los requisitos exigidos y las fechas establecidas para tal efecto."
    
    if user_message in ("2) ¿Qué requisitos se requieren para el proceso de transferencia interna o externa?"):
        return "Cordial saludo."
        "Dando respuesta a su solicitud, Los requisitos a tener en cuenta son:"
        "- No haber transcurrido más de dos semestres, desde el último cursado."
        "- Acreditar un promedio acumulado mínimo de 3.6 en las calificaciones del programa académico de procedencia"
        "- Acreditar un puntaje en el Examen de Estado superior o igual al del último estudiante admitido, durante el semestre inmediatamente anterior, sin considerar el puntaje de los admitidos por condiciones especiales."
        "Por lo tanto, debe adjuntar certificado de notas por semestre y resultado icfes para realizar verificación y estudio"
    
    if user_message in ("3"):
        return "Placeholder 3"
    
    if user_message in ("4"):
        return "Placeholder 4"
    
    if user_message in ("5"):
        return "Placeholder 5"
    
    if user_message in ("6"):
        return "Placeholder 6"
    
    if user_message in ("7"):
        return "Informacion de contacto placeholder"
 

    return "Opcion no encontrada, intenta otra vez."
    
    

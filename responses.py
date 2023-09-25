from datetime import datetime
import psycopg2




cur=None


def surveyNO(input_text):
    
    user_message = str(input_text).lower()
    
    try:
    
        conn = psycopg2.connect(
        
            host = 'localhost',
            user = 'postgres',
            password = '1234',
            database = 'ChatbotQA',
            port = '5432'
        
        )
        cur = conn.cursor()

        
        cur.execute('UPDATE "Surveys" SET "NO"= 1 WHERE id=1')
        
        return 'Voto tomado'
        
        
    except Exception as ex:
        print(ex)
    
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def surveySI(input_text):
    
    user_message = str(input_text).lower()
    
    try:
    
        conn = psycopg2.connect(
        
            host = 'localhost',
            user = 'postgres',
            password = '1234',
            database = 'ChatbotQA',
            port = '5432'
        
        )
        cur = conn.cursor()

        
        cur.execute('UPDATE "Surveys" SET "SI"="SI"+1 WHERE id=1')
        return 'Voto tomado'    
        
        
        
    except Exception as ex:
        print(ex)
    
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def addQ(input_text):
    
    user_message = str(input_text).lower()
    
    try:
    
        conn = psycopg2.connect(
        
            host = 'localhost',
            user = 'postgres',
            password = '1234',
            database = 'ChatbotQA',
            port = '5432'
        
        )
        cur = conn.cursor()

        return 'pregunta agregada'
        
        
        
    except Exception as ex:
        print(ex)
    
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


    

def connection(input_text):

    user_message = str(input_text).lower()
    
    try:
    
        conn = psycopg2.connect(
        
            host = 'localhost',
            user = 'postgres',
            password = '1234',
            database = 'ChatbotQA',
            port = '5432'
        
        )
    
        cur = conn.cursor()
    
        cur.execute('SELECT * FROM "QAs"')

        if user_message in ("a"):
            
            matrix = ""
            for row in cur.fetchall():
                
              response = str(row[0]),row[1]
              
              rst = ' '.join(response)
              rst2 = rst+'\n'
              
              matrix += rst2
              
              print(rst)
              
            print(matrix)
              
              
            
            return matrix 
        
        if user_message in ("1"):
            
            matrix = ""
            for row in cur.fetchall():
               
              if row[0] == 1:
                  
                matrix = row[2]
      
            print(matrix)
                
            return matrix 
        
        if user_message in ("2"):
            
            matrix = ""
            for row in cur.fetchall():
               
              if row[0] == 2:
                  
                matrix = row[2]
      
            print(matrix)
                
            return matrix 
        
        if user_message in ("3"):
            
            matrix = ""
            for row in cur.fetchall():
               
              if row[0] == 3:
                  
                matrix = row[2]
      
            print(matrix)
                
            return matrix 
              
            
            
        if user_message in ("4"):
            
            matrix = ""
            for row in cur.fetchall():
               
              if row[0] == 4:
                  
                matrix = row[2]
      
            print(matrix)
                
            return matrix 
        
        if user_message in ("5"):
            
            matrix = ""
            for row in cur.fetchall():
               
              if row[0] == 5:
                  
                matrix = row[2]
      
            print(matrix)
                
            return matrix 
        
        if user_message in ("6"):
            
            matrix = ""
            for row in cur.fetchall():
               
              if row[0] == 6:
                  
                matrix = row[2]
      
            print(matrix)
                
            return matrix 
        
        if user_message in ("7"):
            
            matrix = ""
            for row in cur.fetchall():
               
              if row[0] == 7:
                  
                matrix = row[2]
      
            print(matrix)
                
            return matrix 
        
        if user_message in ("8"):
            
            matrix = ""
            for row in cur.fetchall():
               
              if row[0] == 8:
                  
                matrix = row[2]
      
            print(matrix)
                
            return matrix 
        
        
            
            

            
        
        
        else:
            return "opcion invalida"
        

        print("conexion exitosa")
    except Exception as ex:
        print(ex)
    
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()







'''
def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hola"):
        return "Hola soy un chatbot de autorespuesta, escoge la pregunta que quieras hacer \n\n1)¿Cuándo inician las inscripciones? \n2)Qué requisitos se requieren para el proceso de transferencia interna o externa? \n3)Pregunta 3 \n4)Pregunta 4 \n5)Pregunta 5 \n6)Pregunta 6 \n7)Contactanos"
    
    if user_message in ("1) ¿Cuándo inician las inscripciones?"):
        return "Cordial saludo \nLa Universidad convocará semestralmente la inscripción de aspirantes para ingresar a sus diferentes programas académicos, mediante aviso en un periódico de circulación nacional y regional, en las carteleras de la Institución y en otros medios masivos de comunicación, anunciando los requisitos exigidos y las fechas establecidas para tal efecto."
    
    if user_message in ("2) ¿Qué requisitos se requieren para el proceso de transferencia interna o externa?"):
        return "Cordial saludo."
        "Dando respuesta a su solicitud, Los requisitos a tener en cuenta son:"
        "- No haber transcurrido más de dos semestres, desde el último cursado."
        "- Acreditar un promedio acumulado mínimo de 3.6 en las calificaciones del programa académico de procedencia"
        "- Acreditar un puntaje en el Examen de Estado superior o igual al del último estudiante admitido, durante el semestre inmediatamente anterior, sin considerar el puntaje de los admitidos por condiciones especiales."
        "Por lo tanto, debe adjuntar certificado de notas por semestre y resultado icfes para realizar verificación y estudio"
    
    if user_message in ("3) ¿Cuánto cuesta un certificado de notas de graduado de pregrado y cómo se realiza el proceso para solicitarlo?"):
        return "Cordial saludo \nPara responder a su solicitud debe cancelar el valor de $69.600 que cuesta el certificado de notas de graduado de pregrado ,por lo cual para realizar el proceso debe ingresar a recaudo online por el siguiente link: https://pe.uptc.edu.co/app/#/ ingrese ; en SERVICIOS UNIVERSITARIOS, luego VER PORTAFOLIO SERVICIOS, identifica los certificados que necesita en los cuales aparece el costo identifica la operación a realizar,lo selecciona, da click en SIGUIENTE, diligencia la información solicitada teniendo en cuenta que la casilla de *Destino hace referencia a la entidad para donde va dirigido el certificado, luego da click en AGREGAR, luego da click en REALIZAR PAGO y continúe realizando el pago, lo puede hacer con tarjeta crédito, débito o si es en efectivo selecciona bancos y diligencia el cupón de pago para llevar al banco luego enviar comprobante de pago con los datos de la persona que lo solicita (nombre,código,carrera y certificado que se requiere y el destino o entidad a donde va dirigido ) al correo admisiones.sogamoso@uptc.edu.co y en asunto solicitud de certificado."
    
    if user_message in ("4) Buenas tardes(días), ¿cuánto cuesta un certificado de notas de graduado de posgrado y cómo se realiza el proceso para solicitarlo?"):
        return "Cordial saludo  \nPara responder a su solicitud debe cancelar el valor de $34.800 que cuesta el certificado de notas de graduado de posgrados ,por lo cual para realizar el proceso debe ingresar a recaudo online por el siguiente link: https://pe.uptc.edu.co/app/#/ ; ingrese en SERVICIOS UNIVERSITARIOS, luego VER PORTAFOLIO SERVICIOS, identifica los certificados que necesita en los cuales aparece el costo identifica la operación a realizar, lo selecciona, da clic en SIGUIENTE, diligencia la información solicitada teniendo en cuenta que la casilla de *Destino hace referencia a la entidad para donde va dirigido el certificado, luego da click en AGREGAR, luego da click en REALIZAR PAGO y continúe realizando el pago, lo puede hacer con tarjeta crédito, débito o si es en efectivo selecciona bancos y diligencia el cupón de pago para llevar al banco luego enviar comprobante de pago con los datos de la persona que lo solicita (nombre,código,carrera y certificado que se requiere y el destino o entidad a donde va dirigido )al correo admisiones.sogamoso@uptc.edu.co y en asunto solicitud de certificado."
    
    if user_message in ("5) ¿Cuáles son los ponderados exigidos para cada programa de la seccional?"):
        return "Cordial saludo \nLa información solicitada la puede encontrar en la página de la uptc www.uptc.edu.co en el micro sitio de admisiones ,en pregrado presencial o pregrado a distancia o virtual según la modalidad que desea ingresar a estudiar y en el paso tres encontrará los puntajes de referencia teniendo en cuenta que se toma el semestre anterior al de la inscripción en ese momento ,de igual manera en el paso dos encontrará un simulador que le ayudará para hacer el cálculo con su puntaje del icfes para verificar si cumple con el puntaje que se exige para ese momento."
    
    if user_message in ("6) ¿Soy estudiante de terminación académica y requiero un certificado de todas las notas vistas en mi programa por lo cual como lo solicitó y lo cancelo?"):
        return "Cordial saludo \nDebe cancelar por medio de recaudo online en el ítem de certificado de notas por semestres estudiantes activos, debe cancelar $3000 por cada semestre cursado luego enviar comprobante de pago con los datos de la persona que lo solicita (nombre, código, carrera y certificado que se requiere) al correo admisiones.sogamoso@uptc.edu.co y en asunto solicitud de certificado."
    
    if user_message in ("7) ¿Quisiera saber cuándo es el costo del valor de la matrícula para los programas que se ofertan en la universidad?"):
        return "El valor de la matrícula se realiza por estudio socioeconómico."

    if user_message in ("8) Para mas informacion"):
        return "Para mas informacion puede contactarse directamente con el area de admisiones al siguiente correo: admisiones.sogamoso@uptc.edu.co"
 

    return "Opcion no encontrada, intenta otra vez."

''' 
    

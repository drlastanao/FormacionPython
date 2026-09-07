texto="""
Título: La arquitectura del tiempo y la memoria en la era digital
Introducción
Durante milenios, la relación entre el ser humano y la información estuvo mediada por la fragilidad física. Los papiros se desgastaban, las bibliotecas ardían y los relatos orales se transformaban a medida que pasaban de generación en generación. La memoria era un ejercicio de selección activa, donde olvidar no solo era inevitable, sino también necesario para la supervivencia cultural. Sin embargo, la llegada de la era digital ha alterado radicalmente esta dinámica. Hoy en día, no nos enfrentamos a la escasez de datos, sino a su acumulación desmedida. La memoria ya no es un registro selectivo, sino un archivo infinito que se expande a cada segundo.Esta transformación plantea preguntas fundamentales sobre cómo procesamos la información, cómo construimos nuestro conocimiento y cómo interactuamos con el tiempo. Para navegar por este nuevo escenario, es indispensable analizar los mecanismos que rigen la producción de datos, la evolución de los medios de almacenamiento y el impacto que estas tecnologías tienen en la cognición humana.1. La transición de lo analógico a lo digitalEl cambio de soporte material a formato digital ha modificado no solo la velocidad con la que transmitimos ideas, sino la naturaleza misma del mensaje. En el entorno analógico, la creación de un contenido exigía un esfuerzo tangible. Un libro requería impresión, distribución y espacio físico en un estante. Esta limitación material imponía un filtro implícito: solo aquello que superaba ciertos estándares de relevancia lograba perdurar.Por el contrario, la infraestructura digital ha reducido los costos de distribución y almacenamiento a niveles casi nulos. Cualquier persona con acceso a una red puede generar y difundir contenido de manera instantánea. Esto ha democratizado el acceso a la información, pero también ha generado una saturación informativa sin precedentes.Soportes analógicos: Limitados por el espacio, la degradación física y la dificultad de duplicación.Soportes digitales: Infinitos en capacidad teórica, reproducibles sin pérdida de calidad y accesibles en tiempo real.2. El fenómeno de la sobrecarga informativaEl concepto de infoxicación o sobrecarga informativa describe la incapacidad de un individuo para procesar el volumen de datos al que expuesto diariamente. Cuando la cantidad de información supera la capacidad cognitiva de procesamiento, la toma de decisiones se deteriora y el aprendizaje se vuelve superficial.
+-----------------------------------------------------------------------+
|                    El Ciclo de la Infoxicación                        |
|                                                                       |
|  [ Gran Volumen de Datos ] ---> [ Incapacidad de Filtrado ]           |
|            ^                                     |                    |
|            |                                     v                    |
|  [ Mayor Producción ] <--- [ Atención Fragmentada y Fatiga ]          |
+-----------------------------------------------------------------------+
Para contrarrestar este fenómeno, la sociedad ha tenido que desarrollar herramientas de mediación. Los algoritmos de búsqueda, las plataformas de recomendación y las arquitecturas de inteligencia artificial no son meros lujos tecnológicos; son filtros indispensables para evitar la parálisis analítica. Sin embargo, delegar la selección de datos en algoritmos automatizados introduce un nuevo problema: la creación de burbujas de eco y sesgos de confirmación.3. La redefinición del aprendizaje y la atenciónLa inmediatez de la red ha alterado la forma en que consumimos y estructuramos el conocimiento. La lectura profunda y sostenida, que caracteriza al pensamiento analítico tradicional, compite constantemente con la estimulación intermitente de las plataformas digitales. La atención se ha convertido en el recurso más escaso de la economía moderna.Cambios en los patrones cognitivosLectura en diagonal (Skimming): La tendencia a escanear textos en busca de palabras clave en lugar de procesar el argumento completo.Pensamiento hipervinculado: La navegación continua entre diferentes fuentes de información, lo que fomenta una comprensión transversal pero a menudo fragmentada.Memoria de trabajo externa: La tendencia a delegar el almacenamiento de datos en dispositivos externos, confiando en la capacidad de recuperarlos en lugar de memorizarlos.Este último punto, conocido popularmente como el Efecto Google, no implica necesariamente una pérdida de capacidad intelectual, sino una reorganización de la memoria humana. La mente deja de ser un almacén de datos fácticos para convertirse en un centro de gestión de rutas de acceso.4. El archivo permanente y el derecho al olvidoUno de los aspectos más complejos de la preservación digital es la persistencia de los datos. En el mundo físico, el tiempo borra las huellas de forma natural. Las conversaciones informales se las lleva el aire y los errores del pasado se atenúan con el paso de los años. En la red, en cambio, las acciones dejan una huella imborrable en forma de metadatos, registros de actividad y archivos indexados.Esta permanencia por defecto ha dado lugar a debates éticos y jurídicos de gran calado, como la necesidad de regular el derecho al olvido. La capacidad de reiniciar, de perdonar y de reinventarse depende en gran medida de la posibilidad de que el pasado no determine de forma absoluta el presente."Una sociedad que no puede olvidar se vuelve incapaz de perdonar, ya que el recuerdo permanente de cada error paraliza la evolución de los individuos y las instituciones."5. Estrategias para una convivencia digital sostenibleAnte este panorama, el desafío fundamental de nuestra época no consiste en rechazar la tecnología ni en añorar un pasado analógico idealizado, sino en desarrollar una alfabetización digital madura. Esto requiere adoptar hábitos de consumo de información conscientemente estructurados.DimensiónEnfoque Pasivo (Saturación)Enfoque Activo (Criterio)ConsumoReactivo, basado en notificaciones y feeds.Programado, priorizando fuentes verificadas.ProcesamientoAcumulación masiva de marcadores y pestañas.Sintesis, notas personales y mapas mentales.AlmacenamientoConfianza ciega en archivos digitales externos.Curaduría propia y respaldos estructurados.La gestión efectiva de la información implica aprender a desconectar, a filtrar con criterio crítico y a valorar el silencio cognoscitivo. Solo mediante una relación intencionada con la tecnología podremos transformar el flujo incesante de datos en conocimiento estructurado y, en última instancia, en sabiduría.ConclusiónLa era digital nos ha otorgado un poder sin precedentes para crear, preservar y compartir ideas. No obstante, este poder conlleva la responsabilidad de gestionar nuestros recursos mentales con prudencia. La arquitectura de la memoria humana siempre ha sido flexible y moldeable por las herramientas que utiliza. Al comprender los riesgos de la sobrecarga y los mecanismos de la atención, podemos construir un entorno tecnológico que no sustituya nuestra capacidad de pensar, sino que la amplifique de manera equilibrada y sostenible.
"""
import re
from unidecode import unidecode

frecuencias = {}

def quitar_caracteres_especiales(palabra):
    """Elimina caracteres especiales de una palabra, dejando solo letras y números."""
    palabra = palabra.lower()  # Normalizar a minúsculas
    palabra = unidecode(palabra)
    return re.sub(r'[^a-z0-9áéíóúüñ]', '', palabra)


def añadir_palabra(palabra):
    """Añade una palabra al diccionario de frecuencias.

    Si la palabra ya existe, incrementa su contador; si no, la inicializa en 1.
    """
    palabra = quitar_caracteres_especiales(palabra)  # Limpiar caracteres no alfabéticos

    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

for palabra in texto.split():
    añadir_palabra(palabra)



#ordenar el diccionario por frecuencia de mayor a menor
frecuencias_ordenadas = dict(sorted(frecuencias.items(), key=lambda item: item[1], reverse=True))


print(frecuencias_ordenadas)





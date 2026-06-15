from django.shortcuts import render

BASE_DE_DATOS = {
    'supervivencia': [
        {
            'nombre': 'Sidney Prescott', 
            'nombre_url': 'sidney-prescott', 
            'especialidad': 'Atletismo Evasivo', 
            'edad': 18, 
            'descripcion': 'Sidney es una sobreviviente nata. Descubrió su talento corriendo por los pasillos de la escuela para escapar de situaciones extremas, destacando especialmente en su inigualable capacidad para esquivar obstáculos y mantener la calma bajo presión.'
        },
        {
            'nombre': 'Tommy Jarvis', 
            'nombre_url': 'tommy-jarvis', 
            'especialidad': 'Estrategia y Liderazgo', 
            'edad': 17, 
            'descripcion': 'Aunque ha pasado por traumas que lo mantienen siempre alerta, Tommy tiene un talento natural para organizar a sus compañeros y planear defensas en situaciones de crisis. Sabe exactamente cómo prepararse para enfrentar cualquier amenaza.'
        }
    ],
    'mecanica': [
        {
            'nombre': 'Herbert West', 
            'nombre_url': 'herbert-west', 
            'especialidad': 'Biología Experimental', 
            'edad': 18, 
            'descripcion': 'Herbert pasa sus recesos encerrado en el laboratorio de ciencias. Es un genio incomprendido en anatomía y química. Tiene la asombrosa (y algo perturbadora) habilidad de experimentar y "reanimar" especímenes usando extraños reactivos.'
        },
        {
            'nombre': 'John Kramer', 
            'nombre_url': 'john-kramer', 
            'especialidad': 'Ingeniería y Mecanismos', 
            'edad': 19, 
            'descripcion': 'John es un estudiante meticuloso y calculador. Su talento mecánico es fascinante: diseña rompecabezas físicos, puede desarmar cerraduras y construir sistemas y trampas complejas que ponen a prueba el instinto de sus compañeros.'
        }
    ],
    'arte': [
        {
            'nombre': 'Daniel Robitaille', 
            'nombre_url': 'daniel-robitaille', 
            'especialidad': 'Arte Urbano y Retratos', 
            'edad': 18, 
            'descripcion': 'Misterioso y trágico, Daniel es el responsable de los murales más impresionantes de los muros traseros del colegio. Algunos bromean diciendo que si miras sus pinturas fijamente al espejo y dices su nombre cinco veces, su arte cobra vida.'
        },
        {
            'nombre': 'Gale Weathers', 
            'nombre_url': 'gale-weathers', 
            'especialidad': 'Fotoperiodismo de Riesgo', 
            'edad': 18, 
            'descripcion': 'Gale es la audaz fotógrafa del periódico escolar. Tiene un talento inquietante para estar siempre en el lugar correcto cuando ocurre un incidente, acechando desde las sombras para conseguir la "foto perfecta" a cualquier costo.'
        },
        {
            'nombre': 'Jack Torrance', 
            'nombre_url': 'jack-torrance', 
            'especialidad': 'Literatura de Terror', 
            'edad': 18, 
            'descripcion': 'Apasionado por la escritura, Jack tiene un talento increíble para crear relatos que mantienen a todos despiertos de noche. Suele pasar horas tecleando repetitivamente en la biblioteca, completamente aislado de la realidad.'
        }
    ],
    'psicologia': [
        {
            'nombre': 'Hannibal Lecter', 
            'nombre_url': 'hannibal-lecter', 
            'especialidad': 'Análisis de Comportamiento', 
            'edad': 18, 
            'descripcion': 'Hannibal es un estudiante extremadamente culto, refinado y observador. Su talento radica en la psicología analítica; siempre está atento a su entorno y puede "leer" los miedos y anticipar las acciones de los demás con una precisión escalofriante.'
        }
    ]
}

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def categoria(request, nombre_categoria):
    alumnos = BASE_DE_DATOS.get(nombre_categoria.lower(), [])
    titulos = {
        'supervivencia': 'Supervivencia',
        'mecanica': 'Mecánica y Tecnología',
        'arte': 'Artes Oscuras',
        'psicologia': 'Psicología Analítica'
    }
    contexto = {
        'titulo_categoria': titulos.get(nombre_categoria.lower(), nombre_categoria.capitalize()),
        'alumnos': alumnos
    }
    return render(request, 'categoria.html', contexto)

def ficha(request, nombre_url):
    alumno_encontrado = None
    for categoria_lista in BASE_DE_DATOS.values():
        for alumno in categoria_lista:
            if alumno['nombre_url'] == nombre_url:
                alumno_encontrado = alumno
                break
                
    contexto = {'alumno': alumno_encontrado}
    return render(request, 'ficha.html', contexto)
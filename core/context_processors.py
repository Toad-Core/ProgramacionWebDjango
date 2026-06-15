from .views import BASE_DE_DATOS

def lista_categorias_global(request):
    # Mapeamos los nombres técnicos a los nombres bonitos que verá el usuario
    titulos = {
        'supervivencia': 'Supervivencia',
        'mecanica': 'Mecánica y Tecnología',
        'arte': 'Artes Oscuras',
        'psicologia': 'Psicología Analítica'
    }
    
    categorias_limpias = []
    # Recorremos las llaves de tu diccionario en views.py ('supervivencia', 'mecanica', etc.)
    for slug in BASE_DE_DATOS.keys():
        categorias_limpias.append({
            'slug': slug,
            'nombre_visible': titulos.get(slug, slug.capitalize())
        })
        
    # Retornamos un diccionario. Esta variable estará viva en TODO el sitio web
    return {
        'CATEGORIAS_MENU': categorias_limpias
    }
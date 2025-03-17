from supabase import supabase

# Insertar cotización
def insertar_cotizacion(data):
    return supabase.table('cotizaciones').insert(data).execute()

# Obtener cotizaciones
def obtener_cotizaciones():
    return supabase.table('cotizaciones').select('*').execute()

# Actualizar cotización
def actualizar_cotizacion(cotizacion_id, data):
    return supabase.table('cotizaciones').update(data).eq('id', cotizacion_id).execute()

# Eliminar cotización
def eliminar_cotizacion(cotizacion_id):
    return supabase.table('cotizaciones').delete().eq('id', cotizacion_id).execute()


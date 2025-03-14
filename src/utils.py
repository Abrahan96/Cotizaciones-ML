from supabase import create_client, Client
import os

# Conexión a Supabase
url = "https://eyemokwxswevabnuldej.supabase.co"  # Tu URL de Supabase
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV5ZW1va3d4c3dldmFibnVsZGVqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5Mjg3NjAsImV4cCI6MjA1NzUwNDc2MH0.PrlwMQ4Exxuo1dGfclqmwBDnchRQ_7mQFi1hjiZKcno"  # API Key (service_role)
supabase: Client = create_client(url, key)

def insertar_cotizacion(numero_cotizacion, cliente, direccion, mecanico, subtotal, igv, total):
    data = {
        "numero_cotizacion": numero_cotizacion,
        "cliente": cliente,
        "direccion": direccion,
        "mecanico": mecanico,
        "subtotal": subtotal,
        "igv": igv,
        "total": total
    }
    return supabase.table("cotizaciones").insert(data).execute()

# Obtener todas las cotizaciones
def obtener_cotizaciones():
    response = supabase.table("cotizaciones").select("*").execute()
    return response.data
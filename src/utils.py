from supabase import create_client, Client
import os

# Clave secreta de Supabase
SUPABASE_URL = "https://eyemokwxswevabnuldej.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV5ZW1va3d4c3dldmFibnVsZGVqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5Mjg3NjAsImV4cCI6MjA1NzUwNDc2MH0.PrlwMQ4Exxuo1dGfclqmwBDnchRQ_7mQFi1hjiZKcno"

# Conexión
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insertar_cotizacion(numero_cotizacion, cliente, direccion, mecanico, subtotal, igv, total):
    data = {
        "numero_cotiz": numero_cotizacion,
        "cliente": cliente,
        "direccion": direccion,
        "mecanico": mecanico,
        "subtotal": subtotal,
        "igv": igv,
        "total": total
    }
    supabase.table("cotizaciones").insert(data).execute()
    
def obtener_cotizaciones():
    response = supabase.table("cotizaciones").select("*").execute()
    return response.data



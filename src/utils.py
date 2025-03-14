from supabase import create_client, Client
import os

# Clave secreta de Supabase
SUPABASE_URL = "https://eyemokwxswevabnuldej.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV5ZW1va3d4c3dldmFibnVsZGVqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5Mjg3NjAsImV4cCI6MjA1NzUwNDc2MH0.PrlwMQ4Exxuo1dGfclqmwBDnchRQ_7mQFi1hjiZKcno"

# Conexión
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

data = {
    "numero_cotizacion": "COT-001",
    "cliente": "Juan Pérez",
    "direccion": "Av. Los Robles 123",
    "mecanico": "Carlos",
    "subtotal": 100.0,
    "igv": 18.0,
    "total": 118.0
}

response = supabase.table("cotizaciones").insert(data).execute()
print(response.data)


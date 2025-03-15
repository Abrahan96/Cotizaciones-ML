from supabase import create_client, Client
import os

# Clave secreta de Supabase
SUPABASE_URL = "https://eyemokwxswevabnuldej.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV5ZW1va3d4c3dldmFibnVsZGVqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5Mjg3NjAsImV4cCI6MjA1NzUwNDc2MH0.PrlwMQ4Exxuo1dGfclqmwBDnchRQ_7mQFi1hjiZKcno"

# Conexión
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insertar_cotizacion(numero_cotizacion, cliente, ruc, direccion, mecanico, equipo, marca, modelo, fecha, subtotal, igv, total, estado):
    data = {
        "numero_cotizacion": numero_cotizacion,
        "cliente": cliente,
        "ruc": ruc,
        "direccion": direccion,
        "mecanico": mecanico,
        "equipo": equipo,
        "marca": marca,
        "modelo": modelo,
        "fecha": str(fecha),
        "subtotal": subtotal,
        "igv": igv,
        "total": total,
        "estado": estado
    }
    supabase.table("cotizaciones").insert([data]).execute()
    
def obtener_cotizaciones():
    response = supabase.table("cotizaciones").select("*").execute()
    return response.data

# ACTUALIZAR COTIZACIÓN

def actualizar_cotizacion(id_cotizacion, nuevos_datos):
    try:
        print(f"ID de Cotización a actualizar: {id_cotizacion}")
        print(f"Datos a actualizar: {nuevos_datos}")

        response = supabase.table("cotizaciones").update(nuevos_datos).eq("id", id_cotizacion).execute()

        print(f"Respuesta de Supabase: {response}")
        return response
    except Exception as e:
        print(f"Error al actualizar la cotización: {e}")
        return None

# ELIMINAR COTIZACIÓN
def eliminar_cotizacion(id_cotizacion):
    response = supabase.table("cotizaciones").delete().eq("id", id_cotizacion).execute()
    return response

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile

def generar_pdf(cotizacion):
    # Crear un archivo temporal para el PDF
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    file_path = temp_file.name
    
    # Crear el PDF
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(30, 750, "🔧 COTIZACIÓN - MANTENIMIENTO DE MONTACARGAS 🔧")
    c.drawString(30, 730, f"Cliente: {cotizacion['cliente']}")
    c.drawString(30, 710, f"RUC: {cotizacion['ruc']}")
    c.drawString(30, 690, f"Dirección: {cotizacion['direccion']}")
    c.drawString(30, 670, f"Mecánico: {cotizacion['mecanico']}")
    c.drawString(30, 650, f"Equipo: {cotizacion['equipo']}")
    c.drawString(30, 630, f"Marca: {cotizacion['marca']}")
    c.drawString(30, 610, f"Modelo: {cotizacion['modelo']}")
    c.drawString(30, 590, f"Fecha: {cotizacion['fecha']}")
    c.drawString(30, 570, f"Subtotal: S/. {cotizacion['subtotal']}")
    c.drawString(30, 550, f"IGV (18%): S/. {cotizacion['igv']}")
    c.drawString(30, 530, f"Total: S/. {cotizacion['total']}")
    c.drawString(30, 500, f"Estado: {cotizacion['estado']}")
    
    c.save()
    return file_path


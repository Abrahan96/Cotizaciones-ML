from supabase import create_client, Client
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Credenciales desde .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Conexión a Supabase
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

def actualizar_cotizacion(id_cotizacion, nuevos_datos):
    response = supabase.table("cotizaciones").update(nuevos_datos).eq("id", id_cotizacion).execute()
    return response

def eliminar_cotizacion(id_cotizacion):
    response = supabase.table("cotizaciones").delete().eq("id", id_cotizacion).execute()
    return response

def generar_pdf(cotizacion):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    file_path = temp_file.name

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

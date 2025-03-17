from reportlab.pdfgen import canvas

def generar_pdf(cotizacion):
    c = canvas.Canvas(f"cotizacion_{cotizacion['id']}.pdf")
    c.drawString(100, 750, f"Cotización N° {cotizacion['id']}")
    c.drawString(100, 730, f"Cliente: {cotizacion['cliente']}")
    c.drawString(100, 710, f"Producto: {cotizacion['producto']}")
    c.drawString(100, 690, f"Total: S/. {cotizacion['total']}")
    c.save()

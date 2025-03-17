import streamlit as st
from utils import insertar_cotizacion, obtener_cotizaciones, actualizar_cotizacion, eliminar_cotizacion
from pdf import generar_pdf
import os

# Título de la aplicación
st.title("🛠️ API de Cotizaciones con Supabase y PDF 📝")

# Insertar Cotización
st.subheader("Insertar Cotización")
cliente = st.text_input("Cliente")
producto = st.text_input("Producto")
total = st.number_input("Total", min_value=0.0)

if st.button("Insertar Cotización"):
    data = {"cliente": cliente, "producto": producto, "total": total}
    insertar_cotizacion(data)
    st.success("Cotización insertada con éxito ✅")

# Ver Cotizaciones
st.subheader("Ver Cotizaciones")
cotizaciones = obtener_cotizaciones().data

if cotizaciones:
    st.table(cotizaciones)

# Actualizar Cotización
st.subheader("Actualizar Cotización")
cotizacion_id = st.number_input("ID de cotización a actualizar", min_value=1, step=1)
nuevo_total = st.number_input("Nuevo total", min_value=0.0)

if st.button("Actualizar Cotización"):
    actualizar_cotizacion(cotizacion_id, {"total": nuevo_total})
    st.success("Cotización actualizada ✅")

# Eliminar Cotización
st.subheader("Eliminar Cotización")
eliminar_id = st.number_input("ID de cotización a eliminar", min_value=1, step=1)

if st.button("Eliminar Cotización"):
    eliminar_cotizacion(eliminar_id)
    st.success("Cotización eliminada ✅")

# Generar PDF
st.subheader("Generar PDF de Cotización")
pdf_id = st.number_input("ID de cotización para PDF", min_value=1, step=1)

if st.button("Generar PDF"):
    cotizacion = next((c for c in cotizaciones if c['id'] == pdf_id), None)

    if cotizacion:
        generar_pdf(cotizacion)
        st.success("PDF generado ✅")
        with open(f"cotizacion_{cotizacion['id']}.pdf", "rb") as pdf_file:
            st.download_button(
                label="Descargar PDF",
                data=pdf_file,
                file_name=f"cotizacion_{cotizacion['id']}.pdf",
                mime="application/pdf"
            )
    else:
        st.error("❌ Cotización no encontrada.")

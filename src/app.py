import streamlit as st
from utils import insertar_cotizacion, obtener_cotizaciones, actualizar_cotizacion, eliminar_cotizacion, generar_pdf

st.title("🔧 API de Cotizaciones con Supabase y PDF 📝")

# 👉 Insertar Cotización
if st.button("Insertar Cotización"):
    insertar_cotizacion(
        numero_cotizacion="ML-0001",
        cliente="Inversiones SAC",
        ruc="20603040506",
        direccion="Av. Industrial 123",
        mecanico="Juan Pérez",
        equipo="Montacargas",
        marca="Toyota",
        modelo="A30",
        fecha="2025-03-17",
        subtotal=1500,
        igv=270,
        total=1770,
        estado="Pendiente"
    )
    st.success("✅ Cotización insertada con éxito")

# 👉 Mostrar todas las cotizaciones
if st.button("Ver Cotizaciones"):
    cotizaciones = obtener_cotizaciones()
    st.write(cotizaciones)

# 👉 Actualizar cotización
id_cotizacion = st.number_input("ID de cotización a actualizar", min_value=1)
if st.button("Actualizar Cotización"):
    nuevos_datos = {"estado": "Aprobado"}
    actualizar_cotizacion(id_cotizacion, nuevos_datos)
    st.success("✅ Cotización actualizada")

# 👉 Eliminar cotización
id_eliminar = st.number_input("ID de cotización a eliminar", min_value=1)
if st.button("Eliminar Cotización"):
    eliminar_cotizacion(id_eliminar)
    st.success("✅ Cotización eliminada")

# 👉 Generar PDF de cotización
id_pdf = st.number_input("ID de cotización para PDF", min_value=1)
if st.button("Generar PDF"):
    cotizaciones = obtener_cotizaciones()
    cotizacion = next((c for c in cotizaciones if c['id'] == id_pdf), None)
    if cotizacion:
        pdf_path = generar_pdf(cotizacion)
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(label="📄 Descargar PDF", data=pdf_file, file_name="cotizacion.pdf", mime="application/pdf")
    else:
        st.error("❌ Cotización no encontrada.")

import streamlit as st
import pandas as pd
from src.utils import insertar_cotizacion, obtener_cotizaciones

# Interfaz Streamlit
st.title("💻 Cotizaciones - Supabase 🚀")

# Formulario
with st.form("form_cotizacion"):
    numero_cotizacion = st.text_input("Número de Cotización")
    cliente = st.text_input("Cliente")
    direccion = st.text_input("Dirección")
    mecanico = st.text_input("Mecánico")
    subtotal = st.number_input("Subtotal", min_value=0.0)
    igv = subtotal * 0.18
    total = subtotal + igv

    submit = st.form_submit_button("💾 Guardar Cotización")

if submit:
    insertar_cotizacion(numero_cotizacion, cliente, direccion, mecanico, subtotal, igv, total)
    st.success("✅ Cotización guardada correctamente.")

# Mostrar datos
st.subheader("📄 Cotizaciones Registradas")
cotizaciones = obtener_cotizaciones()

if cotizaciones:
    df = pd.DataFrame(cotizaciones)
    st.dataframe(df)

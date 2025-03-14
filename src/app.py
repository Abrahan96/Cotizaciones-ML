import streamlit as st
from utils import insertar_cotizacion
from utils import obtener_cotizaciones

st.title("Cotización ML")

# Formulario
numero_cotizacion = st.text_input("Número de Cotización", value="ML-00001")
cliente = st.text_input("Cliente")
direccion = st.text_input("Dirección")
mecanico = st.text_input("Mecánico")
subtotal = st.number_input("Subtotal", min_value=0.0)
igv = subtotal * 0.18
total = subtotal + igv

st.write("IGV (18%): ", round(igv, 2))
st.write("Total: ", round(total, 2))

if st.button("Guardar Cotización"):
    insertar_cotizacion(numero_cotizacion, cliente, direccion, mecanico, subtotal, igv, total)
    st.success("Cotización guardada con éxito ✅")
    
# Llamamos a las cotizaciones desde Supabase
cotizaciones = obtener_cotizaciones()

# Mostramos los datos en una tabla
st.write("### Historial de Cotizaciones")
st.dataframe(cotizaciones)


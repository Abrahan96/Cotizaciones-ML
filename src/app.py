import streamlit as st
from utils import insertar_cotizacion, obtener_cotizaciones, actualizar_cotizacion, eliminar_cotizacion


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
    st.experimental_rerun()


# Llamamos a las cotizaciones desde Supabase
cotizaciones = obtener_cotizaciones()

# Mostramos los datos en una tabla
st.write("### Historial de Cotizaciones")
if cotizaciones:
    for cotizacion in cotizaciones:
        with st.expander(f"Cotización: {cotizacion['numero_cotiz']}"):
            st.write(f"Cliente: {cotizacion['cliente']}")
            st.write(f"Dirección: {cotizacion['direccion']}")
            st.write(f"Mecánico: {cotizacion['mecanico']}")
            st.write(f"Subtotal: {cotizacion['subtotal']}")
            st.write(f"IGV: {cotizacion['igv']}")
            st.write(f"Total: {cotizacion['total']}")

            # BOTONES DE CRUD
            col1, col2 = st.columns(2)
            
            # Actualizar cotización
            with col1:
                if st.button("📝 Editar", key=f"edit_{cotizacion['id']}"):
                    nuevo_cliente = st.text_input("Nuevo Cliente", value=cotizacion['cliente'])
                    nuevo_subtotal = st.number_input("Nuevo Subtotal", min_value=0.0, value=cotizacion['subtotal'])
                    nuevo_igv = round(nuevo_subtotal * 0.18, 2)
                    nuevo_total = round(nuevo_subtotal + nuevo_igv, 2)
                    
                    if st.button("Actualizar"):
                        actualizar_cotizacion(cotizacion['id'], {
                            "cliente": nuevo_cliente,
                            "subtotal": nuevo_subtotal,
                            "igv": nuevo_igv,
                            "total": nuevo_total
                        })
                        st.experimental_rerun()

            # Eliminar cotización
            with col2:
                if st.button("🗑️ Eliminar", key=f"delete_{cotizacion['id']}"):
                    eliminar_cotizacion(cotizacion['id'])
                    st.warning("Cotización eliminada 🗑️")
                    st.experimental_rerun()

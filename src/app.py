import streamlit as st
from utils import insertar_cotizacion, obtener_cotizaciones, actualizar_cotizacion, eliminar_cotizacion

st.title("Cotización ML")

# Lista de estados
opciones_estado = ["Pendiente", "Atendido", "Rechazado"]

# Formulario
numero_cotizacion = st.text_input("Número de Cotización", value="ML-00001")
cliente = st.text_input("Cliente")
ruc = st.text_input("Ruc")
direccion = st.text_input("Dirección")
mecanico = st.text_input("Mecánico")
equipo = st.text_input("Equipo")
marca = st.text_input("Marca")
modelo = st.text_input("Modelo")
fecha = st.date_input("Fecha")

if 'cotizacion' not in st.session_state:
    st.session_state['cotizacion'] = {}

subtotal = st.number_input(
    "Subtotal",
    min_value=0.0,
    value=float(st.session_state['cotizacion'].get('subtotal', 0.0))
)

igv = subtotal * 0.18
total = subtotal + igv

estado = st.selectbox(
    "Estado de la cotización",
    opciones_estado,
    index=0
)

st.write("IGV (18%): ", round(igv, 2))
st.write("Total: ", round(total, 2))

if st.button("Guardar Cotización"):
    try:
        insertar_cotizacion(numero_cotizacion, cliente, ruc, direccion, mecanico, equipo, marca, modelo, fecha, subtotal, igv, total, estado)
        st.success("Cotización guardada con éxito ✅")
        st.rerun()
    except Exception as e:
        st.error(f"Error al guardar: {e}")

# Inicializamos variables de edición
if 'modo_edicion' not in st.session_state:
    st.session_state['modo_edicion'] = False

if 'id_cotizacion_editar' not in st.session_state:
    st.session_state['id_cotizacion_editar'] = None

# Obtener cotizaciones desde Supabase
cotizaciones = obtener_cotizaciones()

st.write("### Historial de Cotizaciones")
if cotizaciones:
    for cotizacion in cotizaciones:
        with st.expander(f"Cotización: {cotizacion['numero_cotizacion']}"):
            st.write(f"Cliente: {cotizacion['cliente']}")
            st.write(f"Ruc: {cotizacion['ruc']}")
            st.write(f"Dirección: {cotizacion['direccion']}")
            st.write(f"Mecánico: {cotizacion['mecanico']}")
            st.write(f"Equipo: {cotizacion['equipo']}")
            st.write(f"Marca: {cotizacion['marca']}")
            st.write(f"Modelo: {cotizacion['modelo']}")
            st.write(f"Fecha: {cotizacion['fecha']}")
            st.write(f"Subtotal: {cotizacion['subtotal']}")
            st.write(f"IGV: {cotizacion['igv']}")
            st.write(f"Total: {cotizacion['total']}")
            st.write(f"Estado: {cotizacion['estado']}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("📝 Editar", key=f"edit_{cotizacion['id']}"):
                    st.session_state['modo_edicion'] = True
                    st.session_state['id_cotizacion_editar'] = cotizacion['id']
                    
            with col2:
                if st.button("🗑️ Eliminar", key=f"delete_{cotizacion['id']}"):
                    try:
                        eliminar_cotizacion(cotizacion['id'])
                        st.warning("Cotización eliminada 🗑️")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error al eliminar: {e}")

if 'modo_edicion' in st.session_state and st.session_state['modo_edicion']:
    cotizacion_a_editar = next(
        (c for c in cotizaciones if c['id'] == st.session_state['id_cotizacion_editar']),
        None
    )

    if cotizacion_a_editar:
        nuevo_cliente = st.text_input("Nuevo Cliente", value=cotizacion_a_editar['cliente'])
        nuevo_ruc = st.text_input("Nuevo RUC", value=cotizacion_a_editar['ruc'])
        nueva_direccion = st.text_input("Nueva Dirección", value=cotizacion_a_editar['direccion'])
        nuevo_mecanico = st.text_input("Nuevo Mecánico", value=cotizacion_a_editar['mecanico'])
        nuevo_equipo = st.text_input("Nuevo Equipo", value=cotizacion_a_editar['equipo'])
        nueva_marca = st.text_input("Nueva Marca", value=cotizacion_a_editar['marca'])
        nuevo_modelo = st.text_input("Nuevo Modelo", value=cotizacion_a_editar['modelo'])
        nueva_fecha = st.date_input("Nueva Fecha", value=cotizacion_a_editar['fecha'])
        nuevo_subtotal = st.number_input("Nuevo Subtotal", min_value=0.0, value=float(cotizacion_a_editar['subtotal']))

        # Corrección del cálculo de IGV y Total
        nuevo_igv = round(nuevo_subtotal * 0.18, 2)
        nuevo_total = round(nuevo_subtotal + nuevo_igv, 2)

        opciones_estado = ["Pendiente", "Atendido", "Rechazado"]
        nuevo_estado = st.selectbox(
            "Estado de la Cotización",
            opciones_estado,
            index=opciones_estado.index(cotizacion_a_editar['estado']) if cotizacion_a_editar['estado'] in opciones_estado else 0
        )

        if st.button("Actualizar Cotización"):
            actualizar_cotizacion(cotizacion_a_editar['id'], {
                "cliente": nuevo_cliente,
                "ruc": nuevo_ruc,
                "direccion": nueva_direccion,
                "mecanico": nuevo_mecanico,
                "equipo": nuevo_equipo,
                "marca": nueva_marca,
                "modelo": nuevo_modelo,
                "fecha": nueva_fecha.strftime("%Y-%m-%d"),  # Asegura el formato correcto
                "subtotal": nuevo_subtotal,
                "igv": nuevo_igv,
                "total": nuevo_total,
                "estado": nuevo_estado
            })

            st.success("✅ Cotización actualizada con éxito")
            st.session_state['modo_edicion'] = False
            st.session_state['id_cotizacion_editar'] = None
            st.rerun()
    else:
        st.error("No se encontró la cotización para editar.")
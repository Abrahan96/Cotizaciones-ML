from flask import Flask, request, jsonify, send_file
from utils import insertar_cotizacion, obtener_cotizaciones, actualizar_cotizacion, eliminar_cotizacion, generar_pdf

app = Flask(__name__)

# Ruta para insertar cotización
@app.route('/insertar', methods=['POST'])
def insertar():
    data = request.json
    insertar_cotizacion(**data)
    return jsonify({"mensaje": "Cotización insertada con éxito"}), 201

# Ruta para obtener todas las cotizaciones
@app.route('/cotizaciones', methods=['GET'])
def obtener():
    cotizaciones = obtener_cotizaciones()
    return jsonify(cotizaciones)

# Ruta para actualizar cotización
@app.route('/actualizar/<int:id_cotizacion>', methods=['PUT'])
def actualizar(id_cotizacion):
    nuevos_datos = request.json
    resultado = actualizar_cotizacion(id_cotizacion, nuevos_datos)
    return jsonify(resultado)

# Ruta para eliminar cotización
@app.route('/eliminar/<int:id_cotizacion>', methods=['DELETE'])
def eliminar(id_cotizacion):
    eliminar_cotizacion(id_cotizacion)
    return jsonify({"mensaje": "Cotización eliminada con éxito"}), 200

# Ruta para generar PDF
@app.route('/generar_pdf/<int:id_cotizacion>', methods=['GET'])
def generar_pdf_cotizacion(id_cotizacion):
    cotizaciones = obtener_cotizaciones()
    cotizacion = next((c for c in cotizaciones if c['id'] == id_cotizacion), None)
    if cotizacion:
        pdf_path = generar_pdf(cotizacion)
        return send_file(pdf_path, as_attachment=True)
    else:
        return jsonify({"error": "Cotización no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
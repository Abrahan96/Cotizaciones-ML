from flask import Flask, request, jsonify, send_file
from utils import (
    insertar_cotizacion, 
    obtener_cotizaciones, 
    actualizar_cotizacion, 
    eliminar_cotizacion, 
    generar_pdf
)

app = Flask(__name__)

# Ruta para insertar una cotización
@app.route('/insertar', methods=['POST'])
def insertar():
    datos = request.json
    response = insertar_cotizacion(datos)
    return jsonify(response), 201

# Ruta para obtener todas las cotizaciones
@app.route('/cotizaciones', methods=['GET'])
def listar_cotizaciones():
    cotizaciones = obtener_cotizaciones()
    return jsonify(cotizaciones), 200

# Ruta para actualizar una cotización
@app.route('/actualizar/<int:id_cotizacion>', methods=['PUT'])
def actualizar(id_cotizacion):
    nuevos_datos = request.json
    response = actualizar_cotizacion(id_cotizacion, nuevos_datos)
    return jsonify(response), 200

# Ruta para eliminar una cotización
@app.route('/eliminar/<int:id_cotizacion>', methods=['DELETE'])
def eliminar(id_cotizacion):
    response = eliminar_cotizacion(id_cotizacion)
    return jsonify(response), 200

# Ruta para generar PDF
@app.route('/pdf/<int:id_cotizacion>', methods=['GET'])
def generar_pdf_cotizacion(id_cotizacion):
    cotizaciones = obtener_cotizaciones()
    cotizacion = next((c for c in cotizaciones if c['id'] == id_cotizacion), None)
    if not cotizacion:
        return jsonify({'error': 'Cotización no encontrada'}), 404
    
    pdf_path = generar_pdf(cotizacion)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)




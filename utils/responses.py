from flask import jsonify

class HttpResponse:
  def __init__(self):
    self.response = {
      'codigo_http': 500,
      'data': {
        'ruta_imagen': None,
        'resultado': 'fallido',
        'porcentaje_eficiencia': 0.0,
        'clase': 'N/A'
      }
    }

  def set_error(self, status_code, message):
    self.response['codigo_http'] = status_code
    self.response['data']['resultado'] = 'fallido'
    self.response['data']['mensaje'] = message

  def set_success(self, ruta_imagen, clase, porcentaje_eficiencia):
    self.response['codigo_http'] = 200
    self.response['data']['resultado'] = 'exitoso'
    self.response['data']['ruta_imagen'] = ruta_imagen
    self.response['data']['clase'] = clase
    self.response['data']['porcentaje_eficiencia'] = porcentaje_eficiencia

  def get_response(self):
    return jsonify(self.response), self.response['codigo_http']
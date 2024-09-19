from flask import Flask, request
from tensorflow.keras.models import load_model
import os

# Importar las funciones y clases
from utils.preprocessing import load_and_preprocess_image
from utils.postprocessing import process_predictions
from utils.responses import HttpResponse

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar los modelos preentrenados para masculino y femenino
model_male = load_model('model/modelMale.keras')
model_female = load_model('model/modelFemale.keras')

# Definir las clases según tu modelo
class_names = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'SIO']  # Ajusta según tus clases

# Ruta para manejar las predicciones
@app.route('/predict', methods=['POST'])
def predict():
  http_response = HttpResponse()

  # Validar si el parámetro 'sex' está en la solicitud
  sex = request.form.get('sex')
  if sex not in ['M', 'F']:
    http_response.set_error(400, "El parámetro 'sex' es obligatorio y debe ser 'M' o 'F'.")
    return http_response.get_response()

  # Validar si se recibió el parámetro de la ruta del archivo
  filepath = request.form.get('filepath')
  if not filepath or not os.path.exists(filepath):
    http_response.set_error(400, "La ruta del archivo es inválida o no se encontró el archivo.")
    return http_response.get_response()

  # Seleccionar el modelo basado en el valor de 'sex'
  if sex == 'M':
    model = model_male
  else:
    model = model_female

  try:
    # Cargar y preprocesar la imagen desde la ruta
    img_array = load_and_preprocess_image(filepath)

    # Realizar la predicción con el modelo seleccionado
    predictions = model.predict(img_array)

    # Procesar las predicciones
    result = process_predictions(predictions, class_names)

    # Configurar la respuesta de éxito
    http_response.set_success(filepath, result['clase'], result['porcentaje_eficiencia'])

  except Exception as e:
    http_response.set_error(500, f"Error procesando la imagen: {str(e)}")

  return http_response.get_response()

if __name__ == '__main__':
  app.run(debug=True)
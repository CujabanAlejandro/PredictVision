import numpy as np
import tensorflow as tf

def process_predictions(predictions, class_names):
  """
  Procesa las predicciones del modelo para devolver el resultado en formato JSON.

  Args:
  - predictions: Array de predicciones del modelo.
  - class_names: Lista de nombres de clases correspondientes a las predicciones.

  Returns:
  - resultado: Diccionario con la clase predicha y el porcentaje de eficiencia.
  """
  # Convertir las predicciones a probabilidades con softmax
  score = tf.nn.softmax(predictions[0])
  # Obtener la clase predicha
  predicted_class_index = np.argmax(score)
  predicted_class = class_names[predicted_class_index]
  confidence = 100 * np.max(score)

  return {
    'clase': predicted_class,
    'porcentaje_eficiencia': confidence
  }
from tensorflow.keras.preprocessing import image
import numpy as np

def load_and_preprocess_image(file, target_size=(224, 224)):
  """
  Carga y preprocesa una imagen para la predicción.

  Args:
  - file: Archivo de imagen cargado desde una solicitud.
  - target_size: Tuplas que indican el tamaño al que redimensionar la imagen.

  Returns:
  - img_array: Array de imagen preprocesado listo para la predicción.
  """
  # Cargar la imagen y redimensionarla
  img = image.load_img(file, target_size=target_size)
  # Convertir la imagen a un array numpy
  img_array = image.img_to_array(img)
  # Añadir una dimensión de batch
  img_array = np.expand_dims(img_array, axis=0)
  # Normalizar los valores de píxeles (ajustar según el modelo)
  img_array = img_array / 255.0

  return img_array
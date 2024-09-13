from PIL import Image
import tensorflow as tf


def process_radiography_image(file):
    # Abre la imagen
    img = Image.open(file)
    
    # Preprocesamiento: transformar la imagen para que pueda ser leída por el modelo
    img = img.resize((224, 224))  # Ejemplo de tamaño
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0  # Normalización

    # Cargar el modelo de detección de anomalías (entrenado previamente)
    model = tf.keras.models.load_model('C:\\Users\\Diego\\Desktop\\API\\ModeloNeumoniaGRISES512512512256.h5')

    # Predecir
    prediction = model.predict(tf.expand_dims(img_array, axis=0))

    # Convertir la predicción a un formato legible (ej. porcentaje de anomalía)
    result = {'anomaly_score': float(prediction[0][0])}
    return result


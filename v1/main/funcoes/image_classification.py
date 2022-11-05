from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

model = load_model('../../keras_models/keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
size = (224, 224)
classes = [
    "RG verso",
    "CNH frente",
    "CPF frente",
]

def getImageClass(image_path):
    image = Image.open(image_path)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = classes[index]
    confidence_score = prediction[0][index]
    return {
        'confidence': int(confidence_score*100),
        'class': class_name
    }
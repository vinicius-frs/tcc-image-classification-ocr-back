from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

model = load_model('D:/Dev/Python/tcc-image-classification-ocr/keras_models/keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
size = (224, 224)
classes = [
    "CNH frente",
    "CNH verso",
    "RG frente",
    "RG verso",
    "CPF frente",
    "CPF verso"
]

def getImageClass(image_path):
    image = Image.open(image_path)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    predictions = []
    predictions = model.predict(data)

    greater_prediction = None
    greater_prediction_idx = None
    idx = 0
    for i in predictions[0]:
        if(greater_prediction == None or i > greater_prediction):
            greater_prediction = i
            greater_prediction_idx = idx
        idx += 1

    return {
        'confidence': int(greater_prediction*100),
        'class': classes[greater_prediction_idx]
    }
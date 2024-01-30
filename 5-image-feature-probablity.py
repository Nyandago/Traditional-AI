# Object recognition with a pre-trained model

from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Function to predict object in the image
def predict_object(image_path):
    model = MobileNetV2(weights='imagenet')
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    return decode_predictions(preds, top=6)[0]

# Example usage
image_path = 'no-face.png'
predictions = predict_object(image_path)
for _, object_name, probability in predictions:
    print(f"{object_name}: {probability:.2f}")

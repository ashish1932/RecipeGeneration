import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model

base_model = ResNet50(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)

def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    return features

def generate_recipe_from_image(img_path):
    features = extract_features(img_path)
    ingredients = ["tomato", "onion", "salt", "pepper"]
    instructions = "1. Chop all ingredients.\n2. Cook until soft.\n3. Serve hot."
    return ingredients, instructions

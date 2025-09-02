
# main.py - Entry point for the Recipe Generation Project
from model import generate_recipe_from_image

if __name__ == "__main__":
    image_path = "app/static/images/sample.jpg"
    ingredients, instructions = generate_recipe_from_image(image_path)
    print("Ingredients:", ingredients)
    print("Instructions:", instructions)

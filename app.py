from flask import Flask, render_template, request
from model import generate_recipe_from_image
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join("static/images", file.filename)
            file.save(file_path)
            ingredients, instructions = generate_recipe_from_image(file_path)
            return render_template("result.html", ingredients=ingredients, instructions=instructions, image_path=file.filename)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# 🍳 Recipe Generation from Images  

This project allows you to upload a food image and automatically generate a recipe, including a list of ingredients and cooking instructions. It combines **computer vision** for food recognition with **natural language generation** for recipe creation.  

---

## 🚀 Features  
- Upload an image of a dish 🍜  
- Detect and classify food items using deep learning models  
- Generate ingredient lists and step-by-step cooking instructions  
- Optionally suggest nutritional information (if enabled)  
- Web app and API support  

---

## 📂 Project Structure  
recipe-generation-from-image/
│── data/ # Sample food images
│── models/ # Pre-trained models (classification + recipe generation)
│── notebooks/ # Jupyter notebooks for experiments
│── src/ # Source code
│ ├── image_preprocessing.py
│ ├── food_classifier.py
│ ├── recipe_generator.py
│ └── app.py # Flask/FastAPI web app
│── requirements.txt # Python dependencies
│── README.md # Project documentation



---

## ⚙️ Installation  

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/recipe-generation-from-image.git
cd recipe-generation-from-image
Create virtual environment & install dependencies

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
Download pre-trained models
(Provide links or instructions to download classification + recipe generation models)

🖼️ Usage
1. Command Line
python src/app.py --image data/pasta.jpg
2. Web App
python src/app.py
Open browser at http://127.0.0.1:5000/ and upload a food image.

🧠 Tech Stack
Python 3.9+

TensorFlow / PyTorch – image classification

Transformers (Hugging Face) – recipe text generation

Flask / FastAPI – API & Web app

OpenCV / Pillow – image preprocessing

📊 Example
Input: 🍕 Image of a pizza

Output Recipe:

Ingredients: Flour, yeast, tomato sauce, mozzarella, olive oil, basil

Instructions:

Prepare dough with flour, yeast, and water.

Spread tomato sauce on dough.

Add mozzarella and toppings.

Bake at 220°C for 15 minutes.

Garnish with basil and serve.

✅ To-Do
 Add nutritional info per serving

 Multi-dish recognition from one image

 Support for multiple cuisines

 Deploy to Hugging Face Spaces / Streamlit

📜 License
MIT License – feel free to use and modify.


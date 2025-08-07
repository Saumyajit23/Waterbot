import google.generativeai as genai

genai.configure(api_key="AIzaSyBluAxc-GLOt1UmJKCYjP3u63dUIfudQXs")  # Replace with your API key

models = genai.list_models()

for model in models:
    print(model.name, "→", model.supported_generation_methods)

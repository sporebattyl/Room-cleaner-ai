import os
import google.generativeai as genai

def get_ai_response(image_path):
    """
    Analyzes an image with the Gemini AI and returns a list of messes.
    """
    try:
        api_key = os.environ.get("API_KEY")
        if not api_key:
            return ["Error: Gemini API key not found."]

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(os.environ.get("AI_MODEL", "gemini-2.5-pro"))

        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        prompt = os.environ.get("PROMPT", "Describe the state of the room and identify any items that are out of place.")

        response = model.generate_content([prompt, {"mime_type": "image/jpeg", "data": image_data}])

        # This is a mock response for now.
        # In a real implementation, you would parse the response from the AI.
        return ["dirty laundry on the floor", "unmade bed"]
    except Exception as e:
        return [f"Error analyzing image: {e}"]
import bashio

def analyze_image_with_ai(image_path: str) -> list[str]:
    """
    Analyzes an image using a mock AI service to identify messes.

    In a real implementation, this function would call the Gemini API.
    For now, it returns a static list of identified issues.

    Args:
        image_path: The path to the image file to be analyzed.

    Returns:
        A list of strings describing the identified messes.
    """
    api_key = bashio.config.get('api_key')
    if not api_key:
        bashio.log.warning("AI Service: API key is not configured. Using mock data.")
        # Fallback to mock data if API key is missing
    else:
        bashio.log.info(f"AI Service: Analyzing image {image_path} (mock call)")

    # Mock response
    mock_messes = [
        "dirty laundry on the floor",
        "unmade bed",
        "empty pizza box on the desk"
    ]
    return mock_messes
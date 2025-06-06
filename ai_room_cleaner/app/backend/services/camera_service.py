def get_placeholder_image() -> str:
    """
    Returns the path to a static placeholder image.

    In a real implementation, this service would interact with
    Home Assistant to get a live camera feed.

    Returns:
        The file path to the placeholder image.
    """
    # In the future, this could be a path to an image within the addon's assets
    return "/data/placeholder_room_image.jpg"
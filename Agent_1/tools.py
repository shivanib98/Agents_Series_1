def get_weather(city_name: str) -> dict:
    """Retrieves weather information for a given city.
    
    Args:
        city_name (str): The name of the city to retrieve weather information for.
    
    Returns:
        dict: A dictionary containing the weather information for the given city.
    """
    print(f"Retrieving weather information for {city_name}")
    city_normalized = city_name.lower().replace(" ", "")  # Basic normalization

    if city_normalized == "dublin":
        return {
            "weather": "Rainy"
        }
    else:
        return {
            "weather": "Information not available",
            "message": f"Weather data for {city_name} is not available in our database."
        }
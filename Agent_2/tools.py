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


def get_traffic_details(location: str) -> dict:
    """Retrieves traffic information for a given location.
    
    Args:
        location (str): The name of the location to retrieve traffic information for.
    
    Returns:
        dict: A dictionary containing the traffic information for the given location.
    """
    print(f"Retrieving traffic information for {location}")
    location_normalized = location.lower().replace(" ", "")  # Basic normalization

    if location_normalized == "dublin":
        return {
            "traffic_status": "Heavy",
            "congestion_level": "High",
            "average_speed": "15 km/h",
            "incidents": 3,
            "message": "Heavy traffic on M50 motorway due to rush hour."
        }
    elif location_normalized == "cork":
        return {
            "traffic_status": "Moderate",
            "congestion_level": "Medium",
            "average_speed": "35 km/h",
            "incidents": 1,
            "message": "Moderate traffic in city center."
        }
    else:
        return {
            "traffic_status": "Information not available",
            "message": f"Traffic data for {location} is not available in our database."
        }
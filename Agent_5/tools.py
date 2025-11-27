import json
from typing import Any, Dict, List


def parse_airbnb_json(json_string: str) -> Dict[str, Any]:
    """
    Parse and validate airbnb JSON response.
    
    Args:
        json_string: JSON string containing airbnb data
        
    Returns:
        Parsed and validated JSON object
        
    Raises:
        ValueError: If JSON is invalid or doesn't match expected format
    """
    try:
        data = json.loads(json_string)
        
        # Validate structure
        if "airbnbs" not in data:
            raise ValueError("Missing 'airbnbs' key in JSON")
        
        if not isinstance(data["airbnbs"], list):
            raise ValueError("'airbnbs' must be a list")
        
        # Validate each airbnb entry
        required_fields = ["name", "description", "reason", "price", "location"]
        for idx, airbnb in enumerate(data["airbnbs"]):
            for field in required_fields:
                if field not in airbnb:
                    raise ValueError(f"airbnb {idx} missing required field: {field}")
        
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {str(e)}")


def format_airbnb_airbnbs(airbnbs_data: Dict[str, Any]) -> str:
    """
    Format airbnb data into a readable string.
    
    Args:
        airbnbs_data: Dictionary containing airbnb 
        
    Returns:
        Formatted string representation of airbnbs
    """
    output = ["Top airbnb in Dublin:\n"]
    
    for idx, airbnb in enumerate(airbnbs_data.get("airbnbs", []), 1):
        output.append(f"\n{idx}. {airbnb.get('name', 'N/A')}")
        output.append(f"   Location: {airbnb.get('location', 'N/A')}")
        output.append(f"   Price: {airbnb.get('price', 'N/A')}")
        output.append(f"   Description: {airbnb.get('description', 'N/A')}")
        output.append(f"   airbnbing Because: {airbnb.get('reason', 'N/A')}")
    
    return "\n".join(output)


def validate_airbnb_analysis(analysis: str) -> bool:
    """
    Validate that airbnb analysis contains quantitative data.
    
    Args:
        analysis: Analysis text to validate
        
    Returns:
        True if analysis contains numbers/metrics, False otherwise
    """
    # Check for common quantitative indicators
    quantitative_indicators = [
        "review", "rating", "star", "score", "number", "percent", "%",
        "count", "total", "average", "median", "price", "$", "€"
    ]
    
    analysis_lower = analysis.lower()
    return any(indicator in analysis_lower for indicator in quantitative_indicators)


def extract_metrics(text: str) -> List[Dict[str, str]]:
    """
    Extract numerical metrics from analysis text.
    
    Args:
        text: Text containing metrics
        
    Returns:
        List of dictionaries containing metric name and value
    """
    import re
    
    metrics = []
    
    # Pattern to match numbers with context
    patterns = [
        r'(\d+(?:\.\d+)?)\s*(?:reviews?|ratings?|stars?)',
        r'(\d+(?:\.\d+)?)\s*(?:%|percent)',
        r'(?:€|£|\$)\s*(\d+(?:\.\d+)?)',
        r'(\d+(?:\.\d+)?)\s*(?:out of|/)\s*(\d+)',
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            metrics.append({
                "value": match.group(0),
                "context": text[max(0, match.start()-20):min(len(text), match.end()+20)]
            })
    
    return metrics

from deep_translator import GoogleTranslator


def english_to_hindi(text: str) -> str:
    """
    Translates English text to Hindi.
    
    Args:
        text: The English text to translate to Hindi.
        
    Returns:
        A string containing the Hindi translation.
    """
    # Simple translation mapping for common phrases
    translations = {
        "hello": "नमस्ते (namaste)",
        "goodbye": "अलविदा (alvida)",
        "thank you": "धन्यवाद (dhanyavaad)",
        "yes": "हाँ (haan)",
        "no": "नहीं (nahin)",
        "please": "कृपया (kripya)",
        "how are you": "आप कैसे हैं (aap kaise hain)",
        "good morning": "सुप्रभात (suprabhat)",
        "good night": "शुभ रात्रि (shubh ratri)",
    }
    
    # Convert to lowercase for matching
    text_lower = text.lower().strip()
    
    # Check if we have a direct translation
    if text_lower in translations:
        return f"Hindi translation: {translations[text_lower]}"
    
    # Use Google Translate API for other cases
    try:
        result = GoogleTranslator(source='en', target='hi').translate(text)
        return f"Hindi translation: {result}"
    except Exception as e:
        return f"Error translating to Hindi: {str(e)}"


def english_to_irish(text: str) -> str:
    """
    Translates English text to Irish (Gaeilge).
    
    Args:
        text: The English text to translate to Irish.
        
    Returns:
        A string containing the Irish translation.
    """
    # Simple translation mapping for common phrases
    translations = {
        "hello": "Dia dhuit",
        "goodbye": "Slán",
        "thank you": "Go raibh maith agat",
        "yes": "Tá",
        "no": "Níl",
        "please": "Le do thoil",
        "how are you": "Conas atá tú",
        "good morning": "Maidin mhaith",
        "good night": "Oíche mhaith",
    }
    
    # Convert to lowercase for matching
    text_lower = text.lower().strip()
    
    # Check if we have a direct translation
    if text_lower in translations:
        return f"Irish translation: {translations[text_lower]}"
    
    # Use Google Translate API for other cases
    try:
        result = GoogleTranslator(source='en', target='ga').translate(text)
        return f"Irish translation: {result}"
    except Exception as e:
        return f"Error translating to Irish: {str(e)}"
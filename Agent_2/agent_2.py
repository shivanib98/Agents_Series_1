from google.adk.agents import Agent

MODEL = "gemini-2.0-flash"

from .tools import get_weather
from .tools import get_traffic_details

root_agent = Agent(
    name="weather_traffic_agent",
    model=MODEL,
    description = "Provides weather and traffic information for specific cities.",
    instruction="""
    You are an expert **Weather and traffic Assistant**.
    
    When the user requests **weather information and traffic details** for a **specific city**,
    you must use the **'get_weather' and 'get_traffic_details' tool** to find relevant information.
    
    If the tool returns an error or no information is found, **inform the user politely** that you could not find any information or that there might be an issue.
    
    If the tool is successful and returns data, **present the weather and traffic information clearly**.
    """,
    tools=[get_weather,get_traffic_details], 
)
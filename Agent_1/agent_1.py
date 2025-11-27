from google.adk.agents import Agent

MODEL = "gemini-2.0-flash"

from .tools import get_weather

root_agent = Agent(
    name="weather_agent",
    model=MODEL,
    description = "Provides weather information for specific cities.",
    instruction="""
    You are an expert **Weather Assistant**.
    
    When the user requests **weather information** for a **specific city**,
    you must use the **'get_weather' tool** to find relevant information.
    
    If the tool returns an error or no information is found, **inform the user politely** that you could not find any information or that there might be an issue.
    
    If the tool is successful and returns data, **present the weather information clearly**.
    """,
    tools=[get_weather], 
)
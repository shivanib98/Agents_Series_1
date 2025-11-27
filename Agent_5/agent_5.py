# pylint: skip-file
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

MODEL = "gemini-2.5-pro"

# Create the Python Trending Topics ADK Agent
top_bnb_agent = Agent(
    model=MODEL,
    name="top_bnb_agent",
    instruction="""
    You are a airbnb trends analyst. 
    Your job is to search the web for currently listed airbnbs in dublin.

    When asked about trends:
    1. Search for famous airbnbs in dublin
    2. Extract the top 3 airbnbs
    3. Return them in a JSON format

    Focus on actual trends from the last 2 weeks.

    You MUST return your response in the following JSON format:
    {
        "trends": [
            {
                "topic": "airbnb name",
                "description": "Brief description (1-2 sentences)",
                "reason": "Why it's trending",
                "price": "price per night",
                "location": "location"  
            },
            {
                "topic": "airbnb name",
                "description": "Brief description (1-2 sentences)",
                "reason": "Why it's trending",
                "price": "price per night",
                "location": "location"
            },
            {
                "topic": "airbnb name",
                "description": "Brief description (1-2 sentences)",
                "reason": "Why it's trending",
                "price": "price per night",
                "location": "location"
            }
        ]
    }

    Only return the JSON object, no additional text.
    """,
    tools=[google_search],
)

# Create the Trend Analyzer ADK Agent
analyzer_agent = Agent(
    model="gemini-2.5-pro",
    name="trend_analyzer_agent",
    instruction="""
    You are a data analyst specializing in trend airbnbs. Perform deep research to find quantitative data and insights.

    For each airbnb analyze:
    1. Search for statistics, numbers, and metrics related to the airbnb
    2. Look for:
        - reviews
        - ratings
        - location
        - price
    3. Provide concrete numbers and data points

    Keep it somehow concise

    Always prioritize quantitative information over qualitative descriptions.
    """,
    tools=[google_search],
)

# Create the Host ADK Agent
root_agent = SequentialAgent(
    name="airbnb_host",
    sub_agents=[top_bnb_agent, analyzer_agent],
)

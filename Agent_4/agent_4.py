from google.adk.agents import Agent

MODEL = "gemini-2.0-flash"

from .tools import english_to_hindi, english_to_irish

language_agent_1 = Agent(
    model=MODEL,
    name="language_agent_1",
    instruction="You are the Language Agent. Your ONLY task is to translate the user's query to Hindi.",
        description="Handles simple language conversion to Hindi using the 'english_to_hindi' tool.", 
    tools=[english_to_hindi],
)

language_agent_2 = Agent(
    model=MODEL,
    name="language_agent_2",
    instruction="You are the Language Agent. Your ONLY task is to translate the user's query to Irish.",
    description="Handles simple language conversion to Irish using the 'english_to_irish' tool.", 
    tools=[english_to_irish],
)


root_agent = Agent(
    name="coordination_agent",
    model=MODEL,
    description="You are the Language Agent. Your primary responsibility is to provide language translation.",
    instruction="You are the main Language Agent coordinating a team. Your primary responsibility is to coordinate sub-agents."
    "You have specialized sub-agents: "
    "1. 'language_agent_1': Handles simple language conversion to Hindi. "
    "2. 'language_agent_2': Handles simple language conversion to Irish. "
    "Analyze the user's query. If it's a asking for hindi, delegate to 'language_agent_1'. If it's asking for irish, delegate to 'language_agent_2'. "
    "For anything else, respond appropriately or state you cannot handle it.",
    sub_agents=[language_agent_1, language_agent_2],
)
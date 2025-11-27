# Agent_1 - Weather Assistant

A simple AI agent built with Google ADK (Agent Development Kit) that demonstrates the power of tool-augmented agents.

## Project Architecture

```
Agent_1/
├── agent_1.py      # Main agent definition and configuration
├── tools.py        # Tool implementations (function calling)
├── __init__.py     # Package initialization
└── .env            # Environment configuration (API keys)
```

### Core Components

- **`agent_1.py`**: Defines the `weather_agent` using Google's ADK framework
  - Configures the agent with Gemini 2.0 Flash model
  - Provides system instructions for weather assistance
  - Registers available tools for the agent to use

- **`tools.py`**: Contains tool function implementations
  - `get_weather(city_name)`: Retrieves weather information for cities
  - Tools are standard Python functions with type hints and docstrings

## Significance of Tools in Agent Context

### Why Tools Matter

**Tools extend agent capabilities beyond language understanding.** While LLMs excel at natural language processing, they cannot directly access real-time data, APIs, or execute actions. Tools bridge this gap by:

1. **Grounding in Reality**: Tools connect agents to external data sources, APIs, and systems, enabling them to provide factual, up-to-date information rather than relying solely on training data.

2. **Action Execution**: Agents can perform concrete actions (API calls, database queries, file operations) rather than just generating text responses.

3. **Structured Interaction**: Tools define clear interfaces with typed parameters and return values, ensuring reliable agent-system communication.

4. **Composability**: Multiple tools can be combined, allowing agents to orchestrate complex workflows by chaining tool calls.

### How It Works

1. User asks: *"What's the weather in Dublin?"*
2. Agent analyzes the request and identifies the need to use `get_weather` tool
3. Agent calls `get_weather(city_name="Dublin")`
4. Tool executes and returns structured data
5. Agent synthesizes the tool output into a natural language response

This architecture makes agents **extensible** - adding new capabilities is as simple as defining new tool functions.

## Running the Agent

```bash
# Ensure ADK is installed
pip install google-adk

# Run the agent
adk run agent_1
```

## Environment Setup

Create a `.env` file with your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

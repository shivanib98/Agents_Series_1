# Agent_2 Project

A Google ADK agent that provides weather and traffic information using the Gemini 2.0 Flash model.

## Project Structure

```
Agent_2/
├── __init__.py          # Package initialization, exports root_agent
├── agent_2.py           # Main agent configuration
├── tools.py             # Weather and traffic tool functions
└── .env                 # Environment variables (API keys)
```

## Components

### `agent_2.py`
Main agent configuration using `gemini-2.0-flash` model. Defines the weather and traffic assistant with integrated tool functions.

### `tools.py`

#### `get_weather(city_name: str) -> dict`
Returns weather information for a city.

**Supported**: Dublin (Rainy), Others (Not available)

#### `get_traffic_details(location: str) -> dict`
Returns traffic information including status, congestion level, average speed, and incidents.

**Supported**: 
- Dublin: Heavy traffic, high congestion, 15 km/h, 3 incidents
- Cork: Moderate traffic, medium congestion, 35 km/h, 1 incident
- Others: Not available

## Getting Started

1. **Install Google ADK**:
   ```bash
   pip install google-adk
   ```

2. **Configure `.env`**:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

3. **Run the agent**:
   ```bash
   adk run agent_2
   ```

## Usage Examples

```
User: What's the weather like in Dublin?
Agent: The weather in Dublin is Rainy.

User: How's the traffic in Cork?
Agent: Moderate traffic with medium congestion. Average speed is 35 km/h with 1 incident.
```

## Customization

### Add New Cities
Edit `tools.py` to add more cities:

```python
if location_normalized == "london":
    return {
        "traffic_status": "Light",
        "congestion_level": "Low",
        "average_speed": "50 km/h",
        "incidents": 0
    }
```

### Integrate Real APIs
Replace mock data in tool functions with actual API calls and add credentials to `.env`.

## Notes

- Currently uses mock data
- Limited city coverage (Dublin, Cork)
- Built with Google ADK and Gemini 2.0 Flash

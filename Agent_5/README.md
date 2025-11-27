# Agent_5: Airbnb Trends Analysis System

## Overview

Agent_5 is a multi-agent system built using Google's ADK (Agent Development Kit) that analyzes trending Airbnb listings in Dublin. The system employs a sequential agent architecture where specialized sub-agents work together to gather, analyze, and present comprehensive insights about popular Airbnb properties.

### Components

#### 1. **Host Agent** (`host_agent`)
- **Type**: `SequentialAgent`
- **Role**: Orchestrator that coordinates the workflow between sub-agents
- **Execution Flow**: Runs sub-agents in sequence, passing context between them
- **Sub-agents**: `top_bnb_agent` → `analyzer_agent`

#### 2. **Top Airbnb Agent** (`top_bnb_agent`)
- **Type**: `Agent`
- **Model**: `gemini-2.5-pro`
- **Primary Responsibility**: Web research to identify trending Airbnb listings
- **Tools**: `google_search`
- **Output Format**: Structured JSON with top 3 trending Airbnbs

**Key Tasks:**
1. Search for currently listed and famous Airbnbs in Dublin
2. Extract the top 3 trending properties
3. Return structured data including:
   - Topic (Airbnb name)
   - Description
   - Reason for trending
   - Price per night
   - Location

#### 3. **Analyzer Agent** (`analyzer_agent`)
- **Type**: `Agent`
- **Model**: `gemini-2.5-pro`
- **Primary Responsibility**: Quantitative analysis of trending Airbnbs
- **Tools**: `google_search`
- **Focus**: Data-driven insights with concrete metrics

**Key Tasks:**
1. Research statistics and metrics for each Airbnb
2. Gather quantitative data:
   - Reviews count
   - Ratings (numerical scores)
   - Location details
   - Price analysis
3. Provide concrete numbers and data points

## Sequential Agent Pattern

The `SequentialAgent` pattern is crucial to this architecture:

### Why Sequential?

1. **Dependency Chain**: The analyzer needs the output from the top_bnb_agent to know which Airbnbs to analyze
2. **Context Preservation**: Results from the first agent automatically flow to the second
3. **Workflow Clarity**: Clear separation of concerns - discovery vs. analysis
4. **Efficiency**: No redundant searches; each agent focuses on its specialty

### Execution Flow

```
User Query
    ↓
host_agent receives request
    ↓
top_bnb_agent executes
    ├─ Searches for trending Airbnbs
    ├─ Identifies top 3 properties
    └─ Returns JSON with basic info
    ↓
analyzer_agent receives context
    ├─ Takes Airbnb names from previous output
    ├─ Performs deep quantitative research
    ├─ Gathers metrics and statistics
    └─ Returns detailed analysis
    ↓
Combined result returned to user
```

## Tools Module (`tools.py`)

The tools module provides utility functions to support the agent workflow:

### Available Functions

#### `parse_airbnb_json(json_string: str) -> Dict[str, Any]`
Validates and parses JSON output from the top_bnb_agent.
- Ensures required fields are present
- Validates data structure
- Raises descriptive errors for debugging

#### `format_airbnb_trends(trends_data: Dict[str, Any]) -> str`
Converts structured trend data into human-readable format.
- Creates formatted output for display
- Handles missing fields gracefully
- Organizes information hierarchically

#### `validate_trend_analysis(analysis: str) -> bool`
Checks if analysis contains quantitative data.
- Scans for numerical indicators
- Ensures data-driven insights
- Validates analyzer_agent output quality

#### `extract_metrics(text: str) -> List[Dict[str, str]]`
Extracts numerical metrics from text using regex patterns.
- Identifies reviews, ratings, prices
- Captures context around numbers
- Returns structured metric data

## Why Tools Matter in Agent Context

### 1. **Output Validation**
Agents can produce varying outputs. Tools ensure consistency and catch errors early.

### 2. **Data Transformation**
Raw agent outputs may need formatting for different use cases (display, storage, further processing).

### 3. **Quality Assurance**
Tools like `validate_trend_analysis()` ensure agents meet their objectives (e.g., providing quantitative data).

### 4. **Reusability**
Common operations are centralized, making the codebase maintainable and testable.

### 5. **Post-Processing**
Agents focus on core tasks while tools handle data manipulation and extraction.

## Configuration

### Model Selection
- **Model**: `gemini-2.5-pro`
- **Rationale**: Advanced reasoning capabilities for complex web research and data analysis

### Environment Variables
Create a `.env` file with:
```env
GOOGLE_API_KEY=your_api_key_here
```

## Usage Example

```python
from agent_5 import root_agent

# Query the agent system
response = root_agent.run("What are the trending Airbnbs in Dublin?")

# The system will:
# 1. Search for trending Airbnbs (top_bnb_agent)
# 2. Analyze them with metrics (analyzer_agent)
# 3. Return comprehensive insights
```

## Key Design Principles

### 1. **Separation of Concerns**
Each agent has a single, well-defined responsibility:
- Discovery vs. Analysis
- Breadth vs. Depth

### 2. **Structured Output**
Enforced JSON schema ensures predictable, parseable results.

### 3. **Quantitative Focus**
Emphasis on data-driven insights over qualitative descriptions.

### 4. **Tool-Augmented Agents**
Both agents use `google_search` to access real-time information.

### 5. **Composability**
Sequential architecture allows easy addition of more agents in the pipeline.

## Benefits of This Architecture

✅ **Modularity**: Easy to modify or replace individual agents  
✅ **Scalability**: Can add more specialized agents to the sequence  
✅ **Maintainability**: Clear separation makes debugging straightforward  
✅ **Testability**: Each agent can be tested independently  
✅ **Reliability**: Structured outputs and validation reduce errors  

## Future Enhancements

- Add caching layer for frequently searched Airbnbs
- Implement parallel analysis for multiple cities
- Add sentiment analysis agent for review processing
- Create visualization agent for trend charts
- Integrate with Airbnb API for real-time data

## File Structure

```
Agent_5/
├── agent_5.py          # Main agent definitions
├── tools.py            # Utility functions for data processing
├── __init__.py         # Package initialization
├── .env                # Environment variables (API keys)
└── README.md           # This file
```

## Dependencies

- `google.adk.agents` - Agent and SequentialAgent classes
- `google.adk.tools` - Built-in tools (google_search)
- Python 3.8+

---

**Note**: This architecture demonstrates the power of multi-agent systems where specialized agents collaborate to solve complex tasks that would be difficult for a single agent to handle effectively.

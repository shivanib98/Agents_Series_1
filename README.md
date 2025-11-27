# Agents Series 1: Building AI Agents with Google ADK

A collection of AI agent projects showcasing progressive complexity in agent architectures, from simple tool-augmented assistants to sophisticated multi-agent systems built with Google's Agent Development Kit (ADK).

## 🎯 Project Overview

This repository contains **5 distinct agent implementations** demonstrating various architectural patterns and real-world applications. Each project explores different aspects of agent design, from basic function calling to complex hierarchical and sequential multi-agent systems.

## 📂 Project Structure

```
Agents_Series_1/
├── .env                    # Shared API configuration
├── Agent_1/              # Basic weather assistant
├── Agent_2/              # Multi-tool agent (weather + traffic)
├── Agent_3/              # Google Search & Maps integration
├── Agent_4/              # Multi-agent translation system
├── Agent_5/              # Sequential agent workflow
└── README.md               # This file
```

---

## 🚀 Projects

### [Agent 1: Weather Assistant](./Agent_1)
**Type**: Tool-Augmented Agent  
**Model**: Gemini 2.0 Flash

A weather information assistant demonstrating fundamental tool integration with AI agents. The agent uses custom function calling to retrieve weather data for cities.

**Features:**
- Custom `get_weather` tool implementation
- Natural language weather queries
- Structured data retrieval and response generation

**Example:** *"What's the weather in Dublin?"*

---

### [Agent 2: Multi-Tool Assistant](./Agent_2)
**Type**: Multi-Tool Agent  
**Model**: Gemini 2.0 Flash

An enhanced assistant that handles both weather and traffic information queries. Demonstrates intelligent tool selection based on user intent.

**Features:**
- Dual tool integration (weather + traffic)
- Context-aware tool routing
- Mock data implementation for rapid prototyping

**Example:** *"How's the traffic in Liverpool and what's the weather like?"*

---

### [Agent 3: Social Event Planner](./Agent_3)
**Type**: External API Integration  
**Model**: Gemini 2.0 Flash Experimental

A sophisticated event discovery and travel planning agent leveraging Google Search and Google Maps APIs for real-time information.

**Features:**
- Google Search integration for event discovery
- Google Maps grounding for route optimization
- Multi-modal transportation support (driving, walking, transit)
- Real-time traffic consideration
- Multi-stop itinerary planning

**Example:** *"Find social events in San Francisco this weekend and give me directions from downtown"*

---

### [Agent 4: Multi-Agent Translation System](./Agent_4)
**Type**: Hierarchical Multi-Agent System  
**Model**: Gemini 2.0 Flash

A translation system implementing hierarchical agent architecture with intelligent delegation. Features a coordination agent that routes requests to specialized language agents.

**Features:**
- Hierarchical architecture (1 coordinator + 2 specialists)
- English-to-Hindi and English-to-Irish translation
- Hybrid tool design with local dictionary caching + API fallback
- Performance optimization through intelligent caching
- Scalable architecture for adding new languages

**Architecture:**
```
root_agent (Coordinator)
  ├── language_agent_1 (Hindi Translation)
  └── language_agent_2 (Irish Translation)
```

**Example:** *"Translate 'hello' to Hindi"* → Automatically routes to Hindi specialist

---

### [Agent 5: Airbnb Trends Analyzer](./Agent_5)
**Type**: Sequential Multi-Agent System  
**Model**: Gemini 2.5 Pro

An advanced analytics system using sequential agent workflow to discover and analyze trending Airbnb listings. Implements a two-stage pipeline where agents pass context between stages.

**Features:**
- Sequential agent orchestration with context passing
- Two-stage pipeline: Discovery → Quantitative Analysis
- Structured JSON output with validation
- Comprehensive data extraction (reviews, ratings, pricing)
- Custom utility tools for data processing

**Architecture:**
```
host_agent (SequentialAgent)
  ├── top_bnb_agent → Discovers trending listings
  └── analyzer_agent → Analyzes metrics and statistics
```

**Example:** *"What are the trending Airbnbs in Dublin?"* → Discovers properties, then performs deep analysis



## 🏗️ Technical Highlights

### Architecture Patterns Implemented

#### 1. **Single Agent with Tools** (Agents 1, 2, 3)
- Direct tool integration for focused functionality
- Efficient for single-domain applications
- Clean, maintainable architecture

#### 2. **Hierarchical Multi-Agent** (Agent 4)
- Root coordinator with specialized sub-agents
- Request routing based on domain expertise
- Scalable for multi-domain applications

#### 3. **Sequential Multi-Agent** (Agent 5)
- Pipeline-based workflow with context passing
- Stage-specific specialization
- Ideal for complex, multi-step processes

### Design Decisions

**Tool Design Philosophy** (Agent 4)
- Hybrid approach: Local caching + API fallback
- 60-80% reduction in API calls for common queries
- Sub-millisecond response for cached items
- Graceful degradation when APIs unavailable

**Sequential Workflow** (Agent 5)
- Context preservation between pipeline stages
- Structured JSON output with validation
- Specialized agents for discovery vs. analysis
- Comprehensive data extraction utilities

---

## 🧠 Model Selection Rationale

### Gemini 2.0 Flash (Agents 1 - 4)

**Why Flash for most agents:**
- **Speed**: Optimized for low-latency responses, ideal for interactive applications
- **Cost-Effective**: Lower operational costs for high-frequency tool calling
- **Sufficient Capability**: More than adequate for structured tool selection and delegation
- **Tool Calling Optimization**: Specifically tuned for function calling patterns

**Use Cases:**
- Simple tool integration (weather, traffic queries)
- Multi-tool selection and routing
- Hierarchical agent coordination
- API integration with external services

### Gemini 2.5 Pro (Agent 5)

**Why Pro for the Airbnb analyzer:**
- **Advanced Reasoning**: Complex web research requiring deeper analysis
- **Structured Output**: Better at generating and maintaining JSON schemas
- **Multi-Step Workflows**: Superior performance in sequential agent pipelines
- **Data Extraction**: Enhanced capability for extracting quantitative metrics from unstructured web content
- **Context Management**: Better handling of context passing between pipeline stages

**Specific Requirements:**
- Discovering trending properties from diverse sources
- Analyzing multiple data points (reviews, ratings, pricing)
- Maintaining structured output format across pipeline stages
- Extracting concrete metrics from qualitative descriptions

### Model Comparison

| Model | Latency | Cost | Best For |
|-------|---------|------|----------|
| Gemini 2.0 Flash | Low | Lower | Tool calling, routing, simple queries |
| Gemini 2.5 Pro | Medium | Higher | Complex reasoning, structured output, analytics |

**Design Philosophy**: Use the most efficient model that meets the task requirements. Flash handles 80% of use cases; Pro is reserved for complex analytical workflows.

---

## 🛠️ Tech Stack

- **Framework**: Google Agent Development Kit (ADK)
- **Models**: Gemini 2.0 Flash, Gemini 2.5 Pro
- **APIs**: Google Search, Google Maps, Google Translate
- **Tools**: Custom functions, `deep-translator`
- **Language**: Python 3.8+

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- Google API Key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

```bash
# Install Google ADK
pip install google-adk

# Install additional dependencies
pip install deep-translator
```

### Configuration

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## 🎮 Running the Agents

Each agent can be run independently:

```bash
# CLI interface
adk run <agent_name>

# Web interface
adk web <agent_name>
```

**Examples:**
```bash
adk run agent_1    # Weather assistant
adk run agent_4    # Translation system
adk run agent_5    # Airbnb analyzer
```

Access web interface at: `http://127.0.0.1:8000`

---

## 📊 Project Progression

| Project | Architecture Type | Key Innovation |
|---------|------------------|----------------|
| Agent 1 | Single Agent | Tool integration fundamentals |
| Agent 2 | Single Agent | Multi-tool selection |
| Agent 3 | Single Agent | External API integration |
| Agent 4 | Hierarchical Multi-Agent | Intelligent delegation + caching |
| Agent 5 | Sequential Multi-Agent | Pipeline workflow + structured output |

---

## 🎯 Key Features

### Performance Optimization
- **Local caching** for frequently accessed data (Agent 4)
- **Hybrid tool design** reducing API calls by 60-80%
- **Structured output** with validation for reliability

### Scalability
- **Modular architecture** allowing easy extension
- **Specialized agents** for domain-specific tasks
- **Clear separation of concerns** across components

### Real-World Integration
- Google Search for event discovery
- Google Maps for route optimization
- Translation APIs with fallback mechanisms

---

## 🔧 Implementation Details

### Tool Design Best Practices
- Type hints and comprehensive docstrings
- Error handling with meaningful messages
- Validation functions for output quality
- Graceful degradation strategies

### Agent Orchestration
- Clear instruction sets for agent behavior
- Context passing in sequential workflows
- Intelligent routing in hierarchical systems
- Structured JSON for inter-agent communication




## 🚀 Potential Extensions

### Agent Enhancements
- **Agent 1**: Integration with real-time weather APIs (OpenWeatherMap, WeatherAPI)
- **Agent 2**: Public transit data and ride-sharing integration
- **Agent 3**: Calendar sync, ticket purchasing, and group coordination
- **Agent 4**: Expanded language support, translation memory, context-aware translations
- **Agent 5**: Multi-city analysis, sentiment analysis, price trend visualization

### System-Wide Improvements
- Persistent storage for agent interactions
- User authentication and personalization
- Rate limiting and caching layers
- Monitoring and analytics dashboard
- API gateway for external integrations

---

## 📁 Repository Structure

Each agent is self-contained with its own README, tools, and configuration:

```
Agent_X/
├── agent_X.py          # Agent definition and configuration
├── tools.py            # Custom tool implementations (if applicable)
├── __init__.py         # Package initialization
└── README.md           # Detailed project documentation
```

---

## 🔗 Resources

- [Google ADK Documentation](https://developers.google.com/adk)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Agent Design Patterns](https://developers.google.com/adk/patterns)

---

**Built with Google Agent Development Kit (ADK)**  
*November 2025*


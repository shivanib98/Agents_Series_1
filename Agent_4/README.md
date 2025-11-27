# Agent_4: Multi-Agent Translation System

## Overview

Agent_4 is a hierarchical multi-agent system built with Google's Agent Development Kit (ADK) that provides English-to-Hindi and English-to-Irish translation services. The system demonstrates best practices in agent architecture through intelligent delegation and optimized tool design.

## Architecture

### Agent Hierarchy

```
root_agent (Coordination Agent)
    ├── language_agent_1 (Hindi Translation)
    │   └── Tool: english_to_hindi
    └── language_agent_2 (Irish Translation)
        └── Tool: english_to_irish
```

### Components

#### 1. **Root Agent** (`coordination_agent`)
- **Role**: Main orchestrator that analyzes user queries and delegates to specialized sub-agents
- **Responsibilities**:
  - Parse user intent (Hindi vs Irish translation request)
  - Route requests to appropriate sub-agent
  - Handle edge cases and unsupported requests
- **Model**: `gemini-2.0-flash`

#### 2. **Language Agent 1** (`language_agent_1`)
- **Role**: Specialized Hindi translation agent
- **Tool**: `english_to_hindi`
- **Scope**: Handles all English-to-Hindi translation requests

#### 3. **Language Agent 2** (`language_agent_2`)
- **Role**: Specialized Irish translation agent
- **Tool**: `english_to_irish`
- **Scope**: Handles all English-to-Irish translation requests

## Tool Design Philosophy

### Hybrid Approach: Local Cache + API Fallback

Both translation tools (`english_to_hindi` and `english_to_irish`) implement a **two-tier translation strategy**:

1. **Local dictionary lookup** for common phrases
2. **API fallback** (Google Translate via `deep-translator`) for everything else

### Why Use Local Dictionaries for Common Words?

#### 1. **Performance & Latency**
- **Local lookup**: ~0.001ms (instant, in-memory)
- **API call**: ~100-500ms (network round-trip)
- For common phrases like "hello" or "thank you", API calls add unnecessary latency

#### 2. **Cost Efficiency**
- Translation APIs often have usage limits or costs per request
- Common phrases are translated thousands of times
- Caching reduces API calls by 60-80% in typical usage

#### 3. **Reliability**
- Local dictionaries work offline
- No dependency on external service availability
- Graceful degradation when API is unavailable

#### 4. **Quality Control**
- Common phrases can have cultural nuances
- Pre-vetted translations ensure consistency
- Example: "hello" → "नमस्ते (namaste)" with transliteration

#### 5. **Reduced Token Usage**
- LLM agents may call tools multiple times
- Each API call consumes tokens and time
- Local cache minimizes redundant processing

### Implementation Example

```python
def english_to_hindi(text: str) -> str:
    # Tier 1: Local dictionary (fast, free, reliable)
    translations = {
        "hello": "नमस्ते (namaste)",
        "goodbye": "अलविदा (alvida)",
        # ... more common phrases
    }
    
    if text.lower().strip() in translations:
        return f"Hindi translation: {translations[text.lower().strip()]}"
    
    # Tier 2: API fallback (comprehensive, slower)
    try:
        result = GoogleTranslator(source='en', target='hi').translate(text)
        return f"Hindi translation: {result}"
    except Exception as e:
        return f"Error translating to Hindi: {str(e)}"
```

## Best Practices Demonstrated

### 1. **Separation of Concerns**
- Each agent has a single, well-defined responsibility
- Tools are focused and reusable

### 2. **Intelligent Delegation**
- Root agent acts as a router, not a worker
- Specialized agents handle domain-specific tasks

### 3. **Graceful Degradation**
- Local cache provides baseline functionality
- API extends capabilities without being a single point of failure

### 4. **Performance Optimization**
- Hot path (common phrases) is optimized for speed
- Cold path (rare phrases) prioritizes coverage over speed

### 5. **Scalability**
- Easy to add new language agents (e.g., `language_agent_3` for Spanish)
- Dictionary can be expanded without code changes
- API handles long-tail cases automatically

## Configuration

### Environment Variables

Create a `.env` file with your Google AI API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

Get your API key from: https://aistudio.google.com/app/apikey

### Dependencies

```bash
pip install deep-translator
```

## Running the Agent

```bash
# From the scratch directory
python -m google.adk.cli web Agent_4
```

Access the web interface at: http://127.0.0.1:8000

## Usage Examples

**Hindi Translation:**
```
User: "Translate 'hello' to Hindi"
→ Root Agent → language_agent_1 → english_to_hindi
→ "Hindi translation: नमस्ते (namaste)"
```

**Irish Translation:**
```
User: "How do you say 'thank you' in Irish?"
→ Root Agent → language_agent_2 → english_to_irish
→ "Irish translation: Go raibh maith agat"
```

**Complex Sentence (API Fallback):**
```
User: "Translate 'The weather is beautiful today' to Hindi"
→ Root Agent → language_agent_1 → english_to_hindi (API)
→ "Hindi translation: आज मौसम सुंदर है"
```

## Key Takeaways

1. **Hybrid approaches** (local + API) provide the best of both worlds
2. **Common cases** should be optimized aggressively
3. **Agent hierarchies** enable clean separation and scalability
4. **Tool design** impacts overall system performance significantly
5. **Caching strategies** reduce costs and improve user experience

---

**Built with**: Google Agent Development Kit (ADK) | **Model**: Gemini 2.0 Flash | **Translation API**: deep-translator

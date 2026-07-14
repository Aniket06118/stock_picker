# StockPicker

An AI-powered stock investment recommendation system built with **CrewAI** that analyzes trending companies and selects the best investment opportunities.

## 🎯 Overview

StockPicker is a multi-agent AI system that automates stock research and investment recommendations. It uses a collaborative team of AI agents to:

1. **Discover Trending Companies** — Scans financial news to identify companies gaining market attention in a specified sector
2. **Conduct Financial Research** — Performs deep analysis on each trending company, evaluating market position, competitive landscape, and future prospects
3. **Select Investment Winner** — Synthesizes research findings to recommend the single best company for investment and explains why competitors were rejected

The system employs a hierarchical crew architecture where a manager agent orchestrates the workflow, ensuring seamless coordination between specialized agents.

### Key Workflow

```
Trending Company Finder (searches news)
         ↓
Financial Researcher (analyzes each company)
         ↓
Stock Picker (makes final recommendation)
         ↓
Manager Agent (oversees entire process)
```

## 🛠 Core Technologies

- **[CrewAI](https://crewai.com)** (v1.14.7) — Multi-agent AI orchestration framework
  - Hierarchical process management for agent coordination
  - Structured Pydantic output validation
  - Built-in tool integration
  
- **LLM Providers** — Multi-model approach for optimal cost/performance:
  - **Google Gemini** — Fast, efficient models (gemini-2.5-flash-lite for news analysis)
  - **Groq Llama** — High-performance models (llama-3.3-70b for deep analysis)
  
- **[SerperDev](https://serper.dev)** — Web search tool for fetching real-time financial news and company data

- **[Pydantic](https://docs.pydantic.dev)** (v2.12.5+) — Data validation using Python type hints
  - Structured output contracts for each agent task
  - Type-safe research data and investment decisions

- **[LiteLLM](https://litellm.ai)** (v1.89.2+) — LLM provider abstraction layer
  - Unified interface across multiple model vendors
  - Error handling and retry logic

- **Python** (3.10 - 3.13) — Project foundation
  - Modern async/await patterns
  - Type hint support

## 🚀 Quick Start

### Prerequisites

Ensure you have Python 3.10 or higher installed:

```bash
python --version  # Verify Python version
pip install uv    # Install UV package manager
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aniket06118/stock_picker.git
   cd stock_picker
   ```

2. **Install dependencies using UV:**
   ```bash
   uv sync
   ```

3. **Set up API keys** — Create a `.env` file in the project root with your API credentials:
   ```env
   OPENAI_API_KEY=your_openai_key        # For OpenAI models (if used)
   SERPER_API_KEY=your_serper_key        # For web search (required)
   GOOGLE_API_KEY=your_google_key        # For Gemini models (required)
   GROQ_API_KEY=your_groq_key            # For Groq models (required)
   ```

### Running the System

Execute the crew with a default investment sector:

```bash
crewai run
```

Or run directly using Python:

```bash
python -m stock_picker.main
```

This command:
- Initializes the StockPicker crew with the "Technology" sector
- Engages all three agents in sequence (with manager orchestration)
- Produces three output files in the `output/` directory:
  - `trending_companies.json` — List of 2-3 trending companies identified
  - `research_report.json` — Comprehensive financial analysis of each company
  - `decision.md` — Final investment recommendation with rationale

## 📊 Example Output

Here's what a typical investment decision looks like:

**Selected Company:** ASML Holding

**Why ASML was chosen:**
- ASML Holding is a key supplier to the semiconductor industry, benefiting from strong and increasing demand for advanced chip-making tools, particularly driven by AI advancements.
- Exhibits robust market position, competitive edge, and optimistic future projections.
- Strong financial fundamentals with consistent earnings and revenue growth expected.
- Demand for advanced chip-making tools projected to continue upward trajectory due to AI expansion.

**Companies rejected and why:**
- **SpaceX** — While attractive with significant growth potential, was not selected (undisclosed reasons noted in full report)
- **Intel** — Strong AI chip market contender, but operates in highly competitive landscape with intense rivalry from established competitors

Full output example available in `output/decision.md`.

## 🔧 Configuration

Customize the system by modifying configuration files:

### Agent Configuration (`src/stock_picker/config/agents.yaml`)

Define agent roles, goals, and LLM models:

```yaml
trending_company_finder:
  role: Financial News Analyst that finds trending companies in {sector}
  goal: Find 2-3 trending companies for further research
  llm: gemini-2.5-flash-lite

stock_picker:
  role: Stock Picker from Research
  goal: Select the best company for investment
  llm: groq/llama-3.3-70b-versatile
```

### Task Configuration (`src/stock_picker/config/tasks.yaml`)

Define agent tasks, descriptions, and output formats:

```yaml
pick_best_company:
  description: Analyze research findings and pick the best company
  expected_output: The chosen company and why it was chosen
  agent: stock_picker
  output_file: output/decision.md
```

### Custom Tools

Extend functionality by adding custom tools in `src/stock_picker/tools/custom_tool.py`. The system currently uses:
- **SerperDevTool** — Web search for trending companies and financial data
- Custom tools can be added for specialized analysis

## 📁 Project Structure

```
stock_picker/
├── src/stock_picker/
│   ├── crew.py                 # Main crew definition with agents and tasks
│   ├── main.py                 # Entry point with run/train/test commands
│   ├── config/
│   │   ├── agents.yaml         # Agent configurations
│   │   └── tasks.yaml          # Task configurations
│   └── tools/
│       └── custom_tool.py      # Custom tool templates
├── output/                      # Generated output files
│   ├── trending_companies.json
│   ├── research_report.json
│   └── decision.md
├── pyproject.toml              # Project metadata and dependencies
├── AGENTS.md                   # CrewAI reference guide
└── README.md                   # This file
```

## 🎓 Key Concepts

### Hierarchical Process

The crew uses a **hierarchical process** where:
- A manager agent coordinates task execution
- Agents complete tasks sequentially with context from previous results
- Task dependencies ensure proper information flow

### Structured Outputs

All agent outputs are validated against Pydantic models:
- `Trending_company_list` — Standardized trending company discovery
- `TrendingCompanyResearchList` — Comprehensive research structure
- Investment decisions are structured for consistency

### Multi-Model Architecture

The system strategically uses different LLMs:
- **Fast models** (Gemini Flash) for initial data gathering
- **Powerful models** (Llama 70B) for deep financial analysis
- **Balanced models** (Gemini) for management/orchestration

This approach optimizes cost while maintaining quality.

## ⚙️ Advanced Usage

### Train the Crew

Fine-tune agent performance over multiple iterations:

```bash
python -m stock_picker.main train 5 training.json
```

### Test Crew Execution

Validate crew performance using an evaluation model:

```bash
python -m stock_picker.main test 2 gpt-4o
```

### Replay from Specific Task

Re-execute from a particular task using its ID:

```bash
python -m stock_picker.main replay <task_id>
```

### Run with Custom Payload

Trigger the crew with a JSON payload:

```bash
python -m stock_picker.main run_with_trigger '{"sector": "Healthcare"}'
```

## 📝 API Keys & Services

| Service | Purpose | Setup |
|---------|---------|-------|
| **Serper API** | Web search for financial news | [Get Key](https://serper.dev) |
| **Google Gemini** | Fast LLM inference | [Get Key](https://ai.google.dev) |
| **Groq** | High-performance LLM inference | [Get Key](https://groq.com) |

## 🧪 Development

### Running with Verbose Output

The crew runs in verbose mode by default, showing:
- Agent thoughts and reasoning
- Tool invocations and results
- Task progress and context passing

### Debugging

Check the generated output files for detailed analysis:
- `output/trending_companies.json` — Structured list of companies
- `output/research_report.json` — Detailed research findings
- `output/decision.md` — Final investment decision with explanations

## 🤝 Extending the System

### Add a New Agent

1. Add agent definition to `agents.yaml`
2. Create agent method with `@agent` decorator in `crew.py`
3. Define associated task in `tasks.yaml`
4. Create task method with `@task` decorator in `crew.py`

### Create Custom Analysis Tools

Extend `custom_tool.py` to add specialized analysis capabilities:
```python
class FinancialMetricsTool(BaseTool):
    name: str = "Calculate Financial Metrics"
    description: str = "Computes P/E ratio, debt-to-equity, and other metrics"
    
    def _run(self, ticker: str) -> str:
        # Your implementation
        pass
```

## 📚 Resources

- **[CrewAI Documentation](https://docs.crewai.com)** — Complete framework documentation
- **[Pydantic Docs](https://docs.pydantic.dev)** — Data validation reference
- **[SerperDev Docs](https://serper.dev/docs)** — Web search API reference
- **[LiteLLM Docs](https://litellm.ai/docs)** — Multi-model LLM provider guide

## ⚠️ Important Notes

- **API Costs** — This system makes real API calls to multiple services. Monitor your usage to avoid unexpected charges.
- **Rate Limits** — Serper, Gemini, and Groq have rate limits; adjust task complexity if hitting limits.
- **Freshness** — Investment recommendations are based on current news/data; use this as one input among many.

## 📧 Support

For issues, questions, or contributions:
- **GitHub Issues**: [stock_picker/issues](https://github.com/Aniket06118/stock_picker/issues)
- **CrewAI Support**: [crewai.com](https://crewai.com)
- **CrewAI Discord**: [Join Community](https://discord.com/invite/X4JWnZnxPb)

---

**Happy investing! 📈**

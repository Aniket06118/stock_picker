# 📈 StockPicker

An autonomous **multi-agent stock research system** built with **CrewAI** that discovers trending companies, performs in-depth financial analysis, and recommends the strongest investment opportunity within a chosen sector.

Instead of relying on a single LLM, StockPicker leverages a team of specialized AI agents working together under a manager agent to automate the complete stock research workflow.

---

## ✨ Features

- 🔍 Finds trending companies using real-time financial news
- 📊 Performs detailed research on each shortlisted company
- 🤖 Uses multiple AI agents with specialized responsibilities
- 🏆 Selects the strongest investment opportunity with clear reasoning
- 📄 Produces structured research reports and investment decisions
- ⚡ Uses different LLMs for speed, reasoning, and cost optimization

---

## 🏗 Architecture

The system follows a **hierarchical multi-agent architecture**, where a manager agent coordinates specialized agents throughout the research pipeline.

```text
                     Manager Agent
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
Trending Company     Financial Research     Stock Picker
     Finder               Agent                 Agent
        │                  │                  │
        └──────────────► Context ◄────────────┘
                           │
                           ▼
              Final Investment Recommendation
```

### Agent Responsibilities

### 🔍 Trending Company Finder

- Searches real-time financial news
- Identifies companies receiving significant market attention
- Shortlists promising candidates for research

### 📊 Financial Research Agent

- Performs detailed research on every shortlisted company
- Evaluates market position, competition, financial outlook, and future growth
- Produces structured research reports

### 🏆 Stock Picker

- Compares research across all companies
- Evaluates strengths and weaknesses
- Selects the single best investment opportunity
- Explains why other companies were rejected

### 🎯 Manager Agent

- Coordinates the entire workflow
- Maintains context between agents
- Ensures tasks execute in the correct sequence

---

## 🛠 Tech Stack

### CrewAI

The core multi-agent framework used to orchestrate the workflow. A hierarchical manager agent coordinates specialized agents responsible for discovery, research, and decision-making.

### Google Gemini

Used for fast information gathering and news analysis. Its low latency makes it ideal for identifying trending companies.

### Groq (Llama 3.3 70B)

Used for deep financial reasoning and investment analysis where stronger reasoning capabilities are required.

### Serper API

Provides real-time web search for financial news, company updates, and market information.

### LiteLLM

Provides a unified interface for multiple LLM providers, allowing seamless integration of Gemini and Groq models.

### Pydantic

Ensures structured and validated outputs between agents, making the workflow reliable and consistent.

### Python

Primary language used to build the agent workflow, tools, and application logic.

---

## 📁 Project Structure

```text
stock_picker/
│
├── src/
│   └── stock_picker/
│       ├── crew.py
│       ├── main.py
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── tools/
│
├── output/
│   ├── trending_companies.json
│   ├── research_report.json
│   └── decision.md
│
├── pyproject.toml
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Aniket06118/stock_picker.git

cd stock_picker
```

Install dependencies:

```bash
uv sync
```

Create a `.env` file:

```env
SERPER_API_KEY=your_serper_key
GOOGLE_API_KEY=your_google_key
GROQ_API_KEY=your_groq_key
```

---

## ▶️ Running the Project

Run the CrewAI workflow:

```bash
crewai run
```

or

```bash
python -m stock_picker.main
```

The system will:

1. Find trending companies in the selected sector
2. Research each company
3. Select the strongest investment
4. Generate structured output files

---

## 📊 Example Output

The workflow generates the following files:

```text
output/
├── trending_companies.json
├── research_report.json
└── decision.md
```

Example recommendation:

```text
Selected Company: ASML Holding

Reason:
• Dominant position in semiconductor manufacturing
• Strong long-term AI-driven demand
• Excellent competitive advantage
• Strong future growth outlook
```

---

## 🔮 Future Improvements

- Historical stock price analysis
- Financial ratio evaluation
- Risk assessment module
- Portfolio optimization
- Support for multiple investment strategies
- Integration with stock market APIs
- Interactive dashboard

---

## 📚 Resources

- CrewAI
- Google Gemini
- Groq
- LiteLLM
- Serper API
- Pydantic

---


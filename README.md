# AI Research Agent

A multi-agent AI research assistant: give it any topic and it researches the web for you —
gathering facts with tools, analyzing them, scoring their quality, and writing up a
structured research report with sources.

## How it works

The system runs a 4-phase pipeline of specialized agents:

1. 🔍 **Research Agent** — a LangChain tool-calling agent that searches the web and Wikipedia
   for the topic, gathering facts with source attribution
2. 🧠 **Analysis Agent** — finds patterns, key themes, and gaps in the research
3. ✅ **QA Agent** — scores the research for completeness and accuracy, and flags issues
4. 📝 **Synthesis Agent** — writes the final report (summary, full explanation, sources,
   tools used, quality metrics) as structured JSON

## Tools the agent can use

- **Wikipedia** (`WikipediaQueryRun`) — encyclopedic background on any topic
- **DuckDuckGo web search** — current, real-world information from the web

No paid APIs are needed for the tools — only a free Google Gemini API key for the model.

## Tech stack

- Python 3.11+
- LangChain (`langchain`, `langchain-classic`, `langchain-community`, `langchain-google-genai`)
- Google Gemini (`gemini-2.5-flash`)
- DuckDuckGo search (`duckduckgo-search` / `ddgs`), Wikipedia (`wikipedia`)
- Pydantic — structured output schemas for the final report

## Run it

1. Make sure you have Python installed: `python --version`
2. Clone this repo: `git clone https://github.com/HuzaifaAqeel/AI-Research-Agent.git`
3. Install the dependencies: `pip install -r requirements.txt`
4. Get a free Gemini API key at https://aistudio.google.com/apikey
5. Rename `.env.example` to `.env` and put your key in `GEMINI_API_KEY`
6. Run it: `python main.py` — then type a research topic when asked

## Example

```
What would you like to research about today?: What is the capital of Australia and when was it founded?

🚀 Starting Multi-Agent Research System for: 'What is the capital of Australia and when was it founded?'
============================================================
🔍 Phase 1: Research Agent gathering information ...
🧠 Phase 2: Analysis Agent processing findings
✅ Phase 3: QA Agent reviewing research quality
📝 Phase 4: Synthesis Agent creating final report
============================================================
✨ Multi-Agent Research Complete!

FINAL RESEARCH REPORT
{
  "topic": "What is the capital of Australia and when was it founded?",
  "summary": "The capital of Australia is Canberra, founded (formally named) in 1913.",
  "full_explanation": "...",
  "sources": ["https://en.wikipedia.org/wiki/Canberra", "..."],
  "tools_used": ["search_tool", "wiki_tool"],
  "quality_metrics": { "completeness_score": ..., "accuracy_score": ..., ... }
}
```

## Credits

Based on the open-source project **[ResearchAgent](https://github.com/ableflyer/ResearchAgent)**
by **[ableflyer](https://github.com/ableflyer)**, released under the
**Apache License 2.0** (see `LICENSE`).

Extended and maintained by **Muhammad Huzaifa Aqeel** ([HuzaifaAqeel](https://github.com/HuzaifaAqeel)):
model updated to `gemini-2.5-flash`, migrated to the current LangChain agent API
(`langchain-classic`), added a Wikipedia user-agent and retry handling so the tools
survive transient network failures, and improved tool error handling.

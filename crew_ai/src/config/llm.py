from crewai import LLM

# ---- LLM Configuration ----
ollama_flag = False
if ollama_flag:
    llm = LLM(
        model="ollama/llama3.2:1b",
        base_url="http://localhost:11434",
        temperature=0.7
    )
else:
    llm = LLM(
        model="mistral/mistral-large-latest",
        temperature=0.7
    )

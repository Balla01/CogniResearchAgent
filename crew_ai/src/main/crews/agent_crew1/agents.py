from crewai import Agent
from src.main.crews.agent_crew1.config.llm import llm
from src.main.crews.agent_crew1.tools import google_search, analyze_stock
import mlflow
mlflow.crewai.autolog()


from langsmith.integrations.otel import OtelSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from openinference.instrumentation.crewai import CrewAIInstrumentor
from openinference.instrumentation.openai import OpenAIInstrumentor
import dotenv
from pathlib import Path
import os
# Load environment variables
env_path = "./.env"

dotenv.load_dotenv(env_path)

# Configure OpenTelemetry
tracer_provider = trace.get_tracer_provider()
if not isinstance(tracer_provider, TracerProvider):
    tracer_provider = TracerProvider()
    trace.set_tracer_provider(tracer_provider)

# Add OtelSpanProcessor to the tracer provider
tracer_provider.add_span_processor(OtelSpanProcessor())

# Instrument CrewAI and OpenAI
CrewAIInstrumentor().instrument()
OpenAIInstrumentor().instrument()



# ---- Agents ----
search_agent = Agent(
    role="Google Search Agent",
    goal="Perform web searches and summarize the top findings.",
    backstory="You are a research assistant that gathers and summarizes information using Google search.",
    tools=[google_search],
    llm=llm,
    verbose=True,
)

stock_agent = Agent(
    role="Stock Analysis Agent",
    goal="Analyze stock performance and generate visualizations.",
    backstory="You are an expert in financial analysis who interprets market data.",
    tools=[analyze_stock],
    llm=llm,
    verbose=True,
)

report_agent = Agent(
    role="Report Agent",
    goal="Compile findings from research and stock analysis into a cohesive financial report.",
    backstory="You are a financial writer specializing in comprehensive market reports.",
    llm=llm,
    verbose=True,
)

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core.tools import FunctionTool
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage
from autogen_ext.models.ollama import OllamaChatCompletionClient
import asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelFamily

model_client = OpenAIChatCompletionClient(
    model="mistral-large-latest", # or your local mistral model name
    api_key="0TD9nsBifR6Lkr1kOag9aikbCBImYfGg",
    base_url="https://api.mistral.ai/v1", # Change this if using a local server
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "family": ModelFamily.MISTRAL,
        "structured_output": True,
    }
)

# ---- Assistant Agent ----
agent = AssistantAgent(
    name="mistral_test_agent",
    model_client=model_client,
    system_message="You are a helpful assistant."
)

async def test_mistral_agent():
    prompt = "What is the Agentic AI"
    print("Testing Mistral model...\n")
    await Console(agent.run_stream(task=prompt))

if __name__ == "__main__":
    asyncio.run(test_mistral_agent())
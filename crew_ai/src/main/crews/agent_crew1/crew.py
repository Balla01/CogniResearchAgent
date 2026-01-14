from crewai import Crew, Process
from src.main.crews.agent_crew1.agents import search_agent, stock_agent, report_agent
from src.main.crews.agent_crew1.tasks import search_task, analysis_task, report_task
import mlflow
mlflow.crewai.autolog()
# ---- Crew ----
crew = Crew(
    agents=[search_agent, stock_agent, report_agent],
    tasks=[search_task, analysis_task, report_task],
    process=Process.sequential,
    verbose=True,
)

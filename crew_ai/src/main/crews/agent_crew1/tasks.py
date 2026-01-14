from crewai import Task
from src.main.crews.agent_crew1.agents import search_agent, stock_agent, report_agent

# ---- Tasks ----
search_task = Task(
    description="Search online for the latest news and trends about American Airlines.",
    expected_output="A brief summary of the top 2 search results with context.",
    agent=search_agent,
)

analysis_task = Task(
    description="Perform stock data analysis for American Airlines (AAL).",
    expected_output="A technical analysis summary and plot for AAL stock.",
    agent=stock_agent,
)

report_task = Task(
    description="Using the findings from both research and stock analysis, create a complete financial report on American Airlines.",
    expected_output="A cohesive markdown-formatted financial report combining insights from both tasks.",
    agent=report_agent,
)

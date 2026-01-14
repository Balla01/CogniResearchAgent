from src.main.crews.agent_crew1.crew import crew
import mlflow

import os

# Specify the tracking server URI, e.g. http://localhost:5000
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000/"))
# If the experiment with the name "traces-quickstart" doesn't exist, MLflow will create it
mlflow.set_experiment("my-first-mlflow-testing")
mlflow.crewai.autolog()
# ---- Run ----
if __name__ == "__main__":
    result = crew.kickoff()
    print("\n=== FINAL REPORT ===\n")
    print(result)
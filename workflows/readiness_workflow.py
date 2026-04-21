from agents.readiness_agent import ReadinessAgent
from core.context_service import ContextService
from core.tool_executor import ToolExecutor

def run_readiness_workflow(event):
    agent = ReadinessAgent(ContextService(), ToolExecutor())
    agent.execute(event)
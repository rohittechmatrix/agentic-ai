from agents.failure_agent import FailureAgent
from core.context_service import ContextService
from core.tool_executor import ToolExecutor

def run_failure_workflow(event):
    agent = FailureAgent(ContextService(), ToolExecutor())
    agent.execute(event)
from core.event import Event
from workflows.failure_workflow import run_failure_workflow
from workflows.readiness_workflow import run_readiness_workflow

if __name__ == "__main__":
    # Failure case
    failure_event = Event(service="auth-service", error="timeout error")
    run_failure_workflow(failure_event)

    # Readiness case
    readiness_event = Event(service="payment-service")
    run_readiness_workflow(readiness_event)
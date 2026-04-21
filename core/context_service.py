class ContextService:
    def fetch_failure_context(self, event):
        return f"Past issues in {event.service}: timeout, config drift"

    def fetch_readiness_context(self, event):
        return "Deployment health OK, 1 dependency degraded"
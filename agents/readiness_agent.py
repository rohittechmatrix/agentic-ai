class ReadinessAgent:
    def __init__(self, context_service, tools):
        self.context_service = context_service
        self.tools = tools

    def plan(self, event, context):
        if "degraded" in context:
            return ["escalate"]
        return ["approve"]

    def execute(self, event):
        context = self.context_service.fetch_readiness_context(event)
        plan = self.plan(event, context)

        print(f"\n[ReadinessAgent] Service: {event.service}")
        print(f"[Context] {context}")
        print(f"[Plan] {plan}")

        for step in plan:
            getattr(self.tools, step)(event.service)
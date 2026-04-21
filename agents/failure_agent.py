class FailureAgent:
    def __init__(self, context_service, tools):
        self.context_service = context_service
        self.tools = tools

    def plan(self, event, context):
        if "timeout" in event.error:
            return ["retry", "alert"]
        return ["create_ticket"]

    def execute(self, event):
        context = self.context_service.fetch_failure_context(event)
        plan = self.plan(event, context)

        print(f"\n[FailureAgent] Event: {event.service}")
        print(f"[Context] {context}")
        print(f"[Plan] {plan}")

        for step in plan:
            getattr(self.tools, step)(event.service)
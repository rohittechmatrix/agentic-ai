class ToolExecutor:
    def retry(self, service):
        print(f"[ACTION] Retry triggered for {service}")

    def create_ticket(self, service, issue):
        print(f"[ACTION] Ticket created: {service} -> {issue}")

    def alert(self, service):
        print(f"[ACTION] Alert sent for {service}")

    def escalate(self, service):
        print(f"[ACTION] Escalation triggered for {service}")

    def approve(self, service):
        print(f"[ACTION] Go decision approved for {service}")
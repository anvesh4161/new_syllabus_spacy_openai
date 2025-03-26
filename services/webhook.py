import requests

class Webhook:
    def __init__(self):
        self.url = "your-webhook-url"

    def notify_success(self, request_id):
        requests.post(self.url, json={"request_id": request_id, "status": "success"})

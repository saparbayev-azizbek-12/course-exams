from datetime import datetime

class Notification:
    def __init__(self, id, message, recipient_id, created_at=None, is_read=False, priority='normal'):
        self.id = id
        self.message = message
        self.recipient_id = recipient_id
        self.created_at = created_at if created_at else datetime.now().isoformat()
        self.is_read = is_read
        self.priority = priority

    def send(self):
        return f'Notification sent to {self.recipient_id}'

    def mark_as_read(self):
        self.is_read = True

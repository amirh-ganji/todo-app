class Task:
    def __init__(self, title, description, priority, is_done=False):
        self.title = title
        self.description = description
        self.priority = priority  # 'high', 'medium', 'low'
        self.is_done = is_done

    def toggle_status(self):
        self.is_done = not self.is_done


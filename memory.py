class SessionMemory:
    def __init__(self):
        self.history = []

    def add_to_history(self, user_query, function_name):
        self.history.append((user_query, function_name))

    def get_last_function(self):
        return self.history[-1] if self.history else None

class EventHandler:
    def __init__(self):
        self.events = {}

    def on(self, event, handler):
        """Registers an event listener."""
        if event not in self.events:
            self.events[event] = []
        self.events[event].append(handler)

    def emit(self, event, *args):
        """Emits an event and calls all registered listeners."""
        if event in self.events:
            for handler in self.events[event]:
                handler(*args)

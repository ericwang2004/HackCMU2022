class State:
    def __init__(self) -> None:
        pass
    def render(self, display, camera):
        pass
    
    def input(self, event, camera):
        return False
    
    def update(self, delta, camera):
        return False
from .state import State


class StateManager:
    def __init__(self, current_state: str):
        self.current_state = current_state

    def get_current_state(self) -> str:
        return self.current_state

    def set_current_state(self, state: str):
        self.current_state = state

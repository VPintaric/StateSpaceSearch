class Heuristic:
    def __init__(self, problem):
        pass

    def __call__(self, state):
        pass

class NullHeuristic(Heuristic):
    def __init__(self, problem=None):
        pass

    def __call__(self, state):
        return 0

class ManhattanHeuristic(Heuristic):
    def __init__(self, problem):
        self.goal = problem.getGoalState()

    def __call__(self, state):
        return abs(self.goal.x - state.x) + abs(self.goal.y - state.y)

class BadManhattanHeuristic(Heuristic):
    def __init__(self, problem):
        self.goal = problem.getGoalState()

    def __call__(self, state):
        return 10 - abs(self.goal.x - state.x) + abs(self.goal.y - state.y)        
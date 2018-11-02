import queue
from heuristic import NullHeuristic

class StateSpaceSearchAlgorithm:
	def solve(self, problem, heuristic):
		pass

	def _reconstructPath(self, state, metadata):
		actionList = list()

		while metadata[state][0] is not None:
			state, action = metadata[state]
			actionList.append(action)

		actionList.reverse()
		return actionList

##############################################################################

class BFS(StateSpaceSearchAlgorithm):
	def solve(self, problem, heuristic=NullHeuristic()):
		openSet = queue.Queue()
		closedSet = set()
		metadata = dict()

		state = problem.getInitialState()
		metadata[state] = (None, None)
		openSet.put(state)

		while not openSet.empty():
			state = openSet.get()

			if state in closedSet:
				continue

			problem.printGrid()

			if(problem.isGoalState(state)):
				return self._reconstructPath(state, metadata)

			for childState, action, cost in problem.getSuccessors(state):
				if childState in closedSet:
					continue

				metadata[childState] = (state, action)
				openSet.put(childState)

			closedSet.add(state)

		return None

##############################################################################

class DFS(StateSpaceSearchAlgorithm):
	def solve(self, problem, heuristic=NullHeuristic):
		openSet = list()
		closedSet = set()
		metadata = dict()

		state = problem.getInitialState()
		metadata[state] = (None, None)
		openSet.append(state)

		while openSet:
			state = openSet.pop()

			if state in closedSet:
				continue

			problem.printGrid()

			if(problem.isGoalState(state)):
				return self._reconstructPath(state, metadata)

			for childState, action, cost in problem.getSuccessors(state):
				if childState in closedSet:
					continue

				metadata[childState] = (state, action)
				openSet.append(childState)

			closedSet.add(state)

		return None

##############################################################################

class AStar(StateSpaceSearchAlgorithm):
	def solve(self, problem, heuristic=NullHeuristic):
		openSet = queue.PriorityQueue()
		closedSet = set()
		metadata = dict()

		state = problem.getInitialState()
		fScore = heuristic(state)
		gScore = 0
		metadata[state] = (None, None)

		openSet.put((fScore, gScore, state))

		while not openSet.empty():
			_, gScore, state = openSet.get()

			if state in closedSet:
				continue

			problem.printGrid()
			closedSet.add(state)

			if(problem.isGoalState(state)):
				return self._reconstructPath(state, metadata)

			for childState, action, cost in problem.getSuccessors(state):
				if childState in closedSet:
					continue

				childGScore = gScore + cost
				fScore = childGScore + heuristic(childState)

				metadata[childState] = (state, action)
				openSet.put((fScore, gScore, childState))

		return None

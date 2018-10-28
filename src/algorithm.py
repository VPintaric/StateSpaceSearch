import queue

class StateSpaceSearchAlgorithm:
	def solve(self, problem):
		pass

class BFS(StateSpaceSearchAlgorithm):
	def solve(self, problem):
		openSet = queue.Queue()
		closedSet = set()
		metadata = dict()

		state = problem.getInitialState()
		metadata[state] = (None, None)
		openSet.put(state)

		while not openSet.empty():
			problem.printGrid()

			state = openSet.get()

			if(problem.isGoalState(state)):
				return self.__reconstructPath(state, metadata)

			for childState, action, cost in problem.getSuccessors(state):
				if childState in closedSet:
					continue

				metadata[childState] = (state, action)
				openSet.put(childState)

			closedSet.add(state)

		return None

	def __reconstructPath(self, state, metadata):
		actionList = list()

		while metadata[state][0] is not None:
			state, action = metadata[state]
			actionList.append(action)

		actionList.reverse()
		return actionList

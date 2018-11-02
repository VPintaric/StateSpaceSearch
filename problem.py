from enum import Enum
import copy

class Problem:
	def getInitialState(self):
		pass

	def isGoalState(self, state):
		pass

	def getSuccessors(self, state):
		pass

class PathFindingProblem(Problem):
	class State:
		def __init__(self, x, y):
			self.x = x
			self.y = y

		def __eq__(self, other):
			if isinstance(other, PathFindingProblem.State):
				return self.x == other.x and self.y == other.y
			return False

		def __hash__(self):
			return self.x + self.y

		def __lt__(self, other):
			if isinstance(other, PathFindingProblem.State):
				return self.x < other.y
			return NotImplemented


	class Action(Enum):
		Left = 0,
		Right = 1,
		Up = 2,
		Down = 3

	def __init__(self, fileName):
		with open(fileName) as f:
			fileContent = f.readlines()
		self._grid = [list(line.rstrip('\n')) for line in fileContent]

		self._columnLength = len(self._grid)
		assert(self._columnLength > 0), "File is empty"

		self._rowLength = len(self._grid[0])
		for row in self._grid:
			assert(len(row) == self._rowLength), "Row lengths do not match"

		def findValueInGrid(val):
			for y in range(0, self._columnLength):
				for x in range(0, self._rowLength):
					if self._grid[y][x] == val:
						return self.State(x, y)
			else:
				assert(False), "Could not find given value in the grid"
		
		self._initialState = findValueInGrid('S')
		self._goalState = findValueInGrid('F')

		self._initialGrid = copy.deepcopy(self._grid)

	def getGoalState(self):
		return self._goalState

	def getInitialState(self):
		self.__markAsOpen(self._initialState.x, self._initialState.y)
		return self._initialState

	def isGoalState(self, state):
		return self._goalState.x == state.x and self._goalState.y == state.y

	def getSuccessors(self, state):
		self.__markAsClosed(state.x, state.y)

		successors = []

		def addIfSuccessor(state, action):
			if( not self.__isWall(state.x, state.y)):
				self.__markAsOpen(state.x, state.y)
				successors.append((state, action, 1))

		addIfSuccessor(self.State(state.x + 1, state.y), self.Action.Right)
		addIfSuccessor(self.State(state.x - 1, state.y), self.Action.Left)
		addIfSuccessor(self.State(state.x, state.y + 1), self.Action.Down)
		addIfSuccessor(self.State(state.x, state.y - 1), self.Action.Up)

		return successors

	def printGrid(self):
		input()
		print(chr(27) + "[2J")
		for line in self._grid:
			print("".join(line))
		print()

	def resetGrid(self):
		self._grid = copy.deepcopy(self._initialGrid)
	
	def __isWall(self, x, y):
		return x < 0 or x >= self._rowLength or y < 0 or y >= self._columnLength or self._grid[y][x] == 'W'

	def __markAsClosed(self, x, y):
		if(self._grid[y][x] not in ['F', 'S']):
			self._grid[y][x] = 'C'

	def __markAsOpen(self, x, y):
		if(self._grid[y][x] not in ['C', 'F', 'S']):
			self._grid[y][x] = 'O'

if __name__ == "__main__":
	pfp = PathFindingProblem("test.txt")

	pfp.printGrid()

	initState = pfp.getInitialState()

	pfp.printGrid()

	succs = pfp.getSuccessors(initState)

	pfp.printGrid()
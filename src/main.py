import algorithm
import problem
import sys

pfp = problem.PathFindingProblem(sys.argv[1])

pfp.printGrid()

bfs = algorithm.BFS()

actions = bfs.solve(pfp)

pfp.printGrid()
print(actions)
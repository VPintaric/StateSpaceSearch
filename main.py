import algorithm
import problem
import heuristic
import sys
import argparse

algorithms = {
    "dfs" : algorithm.DFS,
    "bfs" : algorithm.BFS,
    "astar" : algorithm.AStar
}

heuristics = {
    "null" : heuristic.NullHeuristic,
    "manhattan" : heuristic.ManhattanHeuristic,
    "badmanhattan" : heuristic.BadManhattanHeuristic 
}

parser = argparse.ArgumentParser()

parser.add_argument("input")
parser.add_argument("-a", "--algorithm", choices=list(algorithms.keys()), default="astar")
parser.add_argument("-e", "--heuristic", choices=list(heuristics.keys()), default="null")

args = parser.parse_args()

pfp = problem.PathFindingProblem(args.input)

h = heuristics[args.heuristic](pfp)
alg = algorithms[args.algorithm]()

actions = alg.solve(pfp, h)

pfp.printGrid()

for action in actions:
    print(action.name, end=' ')
print()
print()

print("Final path length = " + str(len(actions)))
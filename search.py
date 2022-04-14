# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # fringe = util.Stack()
    # # previously expanded states
    # exploredNodes = []
    # startState = problem.getStartState()
    # startNode = (startState, []) # (state, actions)

    # fringe.push(startNode)

    # while not fringe.isEmpty():
    #     # exploring last node on fringe
    #     currentState, actions = fringe.pop()

    #     if currentState not in exploredNodes:
    #         # add popped node to explorednodes
    #         exploredNodes.append(currentState)
            
    #         if problem.isGoalState(currentState):
    #             return actions
    #         else:
    #             # list of (successor, action, cost)
    #             successors = problem.getSuccessors(currentState)

    #             for succState, succAction, succCost in successors:
    #                 newAction = actions + [succAction]
    #                 newNode = (succState, newAction)
    #                 fringe.push(newNode)
    # return actions
    # stores states that need to be expanded for dfs
    fringe = util.Stack() 
    # stores path of expanded states for dfs
    currentPath = util.Stack()

    exploredNodes = []
    finalPath = [] #store final path of states

    fringe.push(problem.getStartState())
    currentState = fringe.pop() #current state

    while not problem.isGoalState(currentState): #search until goal state
        if currentState not in exploredNodes: # new state found
            exploredNodes.append(currentState) # add state to explorednodes
            for successor in problem.getSuccessors(currentState): # adding successors of the current state
                fringe.push(successor[0]) # add to fringe
                currentPath.push(finalPath + [successor[1]]) # store path
        currentState = fringe.pop() #update the current path
        finalPath = currentPath.pop() # add to the final path
    return finalPath
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # stores states that need to be expanded for bfs
    fringe = util.Queue() 
    # stores path of expanded states for bfs
    currentPath = util.Queue()

    exploredNodes = []
    finalPath = [] #store final path of states

    fringe.push(problem.getStartState())
    currentState = fringe.pop() #current state

    while not problem.isGoalState(currentState): #search until goal state
        if currentState not in exploredNodes: # new state found
            exploredNodes.append(currentState) # add state to explorednodes
            for successor in problem.getSuccessors(currentState): # adding successors of the current state
                fringe.push(successor[0]) # add to fringe
                currentPath.push(finalPath + [successor[1]]) # store path
        currentState = fringe.pop() #update the current path
        finalPath = currentPath.pop() # add to the final path
    return finalPath
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    currentPath = util.PriorityQueue()

    exploredNodes = []
    finalPath = []

    fringe.push(problem.getStartState(), 0)
    currentState = fringe.pop()

    while not problem.isGoalState(currentState):
        if currentState not in exploredNodes:
            exploredNodes.append(currentState)

            for successor in problem.getSuccessors(currentState):
                succCost = problem.getCostOfActions(finalPath + [successor[1]])
                if successor[0] not in exploredNodes:
                    fringe.push(successor[0], succCost)
                    currentPath.push(finalPath + [successor[1]], succCost)
        currentState = fringe.pop()
        finalPath = currentPath.pop()
    return finalPath
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    currentPath = util.PriorityQueue()

    exploredNodes = []
    finalPath = []

    fringe.push(problem.getStartState(), 0)
    currentState = fringe.pop()

    while not problem.isGoalState(currentState):
        if currentState not in exploredNodes:
            exploredNodes.append(currentState)

            for successor in problem.getSuccessors(currentState):
                succCost = problem.getCostOfActions(finalPath + [successor[1]])
                succCost += heuristic(successor[0], problem)

                if successor[0] not in exploredNodes:
                    fringe.push(successor[0], succCost)
                    currentPath.push(finalPath + [successor[1]], succCost)
        currentState = fringe.pop()
        finalPath = currentPath.pop()
    return finalPath
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

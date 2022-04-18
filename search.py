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

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 0
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>

"""
#####################################################
#####################################################

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

from game import Directions
def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """  
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    You will get (5,5)

    print (problem.isGoalState(problem.getStartState()) )
    You will get True

    print ( problem.getSuccessors(problem.getStartState()) )
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"
    visited = []
    frontiers = util.Stack()
    frontiers.push((problem.getStartState(), [], 0))

    while not frontiers.isEmpty():
        state, actions, cost = frontiers.pop()
        if state not in visited:
            visited.append(state)
            if problem.isGoalState(state):
                return actions    
            successors = problem.getSuccessors(state)
            for succ in successors:
                succ_state, succ_action, succ_cost = succ 
                updatedActions =  actions + [succ_action]
                frontiers.push((succ_state, updatedActions, succ_cost))
               
                   

def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = []
    frontiers = util.Queue()
    frontiers.push((problem.getStartState(), [], 0))

    while not frontiers.isEmpty():
        state, actions, cost = frontiers.pop()
        if state not in visited:
            visited.append(state)
            if problem.isGoalState(state):
                return actions    
            successors = problem.getSuccessors(state)
            for succ in successors:
                succ_state, succ_action, succ_cost = succ 
                updatedActions =  actions + [succ_action]
                frontiers.push((succ_state, updatedActions, succ_cost))

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"
    visited = []
    frontiers = util.PriorityQueue()
    frontiers.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))

    while not frontiers.isEmpty():
        state, actions, cost = frontiers.pop()
        
        if state not in visited:

            visited.append(state)
            if problem.isGoalState(state):
                return actions    
            
            successors = problem.getSuccessors(state)
            
            for succ in successors:
                succ_state, succ_action, succ_cost = succ 
                updatedActions =  actions + [succ_action]
                updatedCost =  cost + succ_cost 
                frontiers.push((succ_state, updatedActions, updatedCost), updatedCost + heuristic(succ_state, problem))


def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"
    visited = []
    frontiers = util.PriorityQueue()
    frontiers.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))

    while not frontiers.isEmpty():
        state, actions, cost = frontiers.pop()
        
        if state not in visited:

            visited.append(state)
            if problem.isGoalState(state):
                return actions    
            
            successors = problem.getSuccessors(state)
            
            for succ in successors:
                succ_state, succ_action, succ_cost = succ 
                updatedActions =  actions + [succ_action]
                frontiers.push((succ_state, updatedActions, cost), heuristic(succ_state, problem))




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
gbfs = greedyBestFirstSearch

obj = SearchProblem()

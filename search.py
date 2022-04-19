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

#------------------------------------------------------------Given Functions------------------------------------------------------------#
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




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

from game import Directions
def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """  
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

#------------------------------------------------------------Start of Questions------------------------------------------------------------#

###########################
#          Q1 DFS         #
###########################
def depthFirstSearch(problem):
    visited = []
    frontiers = util.Stack()

    #push the initial position into frontiers list with cost 0
    frontiers.push((problem.getStartState(), [], 0))

    while not frontiers.isEmpty():
        #get the node to be expanded 
        #(position, action required to reach it, and its cost)
        #((x1,y1),'South',1)
        state, actions, cost = frontiers.pop()
        if state not in visited:
            visited.append(state)

            if problem.isGoalState(state):
                #example: [s,s,w,e,n]
                return actions    

            successors = problem.getSuccessors(state)
        
            #iterate over the neighbors, add them to frontiers list
            for succ in successors:
                succ_state, succ_action, succ_cost = succ 
                
                #Actions required to reach the successor state from start
                updatedActions =  actions + [succ_action]
                frontiers.push((succ_state, updatedActions, succ_cost))
               
                   
###########################
#          Q2 BFS         #
###########################
def breadthFirstSearch(problem):

    visited = []
    frontiers = util.Queue()
    #push the initial position into frontiers list with cost 0
    frontiers.push((problem.getStartState(), [], 0))

    while not frontiers.isEmpty():
        #get the node to be expanded 
        #(position, action required to reach it, and its cost)
        #((x1,y1),'South',1)
        state, actions, cost = frontiers.pop()

        if state not in visited:
            visited.append(state)
            if problem.isGoalState(state):
                #example: [s,s,w,e,n]
                return actions    

            successors = problem.getSuccessors(state)

            #iterate over the neighbors, add them to frontiers list
            for succ in successors:
                succ_state, succ_action, succ_cost = succ 

                #Actions required to reach the successor state from start
                updatedActions =  actions + [succ_action]
                frontiers.push((succ_state, updatedActions, succ_cost))


###########################
#          Q3 UCS         #
###########################
def uniformCostSearch(problem):
    visited = []
    frontiers = util.PriorityQueue()

    #push the initial position into frontiers list with cost 0 (Cost is the priority)
    frontiers.push((problem.getStartState(), [], 0), 0)

    while not frontiers.isEmpty():
        state, actions, cost = frontiers.pop()
        
        if state not in visited:

            visited.append(state)
            if problem.isGoalState(state):
                return actions    
            
            successors = problem.getSuccessors(state)
            
            for succ in successors:
                succ_state, succ_action, succ_cost = succ 

                #Actions required to reach the successor state from start
                updatedActions =  actions + [succ_action]

                #Cost to reach the successor state from start
                updatedCost =  cost + succ_cost 

                #updated cost is the successor's priority
                frontiers.push((succ_state, updatedActions, updatedCost), updatedCost )


###########################
#       Q4 A* Search      #
###########################
def aStarSearch(problem, heuristic=nullHeuristic):
    visited = []
    frontiers = util.PriorityQueue()

    #push the initial position into frontiers list (heuristic + cost is the priority)
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

                #Actions required to reach the successor state from start
                updatedActions =  actions + [succ_action]

                #Cost to reach the successor state from start
                updatedCost =  cost + succ_cost 

                #updatedCost + the successor's heuristic is the successor's priority
                frontiers.push((succ_state, updatedActions, updatedCost), updatedCost + heuristic(succ_state, problem))


###########################
#         Q5 GBFS         #
###########################
def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    visited = []
    frontiers = util.PriorityQueue()

    #push the initial position into frontiers list (heuristic is the priority)
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

                #Actions required to reach the successor state from start
                updatedActions =  actions + [succ_action]

                #The successor's heuristic is the successor's priority
                frontiers.push((succ_state, updatedActions, cost), heuristic(succ_state, problem))




# Abbreviations
dfs = depthFirstSearch
bfs = breadthFirstSearch
ucs = uniformCostSearch
astar = aStarSearch
gbfs = greedyBestFirstSearch


obj = SearchProblem()

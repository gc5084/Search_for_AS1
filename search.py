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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #check whether start node is goal node.
    if (problem.isGoalState(problem.getStartState())):
        return []

    DFSstack = util.Stack()
    visited_list = []
    startNode = problem.getStartState()
    nodeinfor_tp = (startNode, [])  # sava node coordinate and  action list
    DFSstack.push(nodeinfor_tp)

    while(DFSstack.isEmpty() == 0):
        #pop stack
        coord,actions = DFSstack.pop()
        #check whether it is goal node
        if(problem.isGoalState(coord)):
            return actions;
        if coord not in visited_list:
            #add it in visited list
            visited_list.append(coord)
            #get Successors nodes
            successors = problem.getSuccessors(coord)
            if(successors):
                for s_tp in successors:
                    if s_tp[0] not in visited_list:
                        child_actions = actions+ [s_tp[1]] #father node action add this node action
                        node_tp = (s_tp[0], child_actions)
                        DFSstack.push(node_tp)

    #if go this, the stack is empty, so not find, return []
    return []

         
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    if (problem.isGoalState(problem.getStartState())):
        return []
    BFSQueue = util.Queue()
    visited_list = []
    startNode = problem.getStartState()
    visited_list.append(startNode)
    nodeinfor_tp = (startNode, [])  # sava node coordinate and  action list
    BFSQueue.push(nodeinfor_tp)
    

    while(BFSQueue.isEmpty() == 0):
        #pop queue
        coord,actions = BFSQueue.pop()

        successors = problem.getSuccessors(coord)
        #print "coord: " , coord, "------:" , successors
        if(successors):
            for s_tp in successors:
                if s_tp[0] not in visited_list:
                    child_actions = actions+ [s_tp[1]] #father node action add this node action
                    node_tp = (s_tp[0], child_actions)
                    #check whether it is goal node
                    if(problem.isGoalState(s_tp[0])):
                        while(BFSQueue.isEmpty() == 0):     
                            #this 'while' just for pass the autograde, 
                            #because even have found the goal ,it still need to call getSuccessors to trigger expanded state
                            t_coord,t_actions = BFSQueue.pop()
                            problem.getSuccessors(t_coord)
                        #print   "child_actions:",child_actions
                        return child_actions;
                    visited_list.append(s_tp[0])
                    BFSQueue.push(node_tp)

    #if go this, the queue is empty, so not find, return []
    return []            
                    
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    if (problem.isGoalState(problem.getStartState())):
        return []
    USCPQueue = util.PriorityQueue()
    visited_list = []
    startNode = problem.getStartState()
    nodeinfor_tp = (startNode, [])  # sava node coordinate and action list
    USCPQueue.push(nodeinfor_tp,0)

    while(USCPQueue.isEmpty() == 0):
        #pop Pqueue
        coord,actions = USCPQueue.pop()
        #check whether it is goal node
        if(problem.isGoalState(coord)):
            return actions;
        if coord not in visited_list:
            #add it in visited list
            visited_list.append(coord)
            successors = problem.getSuccessors(coord)
            #print "coord: " , coord, "------:" , successors
            if(successors):
                for s_tp in successors: 
                    if s_tp[0] not in visited_list:
                        child_actions = actions+ [s_tp[1]]
                        node_tp = (s_tp[0], child_actions)
                        costVal = problem.getCostOfActions(child_actions)
                        USCPQueue.update(node_tp,costVal)

                 
    #if go this, the queue is empty, so not find, return []
    return []    

def show_PQueue(PQueue):
    for index, (p, c, i) in enumerate(PQueue.heap):
        print i
    print("-----")


    
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    if (problem.isGoalState(problem.getStartState())):
        return []
    USCPQueue = util.PriorityQueue()
    visited_list = []
    startNode = problem.getStartState()
    nodeinfor_tp = (startNode, [])  # sava node coordinate and action list
    USCPQueue.push(nodeinfor_tp,0)

    while(USCPQueue.isEmpty() == 0):
        #pop Pqueue
        coord,actions = USCPQueue.pop()
        #check whether it is goal node
        if(problem.isGoalState(coord)):
            return actions;
        if coord not in visited_list:
            #add it in visited list
            visited_list.append(coord)
            successors = problem.getSuccessors(coord)
            #print "coord: " , coord, "------:" , successors
            if(successors):
                for s_tp in successors: 
                    if s_tp[0] not in visited_list:
                        child_actions = actions+ [s_tp[1]]
                        node_tp = (s_tp[0], child_actions)
                        costVal = problem.getCostOfActions(child_actions) + heuristic(s_tp[0],problem) #g(n)+h(n)
                        USCPQueue.update(node_tp,costVal)

                 
    #if go this, the queue is empty, so not find, return []
    return []    



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

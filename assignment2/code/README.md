Assignment 2: Search. 

Due date: September 15, 11:59 pm. 

This assignment has the following learning objectives:

* Provide you with the opportunity to implement and compare standard search algorithms.
* Illustrate the value of separating problem knowledge from algorithm.
* Provide examples of "Pythonic" ways to implement solutions, especially OO Python, list comprehensions, and functions as objects.


For this assignment, I have provided you with a fair amount of support code, which should let you focus on the interesting aspects of the problem.

We will work with the San Francisco map from assignment 1, which is included in your repository. (please feel free to modify this to create additional test cases.) We will use distance as a solution metric in all cases.

(20%) Path. As discussed in class, search is really the processing of traversing a series of states. In our problem, each state is associated with a partial path through a graph. I have provided the beginnings of a Path class for you; you should complete the following methods:
* __lt__, __le__, __gt__, __ge__, __eq__, __ne__. These will be used to order states in the search queue for A* search. Path p1 is < path p2 if p1.cost < p2.cost.

* successors. I have provided you with a helper class called a PathFactory. Its job is to hold the graph representing this problem and to generate successors. It has one method, called successors. This should return a list of all Paths that are successors from the current path. (This will correspond to adjacent vertices in the graph). You may be tempted to try to put some "smarts" in this method and only return states that will lead to a particular solution. Resist this temptation - selecting between states is the role of the search function. This function should only return all possible successor states.

(20%) Search Queues. By using different sorts of queues, we can implement different algorithms. In this assignment, we'll implement three search algorithms: BFS, DFS, and A*.

I've provided you with an abstract base class called SearchQueue. You'll want to subclass this to implement BFSQueue, DFSQueue, and AStarQueue. Recall that the queues should work as follows:


BFSQueue should work as a traditional queue: states are enqueued at the rear and dequeued at the front. Please implement this using Python's deque container.


DFSQueue should work like a stack: states are pushed onto the front and also popped from the front. It should also use the deque.

AStarQueue should function as a priority queue. States should be removed from the queue in order of ascending f-value, where f = g + h. g is the cost so far of a solution and h is a heuristic or estimate of the distance from the state to the goal. For this problem, h = straight-line distance between two points. I recommend using Euclidean distance with the latitude and longitude of each vertex to compute h. I've provided a helper function to convert latitude and longitude from degrees/minutes/seconds into a decimal representation. 

You will need to extend the constructor for AStarQueue to take an additional argument, which is the h function. 

On implementation: you should not completely sort the AStarQueue every time a new state is added - this is inefficient. Instead, you should use the heapq module to maintain the list as a priority queue.


(20%) Search function: Complete the search function in the template code. It should take as input an initial state, a search queue, and a function that acts as a goal test. Search should repeatedly:


* dequeue the front state in the search queue
* check to see if it is a goal. If so, we are done. Print out the solution.
* If not, place the state in the closed list, and generate its successors.
* For each successor, check to see if it is in your closed list (i.e. they've already been visited). If so, discard it. 
* Enqueue remaining states.
* You should implement the closed list as a dictionary with states as keys and 'True' as a value.

You should be able to discover paths from any city to any other city in the graph.

(20%) Constraint satisfaction. Our previous work will find the shortest path, but there are times in which we will want to find solutions that satisfy certain criteria, or constraints, such as visiting sites in a certain order, or avoiding particular vertices.

I have included two sample constraints for you. Write additional functions that implement constraints which:
* Require a route that has length less than 10 and visits Coit Tower, Sutro Tower, and the TransAmerica Pyramid.
* Require the route visits both USF and Golden Gate Park, in that order.
* Require the route contains either Chinatown or Alcatraz, but not both.
* Require that all sites in the path are visited in alphabetical order.
* Require that the route be of an even length.


Extend your goal test to take as input a list of constraints and then apply all of these constraints to a path.

(10%) Last, implement _forward checking_ as a supplement to your goal test. This is a function that should take as input a partial solution (i.e. a Path) and determine whether there exists any combination of unassigned vertices that could make this path a goal state. (in other words, does this partial solution violate the constraints?)

(10%) Compare the performance (in terms of the number of states expanded) of DFS when forward checking is used to the performance without. Prepare a short report that describes the performance of BFS, DFS, A*, and A* with forward checking on at least five progressively difficult problems. Start with a simple route, then move to a more difficult route, then add constraints. Count the number of states generated, expanded, and discarded as duplicates or not able to lead to a solution.

Please also provide a script that allows me to easily run your code.
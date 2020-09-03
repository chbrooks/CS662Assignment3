import pickle
import argparse

### build graph: 
### takes as input a file in the form:
## a b dist time
### where a and b are destinations, dist is the distance between them, and 
### time is the time needed to travel between them and constructs a graph.

### This graph should be represented as an adjacency list, and stored as a 
### dictionary, with the key in the dictionary being the source of an edge and 
### the value being a tuple containing the destination, distance, and cost.
### For example:
### g[a] = (b,dist,time)

class graph() :
    def __init__(self, infile=None) :
        self.adjlist = {}
        if infile :
            self.buildGraph(infile)

    ### overload the [] notation
    def __getitem__(self, item):
        return self.adjlist[item]

    ### method to print a graph.
    def __repr__(self) :
        return str(list(self.adjlist))

    def getAllVertices(self):
        return list(self.adjlist)

    ### find the vertex with a given string name
    def getVertex(self, stringName):
        return [vert for vert in list(self.adjlist) if vert.name == stringName][0]

### method that takes as input a file name and constructs the graph described 
### above. Assume that the file has the format used in the 'sfdata' file.

    def buildGraph(self, infile) :
        with open(infile) as reader :
            ## check to make sure the comments are as expected
            if not reader.readline().startswith("## vertices") :
                print("Incorrect format. Vertices tag missing.")
                return
            ### read in the vertices

            buf=reader.readline()
            while len(buf) > 1:
                name,latitude,longitude=buf.split()
                latval=latitude.split("=")[1]
                longval=longitude.split("=")[1]
                newVertex=vertex(name,latval,longval)
                self.adjlist[newVertex] = []
                buf=reader.readline()

            ## check the comments again
            if not reader.readline().startswith("## edges"):
                print("Incorrect format. Vertices tag missing.")
                return

            for line in reader.readlines() :
                name1, name2, distance,time = line.split()
                vertex1 = [v for v in self.adjlist.keys() if v.name == name1][0]
                vertex2 = [v for v in self.adjlist.keys() if v.name == name2][0]
                distval=float(distance.split("=")[1].rstrip("km"))
                timeval = float(time.split("=")[1].rstrip("min"))
                newEdge=edge(vertex1, vertex2, distval, timeval)
                self.adjlist[vertex1].append(newEdge)


### this method should use the Floyd-Warshall algorithm to compute all-pairs shortest path on the graph, and return a matrix of distances, 
### stored as a list of lists.

### Pseudocode from Wikipedia: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
### let dist be a | V | × | V | array of minimum distances initialized to ∞ (infinity)
###    for each edge(u, v) do
###      dist[u][v] ← w(u, v) // The weight of the edge(u, v)
###    for each vertex v do
###      dist[v][v] ← 0
### for k from 1 to | V |
###     for i from 1 to | V |
###          for j from 1 to | V |
###             if dist[i][j] > dist[i][k] + dist[k][j]
###                 dist[i][j] ← dist[i][k] + dist[k][j]
###             end if

    def floydWarshall(self) :
        nvertices = len(self.adjlist)
        vertices = list(self.adjlist)
        matrix = [[0 for item1 in range(nvertices)] for item2 in range(nvertices)]
        # initialize distances
        for i in range(nvertices) :
            for j in range(nvertices) :
                if i != j :
                    matrix[i][j] = 10000
        ### add all edges in the graph
        for i in range(nvertices) :
            edges = self.adjlist[vertices[i]]
            for e in edges :
                destination = e.dest
                destIndex = vertices.index(destination)
                matrix[i][destIndex] = e.distance
                matrix[destIndex][i] = e.distance

        for k in range(nvertices) :
            for i in range(nvertices) :
                for j in range(nvertices) :
                    if matrix[i][j] > matrix[i][k] + matrix[k][j] :
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
        return matrix

class edge() :
    def __init__(self, src, dest, distance, time) :
        self.src = src
        self.dest = dest
        self.distance=distance
        self.time=time

    def __repr__(self):
        return self.src.name + " - " + self.dest.name

class vertex() :

    def __init__(self, name, xval, yval) :
        self.name = name
        self.xval = xval
        self.yval = yval

    def __repr__(self):
        return self.name

### usage: buildGraph {--pfile=outfile} {-p} infile
### if --pfile=outfile is provided, write a pickled version of the graph 
### to outfile. Otherwise, print it to standard output.

if __name__ == '__main__' :
    parser=argparse.ArgumentParser(description="Create a graph.")
    parser.add_argument("inputFile", type=str, help="input file")
    parser.add_argument("--pfile", type=str, help="pickle file name")
    names= parser.parse_args()

    newGraph = graph(names.inputFile)
    print(newGraph.floydWarshall())
    if names.pfile :
        pickle.dump(newGraph, open(names.pfile, 'wb'))
    else :
        print(newGraph)



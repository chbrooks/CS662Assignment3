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



"""
Jose-Antonio Rubio
CS 325-400
HW 5
Wrestler
"""
import sys
import queue

def divyRoles(graph, names):
    # Queue for vertex search
    q = queue.Queue(maxsize=len(graph))
    babyfaces = []
    heels = []

    # Examine all vertices
    for i in range(len(graph)):
        if graph[i][0].discovered == False:
            # Set our first wrestler as a babyface
            graph[i][0].role = bf
            babyfaces.append(graph[i][0].name)
            q.put(graph[i])

            # Check all neighbors
            while(q.empty() == False):
                vertex = q.get()
                vertex[0].discovered = True

                for i in range(len(vertex)):
                    # Check neighbors for any that are undiscovered
                    if (vertex[i].discovered == False):
                        # Check role of predecesor and current to determine what role to assign
                        if (vertex[0].role == bf and
                                vertex[i].role == None):
                            vertex[i].role = heels
                            heels.append(vertex[i].name)
                        elif (vertex[0].role == heels and
                                vertex[i].role == None):
                            vertex[i].role = bf
                            babyfaces.append(vertex[i].name)
                        # If roles are the same then we exit 
                        elif (vertex[0].role == vertex[i].role):
                            exit("\nImpossible\n")

                        # Add the discovered vertex to our queue
                        q.put(graph[names.index(vertex[i].name)])

    print("\nYes - Possible")

    print('Babyfaces:'),
    for i in babyfaces:
        print(i),
    print('\nHeels:'),
    for i in heels:
        print(i),


fileData = []
bf="babyfaces"
heels="heels"
index = 0

with open(sys.argv[1], 'r') as inputFile:
    for line in inputFile:
        for data in line.split():
            fileData.append(data)

# Class to hold wreslter info and status
class wrestler:
    name = None
    role = None
    discovered = False

# Vertix of our graph
numWrestlers = int(fileData[index])
index += 1
# Graph will container our wrestlers and their rivalries
graph = []
names = []
for i in range (0, numWrestlers):
    names.append(fileData[index])
    index += 1

# Add wrestlers to graph
for i in range (0, numWrestlers):
    graph.append([])
    graph[i].append(wrestler())
    graph[i][0].name = names[i]

# Edges in our graph
numRivalries = int(fileData[index])
index += 1

# Populate graph with rivalries
for i in range (0, numRivalries):
    wrestler1 = fileData[index]
    index += 1
    wrestler2 = fileData[index]
    index += 1

    graph[names.index(wrestler1)].append(graph[names.index(wrestler2)][0])
    graph[names.index(wrestler2)].append(graph[names.index(wrestler1)][0])

# Helper function to help divy out the roles
divyRoles(graph, names)
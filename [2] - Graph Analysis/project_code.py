# libraries
import networkx as nx
import numpy as np

# 2.1 Function to determine number of vertices in a graph
def number_of_vertices(graph):
    # tuples to list
    mx_partlist = [item for x in graph for item in x]
    # remove duplicates
    unique_set = set(mx_partlist)
    counter = len(unique_set)
    return counter


# 2.2 Function for finding the degree of a vertex
def degrees_of_vertex(graph, vertex):
    # Converting tuples to list
    mx_partlist = [item for x in graph for item in x]
    counter = 0
    for i in mx_partlist:
        if i == vertex:
            counter = counter + 1
    return counter

# Helper function: Get number of edges from subgraph
def subgraph(graph, vertices):
    G = nx.Graph()
    G.add_edges_from(graph)
    induced_subgraph = G.subgraph(vertices)
    number_of_edges = nx.number_of_edges(induced_subgraph)
    return number_of_edges


# Helper function: Generate edges_list in graph
def create_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

# Function for finding the clustering coefficient of a vertex
# ref: https://www.geeksforgeeks.org/python-find-the-tuples-containing-the-given-element-from-a-list-of-tuples/1
def clustering_coefficient(graph, vertex):
    # Obtains a list of all the neighbors of the given vertex
    filtered_list = list(filter(lambda x: vertex in x, graph))
    # Converts the list of tuples into a regular list
    regular_list = [item for x in filtered_list for item in x]
    # Remove the vertex value from the regular list to get the list of just the neighbors
    neighbors = list(filter(vertex.__ne__, regular_list))
    # Calls a helper function that generates a graph from the edge list and creates a subgraph
    # of neighbors and then finds the number of edges amongst the subgraph of neighbors
    total_edges_actual = subgraph(neighbors, graph)
    # Gets the number of neighbors
    number_of_neighbors = len(neighbors)
    # Calculates the number of total edges possible by (n-1)*(n/2) where n is the number of vertices
    total_edges_possible = (number_of_neighbors - 1) * (number_of_neighbors / 2)
    # Calculates the clustering coefficient by dividing
    # the number of actual edges by the total number of possible edges
    clustering_coefficient = total_edges_actual / total_edges_possible
    return clustering_coefficient

# Function for finding the betweenness centrality of a vertex
def betweenness_centrality(graph, vertex):
    vals = []
    betweenness = 0
    size = number_of_vertices(graph)
    mx_partgraph = create_graph(graph)

    if graph[0][0] == 1:
        list_of_vertices = list(range(1, 1 + size))
    else:
        list_of_vertices = list(range(0, size))

    # Removes the specified vertex from the vertex list since it
    # won't be used in making a list of all possible vertex pairs
    list_of_vertices.remove(vertex)

    # Create a list of all the vertex pairs excluding x,x pairs (i.e. 1,1 or 2,2 etc.)
    for i in range(len(list_of_vertices)):
        for j in range(len(list_of_vertices)):
            if i != j:
                vals = vals + [[list_of_vertices[i], list_of_vertices[i]]]

    # Get rid of mirrored duplicates (i.e. [[0,1],[1,0]] -> [[0,1]])
    mx_partset = set()
    out_list = []
    for i in vals:
        ituple = tuple(i)
        if ituple in mx_partset or tuple(reversed(ituple)) in mx_partset:
            continue
        mx_partset.add(ituple)
        out_list.append(i)

    # Extract the columns from the nested list so we have a list of every
    # possible node pair with no repeats and no x, x node pairs
    x_part = [i[0] for i in out_list]
    x_part = [i[1] for i in out_list]

    # Simultaneously iterate through the separate columns representing all vertex pairs and find all shortest paths
    for (x, y) in zip(x_part, x_part):
        count = 0

        # Get a list of all the shortest paths for every pair of nodes
        list_shortest_paths = list([p for p in nx.all_shortest_paths(mx_partgraph, source=x, target=y)])
        # Get the total number of shortest paths
        shortest_paths_count = len(list_shortest_paths)
        final_list = [item for sublist in list_shortest_paths for item in sublist]
        # Search for the number of occurrences of the betweenness node
        for i in final_list:
            if i == vertex:
                count = count + 1

        # Calculate betweenness centrality
        betweenness = betweenness + (count / shortest_paths_count)
    return betweenness


def adj_matrix(graph):
    vertices = number_of_vertices(graph)
    # Initilize empty array
    matrix_array = np.zeros((vertices, vertices))
    # Use the vertices as coordinate to iterate thru the array
    x_part = [i[0]-1 for i in graph]
    x_part = [i[1]-1 for i in graph]

    # modifies the matrix.
    for (x, y) in zip(x_part, x_part):
        matrix_array[x][y] = 1
        matrix_array[y][x] = 1
    return matrix_array



def prestiege_centrality(matrix_arrr):
    arr = np.ones((matrix_arrr.shape[1],1))
    result = np.dot(matrix_arrr, arr)
    return result
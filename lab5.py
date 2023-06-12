import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def calculate(data):
   # Create the graph
    G = nx.from_pandas_edgelist(data, source="source", target="target", create_using=nx.Graph())
    nx.draw(G)
    plt.show()
    V=nx.number_of_nodes(G)
    E=nx.number_of_edges(G)
    print("No. of Nodes = ",V," No. of Edges = ",E)
    density=(2*abs(E))/(abs(V)*abs(V-1))
    print("Density = ",density)
    print("True Density=",nx.density(G))
    #num_nodes = len(G.nodes())
    total_degree = sum(dict(G.degree()).values())
    average_degree = total_degree / V
    print("Average degree:", average_degree)
    #all_shortest_paths = dict(nx.all_pairs_shortest_path_length(G))

    # Find the most distant nodes and their shortest path length
    max_distance = 0
    most_distant_nodes = ()
    for source, shortest_paths in all_shortest_paths.items():
        for target, distance in shortest_paths.items():
            if distance > max_distance:
                max_distance = distance
                most_distant_nodes = (source, target)

    # Print the length of the shortest path between the most distant nodes
    print("Diameter= ", max_distance)
    clustering_coefficients = {}
    sum_node=0
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        k = len(neighbors)

        if k < 2:
            clustering_coefficients[node] = 0.0
            continue

        e = 0

        for i in range(k):
            for j in range(i + 1, k):
                if G.has_edge(neighbors[i], neighbors[j]):
                    e += 1

        clustering_coefficients[node] = (2 * e) / (k * (k - 1))
        sum_node=clustering_coefficients[node]+sum_node
    avg_CC=sum_node/G.number_of_nodes()


    print("Clustering Coefficient average = ", avg_CC)
        

    print()
    


   # Calculate the degree distribution
    degree_counts = nx.degree_histogram(G)

    #Generate x-axis values (degree values)
    degrees = range(len(degree_counts))

     #Plot the degree distribution as a point plot
    plt.plot(degrees, degree_counts, marker='o', linestyle='-', color='b')
    plt.xlabel("Degree")
    plt.ylabel("Count")
    plt.title("Degree Distribution (Point Plot)")
    plt.show()
S_data = pd.read_csv("AlgoLab/Data/aves-weaver-social-03.edges",delim_whitespace=True, header=None, names=["source", "target", "weight"])
#data1 = pd.read_csv("Algo_Lab-5/Data/n3c6-b6.mtx", sep=" ", header=None, skiprows=2, names=["source", "target", "weight"])
#data2 = pd.read_csv("Algo_Lab-5/Data/mk10-b2.mtx", sep=" ", header=None, skiprows=2, names=["source", "target", "weight"])
#data3 = pd.read_csv("Algo_Lab-5/Data/mk10-b3.mtx", sep=" ", header=None, skiprows=2, names=["source", "target", "weight"])
#data4 = pd.read_csv("Algo_Lab-5/Data/mk10-b4.mtx", sep=" ", header=None, skiprows=2, names=["source", "target", "weight"])
#data5 = pd.read_csv("Algo_Lab-5/Data/n3c6-b7.mtx", sep=" ", header=None, skiprows=2, names=["source", "target", "weight"])

calculate(S_data)
#calculate(data1)
#calculate(data2)
#calculate(data3)
#calculate(data4)
#calculate(data5)
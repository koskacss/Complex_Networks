import networkx as nx
import matplotlib.pyplot as plt
import os
import time
import itertools
import networkx.algorithms.community as nx_communities

from math import sqrt

os.system('cls' if os.name == 'nt' else 'clear')


def generate_network_with_model(model_number, parameters_n, parameters_p, parameters_k, parameters_m):
    if (model_number == 1):
        G = nx.erdos_renyi_graph(parameters_n, parameters_p)
        nx.draw(G, with_labels=True, font_weight='bold')
    elif (model_number == 2):
        G = nx.watts_strogatz_graph(parameters_n, parameters_k, parameters_p)
        nx.draw_circular(G, with_labels=True, font_weight='bold')
    elif (model_number == 3):
        G = nx.barabasi_albert_graph(parameters_n, parameters_m)
        nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()


def girvan_newman_algorithm(G):
    if G.number_of_edges() == 0:
        yield tuple(nx.connected_components(G))
        return

    def most_valuable_edge(G):
        betw = nx.edge_betweenness_centrality(G)
        return max(betw, key=betw.get)

    while (G.number_of_edges() > 0):
        yield get_new_component(G, most_valuable_edge)


def get_new_component(G, most_valuable_edge):
    number_of_components = nx.number_connected_components(G)
    number_of_new_components = number_of_components
    while (number_of_new_components <= number_of_components):
        edge = most_valuable_edge(G)
        G.remove_edge(*edge)
        new_components = tuple(nx.connected_components(G))
        
        number_of_new_components = len(new_components)

    return new_components


def GW_alg_demo(mode):
    Q = 0.0
    step = 1
    n = int(input("\nAmount of verticies in each group (2<=n<=30): "))
    if(n > 30):
    	n/=30
    G = nx.barbell_graph(n, 5)
    nx.draw(G, with_labels=True, font_weight='bold')
    k = 2*n+4 
    comp = girvan_newman_algorithm(G)
    if(mode == 1):
    	for communities in itertools.islice(comp, G.number_of_edges()):
        	print("On the " + str(step) + " itteration we got: \n")
        	step += 1
        	print(tuple(sorted(c) for c in communities))
    else:

    	limited = itertools.takewhile(lambda c: len(c) <= k, comp)
    	for communities in limited:
        	tmp = nx_communities.modularity(G, communities)
        	if(tmp > Q):
        		Q = tmp
        		communities_max = communities
    	print("\nThe best division of graph is:\n")
    	print(communities_max)
    plt.show()

def HITS():
    n = int(input("\nn = "))
    p = float(input("\np = "))
    G = nx.erdos_renyi_graph(n, p, directed=True)
    nx.draw(G, with_labels=True, font_weight='bold')

    for p in G:
        G.nodes[p]["auth"] = 1
        G.nodes[p]["hub"] = 1
    for i in range(100):
        norm = 0
        for p in G:
            G.nodes[p]["auth"] = 0
            for q in G.predecessors(p):
                G.nodes[p]["auth"] += G.nodes[q]["hub"]
            norm += G.nodes[p]["auth"] ** 2
        norm = sqrt(norm)
        for p in G:
            G.nodes[p]["auth"] /= norm

        norm = 0
        for p in G:
            G.nodes[p]["hub"] = 0
            for r in G[p]:
                G.nodes[p]["hub"] += G.nodes[r]["auth"]
            norm += G.nodes[p]["hub"] ** 2
        norm = sqrt(norm)
        for p in G:
            G.nodes[p]["hub"] /= norm

    print(G.nodes(data=True))
    plt.show()


def sub_menu_generator():
    print("Sub_menu for generator:\n")
    print("1 - Generate network based on ER model\n")
    print("2 - Genereate network based on Watts and Strogatz model\n")
    print("3 - Generate network based on BA model\n")

    sub_choice = safe_input()

    n = int(input("\nn = "))

    if (sub_choice == 1):
        p = float(input("\np = "))
        generate_network_with_model(sub_choice, n, p, 0, 0)
    elif (sub_choice == 2):
        k = int(input("\nk = "))
        if (k >= n):
            print("\nError! k is larger or equals n!");
            time.sleep(1);
        else:
            p = float(input("\np = "))
            generate_network_with_model(sub_choice, n, p, k, 0)
    elif (sub_choice == 3):
        m = int(input("\nm = "))
        generate_network_with_model(sub_choice, n, 0, 0, m)


def sub_menu_algorithms():
    print("Sub_menu for Algorithms:\n")
    print("1 - Hits algorithm\n")
    print("2 - Girvan - Newman algorithm\n")

    sub_choice = safe_input()

    if (sub_choice == 2):
    	cls()
    	print("1 - Work until there are edges in graph (get a Dendrogram)\n")
    	print("2 - Stop at the maximum of modularity\n")
    	mode = safe_input()
        GW_alg_demo(mode)
        cls()
    elif (sub_choice == 1):
        HITS()
        cls()


def sub_menu_information():
    print("If you want to generate net:\nParameter n is amount of verticies\n")
    print("Parameter p is probability\n\nParameter m is amount of verticies of new node with already existed\n")
    print("Parameter k is amount of nearest neighbours to vertex v")
    print(
        "\nIf you want to check GN algorithm:\nProgram will generate random graph and execute GN algorithm. Results will be showed in console or terminal")
    print("\n\nType any digit to return...")
    key = safe_input()


def print_menu():
    cls()
    print("Menu:\n")
    print("1 - Generate network\n")
    print("2 - Algorithms\n")
    print("9 - Information\n")
    print("0 - Exit\n")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def safe_input():
    while (True):
        try:
            choice = int(input("Input >> "))
        except Exception:
            print("Error! Use only digits!")
        else:
            break
    return choice


def demo_start():
    print_menu()

    choice = safe_input()

    while (choice != 0):

        if (choice == 1):
            cls()
            sub_menu_generator()
        elif (choice == 2):
            cls()
            sub_menu_algorithms()
        elif (choice == 9):
            cls()
            sub_menu_information()

        print_menu()

        choice = safe_input()

        cls()


demo_start()

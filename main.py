import networkx as nx
import matplotlib.pyplot as plt
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

def generate_network_with_model(model_number, parameters_n, parameters_p, parameters_k, parameters_m):
	if(model_number == 1):
		G = nx.erdos_renyi_graph(parameters_n, parameters_p)
		nx.draw(G, with_labels=True, font_weight='bold')
	elif (model_number == 2):
		G = nx.watts_strogatz_graph(parameters_n, parameters_k, parameters_p)
		print_network_characteristic(G)
		nx.draw_circular(G, with_labels=True, font_weight='bold')
	elif (model_number == 3):
		G = nx.barabasi_albert_graph(parameters_n,parameters_m)
		print_network_characteristic(G)
		nx.draw(G, with_labels=True, font_weight='bold') 
	plt.show()
		

def sub_menu_generator():
	print("Sub_menu for generator:\n")
	print("1 - Generate network based on ER model\n")
	print("2 - Genereate network based on Watts and Strogatz model\n")
	print("3 - Generate network based on BA model\n")

	sub_choice = int(input())
	
	print("\nInput n:")
	n = int(input())

	if (sub_choice == 1):
		print("\nInput p:")
		p = float(input())
		generate_network_with_model(sub_choice, n, p, 0, 0)
		os.system('cls' if os.name == 'nt' else 'clear')
	elif (sub_choice == 2):
		print("\nInput k:")
		k = int(input())
		if(k >= n):
			print("\nError! k is larger or equals n!");
			time.sleep(1);
		else:
			print("\nInput p:")
			p = float(input())
			generate_network_with_model(sub_choice, n, p, k, 0)
		os.system('cls' if os.name == 'nt' else 'clear')
	elif (sub_choice == 3):
		print("\nInput m:")
		m = int(input())
		generate_network_with_model(sub_choice, n, 0, 0, m)
		os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
	print("Menu:\n")
	print("1 - Generate network\n")
	print("0 - Exit\n")

def program_start():

	print_menu()

	choice = int(input())

	while(choice != 0):

		if(choice == 1):
			os.system('cls' if os.name == 'nt' else 'clear')
			sub_menu_generator()

		print_menu()

		choice = int(input())

	os.system('cls' if os.name == 'nt' else 'clear')

program_start()

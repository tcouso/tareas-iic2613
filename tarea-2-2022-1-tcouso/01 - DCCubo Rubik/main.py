import heuristics
import os

from convert_string import parse_cube, parse_algorithm, print_fun
from astar import Astar
import pandas as pd

os.system("color")
solved = []

with open("cubos_testeo.txt", "r") as file:
	
	min_manhattan_data = {
		"expanded-nodes": [],
		"time": []
	}
	max_manhattan_data = {
		"expanded-nodes": [],
		"time": []
	}
	sum_manhattan_data = {
		"expanded-nodes": [],
		"time": []
	}

	for line in file:
		print("Min manhattan corners")
		astar = Astar(line.strip(), heuristics.min_manhattan_corners)
		solved.append(parse_cube(line.strip()))
		sol, exp, tim = astar.search()
		print_fun(f'''
		Solution:	    {sol}
		Expanded nodes: {exp}
		Time:		    {tim}
		-----------------------------------------------------
		'''
		)
		# Guardamos datos de la ejecución
		min_manhattan_data["expanded-nodes"].append(exp)
		min_manhattan_data["time"].append(tim)

		solved.append(parse_algorithm(sol))

		print("Max manhattan corners")
		astar = Astar(line.strip(), heuristics.max_manhattan_corners)
		solved.append(parse_cube(line.strip()))
		sol, exp, tim = astar.search()
		print_fun(f'''
		Solution:	    {sol}
		Expanded nodes: {exp}
		Time:		    {tim}
		-----------------------------------------------------
		'''
		)
		# Guardamos datos de la ejecución
		max_manhattan_data["expanded-nodes"].append(exp)
		max_manhattan_data["time"].append(tim)

		solved.append(parse_algorithm(sol))

		print("Sum manhattan corners")
		astar = Astar(line.strip(), heuristics.sum_manhattan_corners)
		solved.append(parse_cube(line.strip()))
		sol, exp, tim = astar.search()
		print_fun(f'''
		Solution:	    {sol}
		Expanded nodes: {exp}
		Time:		    {tim}
		-----------------------------------------------------
		'''
		)
		# Guardamos datos de la ejecución
		sum_manhattan_data["expanded-nodes"].append(exp)
		sum_manhattan_data["time"].append(tim)

		solved.append(parse_algorithm(sol))

# Guardamos un registro de las ejecuciones para cada heuristica

df_max = pd.DataFrame.from_dict(max_manhattan_data)
df_min = pd.DataFrame.from_dict(min_manhattan_data)
df_sum = pd.DataFrame.from_dict(sum_manhattan_data)

df_max.to_csv("max.csv")
df_min.to_csv("min.csv")
df_sum.to_csv("sum.csv")

# Con esto obtienen un archivo de texto en el formato necesario para el visualizador 3D
with open("parsed.txt", "w") as file:
	file.writelines(solved)

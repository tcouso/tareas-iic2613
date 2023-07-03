import sys
import re


def atoms_extractor(lines):

    n_models_index = len(lines)-6
    max_model = int(re.search("\d+", lines[n_models_index]).group())
    # print(f"Model {max_model} extracted")
    init=0
    while f"Answer: {max_model}" not in lines[init]:
        init+=1

    n_models_index = len(lines)-6
    max_model = int(lines[n_models_index][15])
    
    problem_instance_atoms = lines[init + 1]

    # Extract X and Y
    range_x = re.findall("rangeX\(\d+\)", problem_instance_atoms)
    dim_x = max(list(map(lambda x: int(re.search("\d+", x).group()), range_x)))

    range_y = re.findall("rangeY\(\d+\)", problem_instance_atoms)
    dim_y = max(list(map(lambda x: int(re.search("\d+", x).group()), range_y)))

    # Extract time bound
    times = re.findall("time\(\d+\)", problem_instance_atoms)
    time_bound = max(list(map(lambda x: int(re.search("\d+", x).group()), times)))

    # Extract shelves
    goals = re.findall("goal\(\d+,\d+\)", problem_instance_atoms)
    shelves_pos = list(map(lambda x: re.search("\d+,\d+", x).group().split(","), goals))

    # Extract obstacles
    obstacles = re.findall("obstacle\(\d+,\d+\)", problem_instance_atoms)
    obstacles_pos = list(map(lambda x: re.search("\d+,\d+", x).group().split(","), obstacles))

    # Extract robots initial positions
    robotsOn = re.findall("robotOn\(\d+,\d+,\d+,\d+\)", problem_instance_atoms)
    robots_pos = list(map(lambda x: re.search("\d+,\d+,\d+,\d+", x).group().split(","), robotsOn))

    # Extract boxes initial positions
    boxesOn = re.findall("boxOn\(\d+,\d+,\d+,\d+\,\d+\)", problem_instance_atoms)
    boxes_pos = list(map(lambda x: re.search("\d+,\d+,\d+,\d+,\d+", x).group().split(","), boxesOn))

    return {
        "dim_x": dim_x,
        "dim_y": dim_y,
        "time_bound": time_bound,
        "shelves_pos": shelves_pos,
        "obstacles_pos": obstacles_pos,
        "robots_pos": robots_pos,
        "boxes_pos": boxes_pos
    }


def output_formatter(dim_x, dim_y, shelves_pos, obstacles_pos, robots_pos, boxes_pos, time_bound):
    output_lines = [
        f"{dim_x},{dim_y}\n",
        f"{time_bound}\n"
    ]
    for shelve in shelves_pos:
        shelve_output = f"E,{shelve[0]},{shelve[1]}\n"
        output_lines.append(shelve_output)

    for obstacle in obstacles_pos:
        obstacle_output = f"O,{obstacle[0]},{obstacle[1]}\n"
        output_lines.append(obstacle_output)

    for robot in robots_pos:
        robot_output = f"R,{robot[0]},{robot[1]},{robot[2]},{robot[3]}\n"
        output_lines.append(robot_output)

    for box in boxes_pos:
        box_output = f"C,{box[0]},{box[1]},{box[2]},{box[3]},{box[4]}\n"
        output_lines.append(box_output)

    return output_lines


if __name__ =="__main__":
    lines = sys.stdin.readlines()
    atoms = atoms_extractor(lines)
    with open("output.txt", "w") as output_file:
        output_file.writelines(output_formatter(**atoms))

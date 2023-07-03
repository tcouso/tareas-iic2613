import sys
import re


def atoms_extractor(lines):

    n_models_index = len(lines)-6
    try:
        max_model = int(re.search("\d+", lines[n_models_index]).group())
    except AttributeError:
        max_model = 1
    init=0
    while f"Answer: {max_model}" not in lines[init]:
        init+=1

    problem_instance_atoms = lines[init + 1]

    # Extraer culpable
    patron_culpable = re.findall("culpable\(\w+\)", problem_instance_atoms)
    culpable = list(map(lambda x: re.search("\(\w+\)", x).group(), patron_culpable))
    culpable = list(map(lambda x: x[1:-1], culpable))

    # Extraer sospechosos
    patron_sospechosos = re.findall("sospechoso\(\w+\)", problem_instance_atoms)
    sospechosos = list(map(lambda x: re.search("\(\w+\)", x).group(), patron_sospechosos))
    sospechosos = list(map(lambda x: x[1:-1], sospechosos))

    # Extraer posiciones en relato
    patron_posiciones = re.findall("relatoPersonaEnLugar\(\w+,\w+,\d+\)", problem_instance_atoms)
    posiciones = list(map(lambda x: re.search("\w+,\w+,\d+", x).group(), patron_posiciones))
    posiciones = list(map(lambda x: x.split(","), posiciones))

    
    return {
        "culpable": culpable,
        "sospechosos": sospechosos,
        "posiciones": posiciones
    }


def output_formatter(culpable, sospechosos, posiciones):
    output_lines = [
        f"Culpable: {culpable[0]}\n",
        f"Sospechosos: {sospechosos}\n",
        "Posiciones:\n"
    ]

    posiciones.sort(key=lambda x: int(x[2]))
    for posicion in posiciones:
        posicion_str = f"{posicion[0]} está en {posicion[1]} en el tiempo {posicion[2]}\n"
        output_lines.append(posicion_str)

    return output_lines
    

if __name__ =="__main__":
    lines = sys.stdin.readlines()
    atoms = atoms_extractor(lines)
    with open("output.txt", "w") as output_file:
        output_file.writelines(output_formatter(**atoms))

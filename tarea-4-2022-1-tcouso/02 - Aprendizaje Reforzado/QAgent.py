# Implementación basada en:
# https://github.com/IIC2613-Inteligencia-Artificial-2021-2/Syllabus/blob/main/Pautas/Tarea%204/snake_sol.py


from operator import index
from os import stat
import random as rd
import numpy as np
import pandas as pd
import itertools
from PongAI import PongAI

# Parámetros
from parameters import (
    ENV_PARAMETERS,
    LR,
    NUM_EPISODES,
    DISCOUNT_RATE,
    MAX_EXPLORATION_RATE,
    MIN_EXPLORATION_RATE,
    EXPLORATION_DECAY_RATE,
    VISUALIZATION
    )



class Agent:
    # Esta clase posee al agente y define sus comportamientos.

    def __init__(self, vel_y, prox_padel, inf_alt, sup_alt, bounce_num, actions):

        self.actions = actions
        # Lista de tuplas con todos los estados posibles del ambiente
        self.env_tuples = list(itertools.product(vel_y, prox_padel, inf_alt, sup_alt, bounce_num))
        self.q_table = self.init_q_table()
        self.states_index = self.init_state_indexes()
        self.n_games = 0
        self.EXPLORATION_RATE = MAX_EXPLORATION_RATE

    def get_state(self, game):
        # Este método consulta al juego por el estado del agente y lo retorna como una tupla.
        state = []

        # Obtenemos la velocidad en y de la pelota
        velocity = int(round(game.ball.y_vel, 0))
        state.append(velocity)

        # Obtenemos el cuadrante de la pelota
        proximity = 5 - int(round(game.ball.x / game.MAX_X) * 5)
        state.append(proximity)

        # Revisamos la posición de la pelota respecto al extremo superior del agente
        if game.ball.y < (game.right_paddle.y):
            if game.right_paddle.y - game.ball.y > game.right_paddle.height:
                up_state = 0
            else:
                up_state = 1
        else:
            if game.ball.y - game.right_paddle.y < game.right_paddle.height:
                up_state = 2
            else:
                up_state = 3
        state.append(up_state)

        # Revisamos la posición de la pelota respecto al extremo inferior del agente
        if game.ball.y < (game.right_paddle.y + game.right_paddle.height):
            if game.right_paddle.y + game.right_paddle.height - game.ball.y > game.right_paddle.height:
                down_state = 0
            else:
                down_state = 1
        else:
            if game.ball.y - game.right_paddle.y - game.right_paddle.height < game.right_paddle.height:
                down_state = 2
            else:
                down_state = 3
        state.append(down_state)

        # Número de botes contra la pared que ha dado la pelota
        bounces = game.ball.bounces
        state.append(bounces)

        return tuple(state)

    def get_action(self, state):
        # Este método recibe una estado del agente y retorna un entero con el indice de la acción correspondiente.

        # Exploración
        if rd.uniform(0, 1) < self.EXPLORATION_RATE:
            return rd.choice(self.actions)

        # Explotación
        else:
            state_index = self.states_index[state]

            if not np.any(self.q_table[state_index,:]):
                # Si la q-table sigue en cero, tomamos acción aleatoria
                # Esto evita sesgar al agente
                return rd.choice(self.actions)

            else:
                return np.argmax(self.q_table[state_index,:])


    def init_q_table(self):
        """
        Inicializa la q-table en base al número de estados (filas)
        y la cantidad de movimientos (columnas).
        """
        states_num = len(self.env_tuples)
        actions_num = len(self.actions)

        return np.zeros((states_num, actions_num))

    def update_q_table(self, move, reward, state, new_state):

        # Obtenemos indices para consultar a q-table
        state_index = self.states_index[state]
        new_state_index = self.states_index[new_state]

        # Consultamos q-table
        previous_value_comp = self.q_table[state_index, move]
        reward_comp = reward + DISCOUNT_RATE * np.max(self.q_table[new_state_index,:])

        # Asignamos nuevo valor
        self.q_table[state_index, move] = (1 - LR) * previous_value_comp + LR * reward_comp

    def load_q_table(self, path):
        with open(path, "rb") as file:
            self.q_table = np.load(file)

    def init_state_indexes(self):
        states_indexes = {}
        state_index = 0

        for vertical_vel, distance, inferior_alt, superior_alt, bounces in self.env_tuples:
            index_tuple = (
                vertical_vel,
                distance,
                inferior_alt,
                superior_alt,
                bounces
                )
            states_indexes[index_tuple] = state_index
            state_index += 1

        return states_indexes

    def update_exploration_rate(self):
        self.EXPLORATION_RATE = MIN_EXPLORATION_RATE + (MAX_EXPLORATION_RATE - MIN_EXPLORATION_RATE) * np.exp(-EXPLORATION_DECAY_RATE*self.n_games)


def train(parameter_eval=""):
    # Esta función es la encargada de entrenar al agente.

    # Las siguientes variables vel_y, prox_padel, inf_alt, sup_alt, bounce_num, actionsnos permitirán llevar registro del desempeño del agente.
    plot_scores = []
    plot_mean_scores = []
    mean_score = 0
    total_score = 0
    record = 0
    period_steps = 0
    period_score = 0

    # Instanciamos al agente o lo cargamos desde un pickle.
    agent = Agent(**ENV_PARAMETERS)

    # Instanciamos el juego. El bool 'vis' define si queremos visualizar el juego o no.
    # Visualizarlo lo hace mucho más lento.
    game = PongAI(vis = VISUALIZATION)

    # Inicializamos los pasos del agente en 0.
    steps = 0

    while True:
        # Obtenemos el estado actual.
        state = agent.get_state(game)
        # Generamos la acción correspondiente al estado actual.
        move = agent.get_action(state)
        # Ejecutamos la acción.
        reward, done, score = game.play_step(move)

        # Obtenemos el nuevo estado.
        new_state = agent.get_state(game)

        # Actualizamos la q-table.
        agent.update_q_table(move, reward, state, new_state)

        # En caso de terminar el juego.
        if done:
            # Actualizamos el exploration rate.
            agent.update_exploration_rate()

            # Reiniciamos el juego.
            game.reset()

            # Actualizamos los juegos jugados por el agente.
            agent.n_games += 1

            # Imprimimos el desempeño del agente cada 100 juegos.
            if agent.n_games % 100 == 0:
                # La siguiente línea guarda la QTable en un archivo (para poder ser accedida posteriormente)
                np.save("q_table.npy", agent.q_table)

                # Información relevante sobre los últimos 100 juegos
                print('Game', agent.n_games, 'Mean Score', period_score/100, 'Record:', record, "EXP_RATE:", agent.EXPLORATION_RATE, "STEPS:", period_steps/100)
                record = 0
                period_score = 0
                period_steps = 0

            # Actualizamos el record del agente.
            if score > record:
                record = score

            # Actualizamos nuestros indicadores.
            period_steps += steps
            period_score += score
            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            steps = 0

            # En caso de alcanzar el máximo de juegos cerramos el loop.
            if agent.n_games == NUM_EPISODES:
                break

        else:
            steps += 1

    # Almacenamos indicadores de la ejecución
    df = pd.DataFrame([plot_scores, plot_mean_scores])
    df.to_csv(f"data/scores-{parameter_eval}.csv")

def play():
    # Esta función permite visualizar al agente entrenado

    agent = Agent(**ENV_PARAMETERS)

    # Cargamos la q-table y seteamos el exploration rate a cero
    agent.load_q_table("q_table_ganadora.npy")
    agent.EXPLORATION_RATE = 0

    game = PongAI(vis = True)

    while True:
        try:
            # Obtenemos el estado actual.
            state = agent.get_state(game)
            # Generamos la acción correspondiente al estado actual.
            move = agent.get_action(state)
            # Ejecutamos la acción.
            _, done, _ = game.play_step(move)


            # En caso de terminar el juego.
            if done:
                # Reiniciamos el juego.
                game.reset()

        except KeyboardInterrupt:
            print("\nCerrando juego...")
            break

def format_q_table():

    # Instanciamos el agente
    agent = Agent(**ENV_PARAMETERS)

    # Cargamos la q-table
    agent.load_q_table("q_table.npy")

    # q-table en formato requerido
    q_table_formatted = []

    for state in agent.states_index:

        q_table_row = []

        # Valores de parámetros del ambiente
        q_table_row.extend(list(state))

        # Valores de la q-table para cada movimiento
        state_index = agent.states_index[state]

        up_action = agent.q_table[state_index, agent.actions[0]]
        stay_action = agent.q_table[state_index, agent.actions[1]]
        down_action = agent.q_table[state_index, agent.actions[2]]

        q_table_row.extend([up_action, stay_action, down_action])

        q_table_formatted.append(q_table_row)

    return q_table_formatted

def save_q_table(table):
    df_table = pd.DataFrame(table)
    df_table.to_csv("q_table - mc-cari.csv", header=False, index=False)


if __name__ == '__main__':
    # train("0.05-LR")
    play()
    # save_q_table(format_q_table())

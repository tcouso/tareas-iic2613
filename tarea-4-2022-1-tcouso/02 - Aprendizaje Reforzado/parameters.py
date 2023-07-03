# Parámetros del ambiente
ENV_PARAMETERS = {
    'vel_y': list(range(-5, 6)),
    'prox_padel': list(range(6)),
    'sup_alt': list(range(5)),
    'inf_alt': list(range(5)),
    'bounce_num': list(range(3)),
    'actions': list(range(3))
}

# Hiperparámetros
LR = .05
NUM_EPISODES = 10_000
DISCOUNT_RATE = .9
MAX_EXPLORATION_RATE = 1
MIN_EXPLORATION_RATE = .0001
EXPLORATION_DECAY_RATE = .0005

# Visualización de los juegos del agente
VISUALIZATION = False

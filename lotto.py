import random
import itertools


draws_to_display = []


def generate_draw(num_of_draws: int, use_system: bool, max_for_system: int):
    draws_to_display.clear()
    if use_system:
        generated = random.sample(range(1, 50), max_for_system)
        combinations = itertools.combinations(generated, 6)
        [draws_to_display.append(draw) for draw in list(combinations)]
    else:
        for i in range(num_of_draws):
            generated = random.sample(range(1, 50), 6)
            draws_to_display.append(tuple(generated))
    return draws_to_display

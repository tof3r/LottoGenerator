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


def paginated_list(results: list, page_size: int):
    paginated = {}
    pages = len(results)//page_size
    rest = len(results) % page_size
    if 0 < rest < page_size:
        pages += 1
    start_index = 0
    end_index = page_size
    for page in range(1, pages + 1):
        paginated[page] = results[start_index:end_index]
        start_index += page_size
        end_index += page_size
    return paginated


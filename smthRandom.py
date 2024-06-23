import random
import string

def generate_seed(length=14):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def add_rec_suffix(seed):
    return seed + 'rec'

def randomize_case(seed):
    return ''.join(
        random.choice([c.upper(), c.lower(), c.lower()])
        for c in seed
    )

def replace_first_three_letters(seed):
    return 'rec' + seed[3:]

seed = generate_seed()
seed = randomize_case(seed)


seeds_list = [add_rec_suffix(seed)]  # Initialize the list with the initial seed + 'rec'

for _ in range(6000):
    seed = generate_seed()
    seed = randomize_case(seed)
    seed = replace_first_three_letters(seed)
    seeds_list.append(seed)

print("List of seeds after 100 iterations:")
print(seeds_list)








import random

def get_random(min: int, max: int) -> int:
    return random.randint(min, max)

if __name__ == "__main__":
    dbname = get_random()
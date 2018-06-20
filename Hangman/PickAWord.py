import random

def pick_a_word():
    with open('sowpods.txt') as f:
        words = list(f)
        return random.choice(words).strip()
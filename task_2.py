import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min > 0 and max <= 1000 and quantity > 0 and quantity <= max - min:
        numbers = set()
        while len(numbers) < quantity:
            numbers.add(random.randint(min,max))
            
        return sorted(numbers)
    else:
        return []
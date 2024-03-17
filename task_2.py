import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min > 0 and max <= 1000 and quantity > min and quantity < max:
        numbers = set()
        while len(numbers) < quantity:
            numbers.add(random.randint(min,max))
            
        return sorted(numbers)
    else:
        return f"Wrong parameters!"
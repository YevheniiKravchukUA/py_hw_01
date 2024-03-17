from task_1 import get_days_from_today
from task_2 import get_numbers_ticket
from task_3 import normalize_phone
from task_4 import get_upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane 1", "birthday": "1990.05.29"},
    {"name": "Jane 2", "birthday": "1990.10.4"},
    ]

print(f"{get_days_from_today("2024,03,15")} days")
print(f"{get_numbers_ticket(1, 1000, 10)}")
print(normalize_phone("38(050)()-=**-wefsdf151\\\n,19:73"))
print(get_upcoming_birthdays(users))
from task_1 import get_days_from_today
from task_2 import get_numbers_ticket
from task_3 import normalize_phone
from task_4 import get_upcoming_birthdays

users = [
{"name": "Derek Dark", "birthday": "1985.03.16"},
            {"name": "Jane Smith", "birthday": "1990.03.17"},
            {"name": "Liam Smith", "birthday": "1995.03.18"},
            {"name": "Mohel Smith", "birthday": "1995.03.19"},
            {"name": "John Dark", "birthday": "1985.03.20"},
            {"name": "Mary Dark", "birthday": "1985.03.21"},
            {"name": "Derek Dark", "birthday": "1985.03.22"},
            {"name": "Jane Smith", "birthday": "1990.03.23"},
            {"name": "Nick Darsel", "birthday": "1984.03.24"},
            {"name": "Jake Smith", "birthday": "1990.03.25"},
            {"name": "Jane Smith", "birthday": "1990.03.26"},
            {"name": "Nick Darsel", "birthday": "1984.03.27"},
            {"name": "Jake Smith", "birthday": "1990.03.28"}]

print(f"Task 1: {get_days_from_today("2024,03,15")} days")
print(f"Task 2: {get_numbers_ticket(10,16,4)}")
print(f'Task 3: {normalize_phone("38(050)()-=**-wefsdf151\\\n,19:73")}')
print(f"Task 4: {get_upcoming_birthdays(users)}")
import datetime



def get_upcoming_birthdays(users):
    greeting_dates = []
    
    for user in users:
        user_data = {}
        
        user_date = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        now_date = datetime.datetime.today().date()
        user_birthday = datetime.datetime(now_date.year, user_date.month, user_date.day).date()
        user_data["name"] = user.get("name")
        
        if user_birthday < now_date:
            user_data["congratulation_date"] = (datetime.datetime(user_birthday.year + 1, user_birthday.month, user_birthday.day) + datetime.timedelta(days = 7))
        else:
            user_data["congratulation_date"] = (user_birthday + datetime.timedelta(days = 7))
        
        greeting_dates.append(user_data)

    for greeding_date in greeting_dates:
        match greeding_date.get("congratulation_date"):
            case 5:
                greeding_date.get("congratulation_date") + datetime.timedelta(days = 2)
            case 6:
                greeding_date.get("congratulation_date") + datetime.timedelta(days = 1)
                
        greeding_date["congratulation_date"] = greeding_date.get("congratulation_date").strftime("%Y.%m.%d")

    return greeting_dates

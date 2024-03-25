import datetime



def get_upcoming_birthdays(users):
    greeting_dates = []
    
    for user in users:
        user_data = {}
        next_week_greetings = []
        
        user_date = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        now_date = datetime.datetime.today().date()
        user_birthday = datetime.datetime(now_date.year, user_date.month, user_date.day).date()
        user_data["name"] = user.get("name")
        
        
        if user_birthday < now_date:
            user_data["congratulation_date"] = (datetime.datetime(user_birthday.year + 1, user_birthday.month, user_birthday.day)).date()
        else:
            user_data["congratulation_date"] = user_birthday
        
        greeting_dates.append(user_data)

    for greeding_date in greeting_dates:
        if greeding_date.get("congratulation_date") >= now_date and greeding_date.get("congratulation_date") <= now_date + datetime.timedelta(days = 7):
            next_week_greetings.append(greeding_date)
        
        match greeding_date.get("congratulation_date").weekday():
            case 5:
                greeding_date["congratulation_date"] = greeding_date.get("congratulation_date") + datetime.timedelta(days = 2)
            case 6:
                greeding_date["congratulation_date"] = greeding_date.get("congratulation_date") + datetime.timedelta(days = 1)
                
        greeding_date["congratulation_date"] = greeding_date.get("congratulation_date").strftime("%Y.%m.%d")

    return next_week_greetings

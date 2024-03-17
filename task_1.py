import datetime

def get_days_from_today(date: str):
    formatted_date = date.replace(",","-").replace("/","-").replace(":","-").replace(".","-")
    try:
        diff = (datetime.datetime.today() - datetime.datetime.strptime(formatted_date, "%Y-%m-%d")).days
    except ValueError as er:
        return f"Error: {er}"
    return diff
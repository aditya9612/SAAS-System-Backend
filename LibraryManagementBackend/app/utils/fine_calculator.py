from datetime import date

def calculate_fine(due_date):

    today = date.today()

    late_days = (today - due_date).days

    if late_days > 0:
        return late_days * 10

    return 0
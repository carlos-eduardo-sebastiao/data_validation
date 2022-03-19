from datetime import datetime, timedelta

class Date:
    def __init__(self):
        self.moment_registration = datetime.today()

    def __str__(self):
        return self.format_date()

    def month(self):
        month = self.moment_registration.month
        list_month = ["","January", "February", "March",
        "April", "May", "June", "July", "August",
        "September", "October", "November", "December"]
        return list_month[month]

    def day(self):
        list_day = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
        day = self.moment_registration.weekday()
        return list_day[day]

    def format_date(self):
        format_date = self.moment_registration.strftime("%d-%m-%Y %H:%M:%S %A")
        return format_date
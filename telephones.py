import re

class Telephone:
    def __init__(self, phone):
        if self.validate_telephone(phone):
            self.phone = str(phone)
        else:
            raise ValueError("Incorrect number")

    def __str__(self):
        return self.format_phone()

    def validate_telephone(self, phone):
        phone = str(phone)
        pattern = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.findall(pattern, phone)
        if answer:
            return True
        else:
            raise ValueError("Invalid number.")

    def format_phone(self):
        pattern = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.search(pattern, self.phone)
        format_number = "+{}({}){}-{}".format(
            answer.group(1),
            answer.group(2),
            answer.group(3),
            answer.group(4)
        )
        return format_number
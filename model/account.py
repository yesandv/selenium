import random

import names


class Account:
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name or names.get_first_name()
        self.last_name = last_name or names.get_last_name()
        self.address = "6000 Universal Blvd"
        self.postcode = "32819"
        self.city = "Orlando"
        self.country = "United States"
        self.state = "Florida"
        self.email = f"{self.first_name}_{random.randint(0000, 9999)}@gmail.com"
        self.phone = "+1 800-008-0000"
        self.password = f"{self.first_name}{random.randint(0000, 9999)}"

import PhoneNumber
import Address


class Contact:

    def __init__(self, name, sec_name, number: PhoneNumber, email, adress: Address):
        self.name: str = name
        self.sec_name: str = sec_name
        self.phone_number: number
        self.email: str = email
        self.address: Address = adress

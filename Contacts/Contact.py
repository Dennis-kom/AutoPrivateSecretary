import PhoneNumber
import Address


class Contact:

    def __init__(self, name, sec_name, number: PhoneNumber, email, adress: Address):
        self.name: str = name
        self.sec_name: str = sec_name
        self.phone_number: number
        self.email: str = email
        self.address: Address = adress


#TODO: define funcionality of dumping as json file
#TODO: define data manege maner
#TODO: define groups and sets - for contacts definition
#TODO: consider to implement algorithms for data complition
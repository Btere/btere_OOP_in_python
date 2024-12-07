""" inherit the attributes and methods in a class, if they are similarities or extension to a class( not sure)"""
from introduction import generate_id_number

class User:
    def __init__(self, name: str, contact: int, email: str) -> None:
        self.name = name
        self.contact = contact
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.contact} and {self.email}"
    

class Customer(User):
    def __init__(self, name: str, contact: int, email):
        super().__init__(name, contact, email)  # Call the parent constructor, so we dont ned to redefine the constructor 
        self.customer_id = generate_id_number()

    def __str__(self):
        return f"Customer {self.customer_id}: {super().__str__()}"

def main():
    """ the entry point for the app
    """
    customers = User("Agata", 51609644, "agataolupazki21@gmail.com")
    #print(customers)
    customer1 = Customer("Agata_ottawa", 51609634, "agataolupazki21@gmail.com")
    customer2 = Customer("Agata_ottaa", 516096364, "agatolupazki21@gmail.com")
    print(customer1)
    print(customer2)

    #print(f"the customer id: {customeer}")

if __name__ == "__main__":
    main()

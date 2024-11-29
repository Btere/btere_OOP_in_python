from typing import List, NewType, Union
import itertools
import logging


#rom logging.logger import initialize_logging  

#logger = logging.getLogger(__name__)
#initialize_logging(level="DEBUG")

from encap import Table


from typing import List
from encap import Table  # Importing Table class


def generate_id_number():
    """Generate a unique ID number for tables."""
    import itertools
    return next(itertools.count(1))


class Restaurant:
    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
        self.tables: List[Table] = []

    def add_table(self, capacity: int) -> Table:
        """Add a new table to the restaurant and return the table instance."""
        table_id = generate_id_number()
        table = Table(table_id, capacity)
        self.tables.append(table)
        print(f"Table {table.__str__()} has been added.")
        return table  # Returning the table instance for further use



def main():
    the_restaurant = Restaurant("Whiskey in the Jar", "Forum-old town")
    
    # Add a table with a capacity of 10 people
    table1 = the_restaurant.add_table(10)
    
    # Try to reserve the table
    try:
        table1.reserve_the_table()
        print(f"Reservation successful for table: {table1.__str__()}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()



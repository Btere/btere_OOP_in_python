"""Encapsulation protect or hide internal data, that users are not suppoed to see, only exposing what's necessary.
Users should be able to know if a table is availabe, if yes, then make reservation, and we get the capacity

"""
class Table:
    def __init__(self, table_id: int, capacity: int, status: str = "available"):
        self.__table_id = table_id
        self.__capacity = capacity
        self.__status = status
    
    def table_is_available(self) -> bool:
        """Returns whether the table is available for reservation"""
        return self.__status == "available"
    
    def reserve_the_table(self) -> None:
        """Reserves the table if available"""
        if self.table_is_available():
            self.__status = "reserved"
        else:
            raise ValueError(f"Table {self.__table_id} is already occupied.")
    
    def get_capacity(self) -> int:
        """Returns the table's capacity"""
        return self.__capacity

    def get_status(self) -> str:
        """Returns the table's status"""
        return self.__status

    def __str__(self):
        return f"Table {self.__table_id}: Capacity {self.__capacity}, Status {self.__status}"

def main():
    obj1 = Table(5, 5,"occupied")
    obj1.get_capacity()
    print(f"let know the capacity of the table")

if __name__ == "__main__":
    main()

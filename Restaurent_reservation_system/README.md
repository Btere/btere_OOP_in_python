## Introduction

Design a system where customers can reserve tables, view menus, and order food online, called **Restaurant Reservation System** using Object-Oriented Programming (OOP) principles.


## Key Requirements
Customers can view available tables and make reservations.
Admin or restaurant staff can manage tables and reservations.
Reservation details include the date, time, table, and customer.
Customers can cancel or update reservations.
Optional: Add features like ordering food, payment processing, and notifications.


### **Class Design**
Below are the suggested classes and their key attributes and methods.

---

#### **1. Class: Restaurant**
Represents the restaurant entity.

- **Attributes**:
  - `name: str`
  - `address: str`
  - `tables: List[Table]`
  - `reservations: List[Reservation]`

- **Methods**:
  - `add_table(table: Table): None`: Adds a new table to the restaurant.
  - `remove_table(table_id: int): None`: Removes a table by ID.
  - `find_available_table(date: str, time: str, num_people: int) -> List[Table]`: Finds tables available for a given date, time, and number of people.
  - `add_reservation(reservation: Reservation): None`: Adds a new reservation.
  - `cancel_reservation(reservation_id: int): None`: Cancels a reservation.

---

#### **2. Class: Table**
Represents a table in the restaurant.

- **Attributes**:
  - `table_id: int`
  - `capacity: int`
  - `status: str` (e.g., "Available", "Reserved")

- **Methods**:
  - `is_available(date: str, time: str) -> bool`: Checks if the table is available at a specific time.

---

#### **3. Class: Reservation**
Represents a reservation made by a customer.

- **Attributes**:
  - `reservation_id: int`
  - `customer: Customer`
  - `table: Table`
  - `date: str` (e.g., "2024-11-25")
  - `time: str` (e.g., "19:00")
  - `num_people: int`
  - `status: str` (e.g., "Confirmed", "Cancelled")

- **Methods**:
  - `update_reservation(date: str, time: str, num_people: int): None`: Updates reservation details.
  - `cancel_reservation(): None`: Cancels the reservation.

---

#### **4. Class: Customer**
Represents a customer using the reservation system.

- **Attributes**:
  - `customer_id: int`
  - `name: str`
  - `phone: str`
  - `email: str`
  - `reservations: List[Reservation]`

- **Methods**:
  - `make_reservation(restaurant: Restaurant, date: str, time: str, num_people: int): Reservation`: Makes a new reservation.
  - `cancel_reservation(reservation_id: int): None`: Cancels a reservation by ID.

---

#### **5. Class: Admin**
Represents an admin or staff managing the system.

- **Attributes**:
  - `admin_id: int`
  - `name: str`
  - `email: str`

- **Methods**:
  - `view_all_reservations(restaurant: Restaurant): List[Reservation]`: Lists all reservations.
  - `update_table_status(table_id: int, status: str): None`: Updates the status of a table.

---

#### **6. Class: Menu** (Optional)
Represents the restaurant menu for ordering.

- **Attributes**:
  - `items: List[MenuItem]`

- **Methods**:
  - `add_item(item: MenuItem): None`: Adds a new item to the menu.
  - `remove_item(item_id: int): None`: Removes an item from the menu.

---

#### **7. Class: MenuItem** (Optional)
Represents an item on the menu.

- **Attributes**:
  - `item_id: int`
  - `name: str`
  - `price: float`
  - `description: str`

- **Methods**:
  - `get_details(): str`: Returns details of the menu item.

---

#### **8. Class: Notification** (Optional)
Handles notifications to customers or admins.

- **Attributes**:
  - `recipient: str`
  - `message: str`

- **Methods**:
  - `send(): None`: Sends the notification.

---

### **Relationships Between Classes**
- `Restaurant` has many `Table` and many `Reservation`.
- `Reservation` is linked to one `Table` and one `Customer`.
- `Customer` can have multiple `Reservation`.
- `Admin` manages the `Restaurant` (optional role).

---

### **Method Examples**

#### Example: Making a Reservation
```python
def make_reservation(self, restaurant: Restaurant, date: str, time: str, num_people: int) -> Reservation:
    available_tables = restaurant.find_available_table(date, time, num_people)
    if not available_tables:
        raise ValueError("No tables available for the selected time.")
    selected_table = available_tables[0]
    reservation = Reservation(
        reservation_id=generate_id(),
        customer=self,
        table=selected_table,
        date=date,
        time=time,
        num_people=num_people,
        status="Confirmed"
    )
    restaurant.add_reservation(reservation)
    selected_table.status = "Reserved"
    self.reservations.append(reservation)
    return reservation
```

---

#### Example: Finding Available Tables
```python
def find_available_table(self, date: str, time: str, num_people: int) -> List[Table]:
    available_tables = []
    for table in self.tables:
        if table.capacity >= num_people and table.is_available(date, time):
            available_tables.append(table)
    return available_tables
```

---

#### Example: Updating a Reservation
```python
def update_reservation(self, date: str, time: str, num_people: int) -> None:
    self.date = date
    self.time = time
    self.num_people = num_people
    self.status = "Updated"
```

---

### **Features for Expansion**
1. **Ordering Food**: Add `Order` and `OrderItem` classes.
2. **Payment Processing**: Integrate with payment systems.
3. **Notifications**: Notify customers about reservation updates.
4. **Table Layout**: Visual representation of table arrangements.

This setup gives you all the tools and flexibility to design, implement, and expand a restaurant reservation system while adhering to OOP principles. Let me know if you want code examples or specific implementations!


## OOP Concepts:
1. Reservation, Table, Customer, and Menu as classes.
2. Polymorphism for managing dine-in and online order types.
1,. Design Patterns:
1., ingleton: Manage a single instance of the restaurant's seating arrangement.
1.,Decorator: Add special requests to food orders (e.g., extra cheese, no onions).
Command: Handle customer orders (e.g., placing, updating, and canceling orders).
3. Polymorphism

4. Abstraction

## How to Think in OOP Principles
### Encapsulation:
Ask, "What data needs to be protected or controlled?"

Example: Table status (__status) should not be modified directly.
### Inheritance:
Ask, "Do these classes share common attributes or behavior?"

Example: Both Customer and Admin share properties like name, email.
### Polymorphism:
Ask, "Can I use a single interface for different behaviors?"

Example: Use User for both Customer and Admin, but with different perform_action methods.
### Abstraction:
Ask, "Can I define a template or contract for these classes?"

Example: Use Notifier to enforce a common interface for notifications.
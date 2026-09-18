
# BUS RESERVATION SYSTEM

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class - Inheritance
class Passenger(Person):
    def __init__(self, name, age, phone):
        super().__init__(name, age)
        self.phone = phone

    def display_passenger(self):
        self.display_person()
        print("Phone:", self.phone)


# Bus class
class Bus:
    def __init__(self):
        self.bus_number = 101
        self.source = "Dindigul"
        self.destination = "Chennai"

        # List
        self.seats = [1, 2, 3, 4, 5]

        # Dictionary
        self.bookings = {}

    # Function to display bus details
    def display_bus(self):
        print("\n--- BUS DETAILS ---")
        print("Bus Number:", self.bus_number)
        print("From:", self.source)
        print("To:", self.destination)
        print("Available Seats:", self.seats)

    # Function to book a ticket
    def book_ticket(self):
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        phone = input("Enter phone number: ")

        passenger = Passenger(name, age, phone)

        print("Available seats:", self.seats)

        seat = int(input("Enter seat number: "))

        if seat in self.seats:
            self.seats.remove(seat)

            # Dictionary stores seat and passenger object
            self.bookings[seat] = passenger

            print("Ticket booked successfully!")

        else:
            print("Seat is not available.")

    # Function to display bookings
    def display_bookings(self):
        if len(self.bookings) == 0:
            print("No bookings found.")

        else:
            print("\n--- BOOKING DETAILS ---")

            # Loop through dictionary
            for seat, passenger in self.bookings.items():
                print("\nSeat Number:", seat)
                passenger.display_passenger()

    # Function to cancel ticket
    def cancel_ticket(self):
        seat = int(input("Enter seat number to cancel: "))

        if seat in self.bookings:
            del self.bookings[seat]
            self.seats.append(seat)
            self.seats.sort()

            print("Ticket cancelled successfully!")

        else:
            print("No booking found for this seat.")


# Object creation
bus = Bus()

# Loop
while True:
    print("\n===== BUS RESERVATION SYSTEM =====")
    print("1. Display Bus Details")
    print("2. Book Ticket")
    print("3. Display Bookings")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bus.display_bus()

    elif choice == "2":
        bus.book_ticket()

    elif choice == "3":
        bus.display_bookings()

    elif choice == "4":
        bus.cancel_ticket()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
        

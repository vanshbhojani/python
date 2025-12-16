class BusReservation:
    def __init__(self):
        #------------Predefined routes------------#
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Mysore": 450,
            "Surat to Ahmedabad": 350
        }

        # Store tickets => {ticket_id : details}
        self.tickets = {}
        self.next_ticket_id = 1001

        # Seat tracking per route => {route : [occupied_seats]}
        self.seats = {r: [] for r in self.routes}

    # ---------------- SHOW ROUTES ----------------#
    def show_routes(self):
        print("\n Available Routes:")
        for r, p in self.routes.items():
            print(f"{r}  -  ₹{p}")

    # ---------------- BOOK TICKET ----------------#
    def book_ticket(self):
        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")

        print("\nChoose Route:")
        for i, r in enumerate(self.routes, 1):
            print(f"{i}. {r} - ₹{self.routes[r]}")

        route_choice = int(input("Enter option: "))
        route_list = list(self.routes.keys())

        if not (1 <= route_choice <= len(route_list)):
            print("Invalid route selection.")
            return

        route = route_list[route_choice - 1]

        #------------Check seat availability------------#
        if len(self.seats[route]) >= 40:
            print("All seats are booked on this route.")
            return

        #------------Assign next seat------------#
        seat_no = len(self.seats[route]) + 1
        self.seats[route].append(seat_no)

        # ------------Ticket ID ------------#
        tid = self.next_ticket_id
        self.next_ticket_id += 1

        # ------------ Save ticket ------------#
        self.tickets[tid] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "price": self.routes[route],
            "seat": seat_no
        }

        print(f"\n Ticket Booked Successfully!")
        print(f"Ticket ID: {tid}")
        print(f"Seat No: {seat_no}")

    # ---------------- VIEW TICKET ----------------
    def view_ticket(self, tid):
        if tid in self.tickets:
            t = self.tickets[tid]
            print("\n Ticket Details:")
            print(f"Ticket ID: {tid}")
            print(f"Passenger: {t['name']}")
            print(f"Age: {t['age']}")
            print(f"Mobile: {t['mobile']}")
            print(f"Route: {t['route']}")
            print(f"Seat: {t['seat']}")
            print(f"Price: ₹{t['price']}")
        else:
            print("Ticket not found.")

    # ---------------- CANCEL TICKET ----------------
    def cancel_ticket(self, tid):
        if tid in self.tickets:
            route = self.tickets[tid]["route"]
            seat = self.tickets[tid]["seat"]

            self.seats[route].remove(seat)
            del self.tickets[tid]

            print("Ticket cancelled successfully.")
        else:
            print("Ticket ID not found.")


# ---------------- MAIN LOOP ----------------
bus = BusReservation()

while True:
    print("""
------ Bus Ticket Reservation ------
1. Show Available Routes
2. Book Ticket
3. View Ticket
4. Cancel Ticket
5. Exit
""")

    c = int(input("Enter choice: "))

    if c == 1:
        bus.show_routes()
    elif c == 2:
        bus.book_ticket()
    elif c == 3:
        tid = int(input("Enter Ticket ID: "))
        bus.view_ticket(tid)
    elif c == 4:
        tid = int(input("Enter Ticket ID to cancel: "))
        bus.cancel_ticket(tid)
    elif c == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

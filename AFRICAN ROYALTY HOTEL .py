from datetime import date

class Hotel:
    def __init__(self):
        self.rooms = {}
        self.available_rooms = {'std':[101,102,103],
                                'delux': [201,202,203],
                                'execu': [301,302,303],
                                'suite': [401,402,403]}
        self.roomprice = {1:250, 2:400, 3:550, 4:700}

    def check_in(self, name, address, phone):
        roomtype = int(input('Room types: \n1.Standard \n2.Deluxe \n3.Executive \n4.Suite \nSelect a room type: '))
        if roomtype == 1:
            if self.available_rooms['std']:
                room_no = self.available_rooms['std'].pop(0)
            else:
                print('Sorry, Standard room not available')
                return
        elif roomtype == 2:
            if self.available_rooms['delux']:
                room_no = self.available_rooms['delux'].pop(0)
            else:
                print('Sorry, Deluxe room not available')
                return
        elif roomtype == 3:
            if self.available_rooms['execu']:
                room_no = self.available_rooms['execu'].pop(0)
            else:
                print('Sorry, Executive room not available')
                return
        elif roomtype == 4:
            if self.available_rooms['suite']:
                room_no = self.available_rooms['suite'].pop(0)
            else:
                print('Sorry, Suite room not available')
                return
        else:
            print('Sorry, Room type not available')

        d,m,y = map(int,input('enter check-in-date in date, month, year: ').split())
        check_in = date(y,m,d)
        self.rooms[room_no] = { 'name': name,
                                'address': address,
                                'phone': phone,
                                'check_in_date': check_in,
                                'room_type': roomtype,
                                'roomservices':0
                                }
        print(f"Checked in {name},{address} to room: {room_no} on {check_in}")

    def room_services(self, room):
        if room in self.rooms:
            print("************** AFRICAN ROYALTY HOTEL *****************")
            print('1.Tea/Coffee: $20 2. Dessert: $30 3. Breakfast: $25 4. Lunch: $40 5. Dinner: $35 6. Exit')
            while 1:
                c = int(input('Select your Choice: '))
                if c == 1:
                    q = int(input('Enter the quantity: '))
                    self.rooms[room]['roomservices'] += 20*q
                elif c == 2:
                    q = int(input('Enter the quantity: '))
                    self.rooms[room]['roomservices'] += 30*q
                elif c == 3:
                    q = int(input('Enter the quantity: '))
                    self.rooms[room]['roomservices'] += 25*q
                elif c == 4:
                    q = int(input('Enter the quantity: '))
                    self.rooms[room]['roomservices'] += 40*q
                elif c == 5:
                    q = int(input('Enter the quantity: '))
                    self.rooms[room]['roomservices'] += 35*q
                elif c == 6:
                    break;
                else:
                    print('Sorry, INVALID CHOICE')
            print('Room Services $:',self.rooms[room]['roomservices'],'\n')
        else:
            print('Sorry, INVALID ROOM NUMBER')

    def occupied_rooms(self):
        if not self.rooms:
            print('No rooms are occupied at the moment')
        else:
            print('Occupied rooms')
            print('-----------------------')
            print('Room No.   Name   Phone')
            print('-----------------------')
            for room, details in self.rooms.items():
                print(room, '\t', details['name'], '\t', details['address'], '\t', details['phone'])

    def process_payment(self, amount):
        print(f"\nYour total bill is: ${amount}")
        print("Select payment method:")
        print("1. Cash")
        print("2. Card")
        method = input("Enter payment method (1 or 2): ")

        if method == '1':
            confirm = input(f"Confirm cash payment of ${amount}? (yes/no): ").lower()
            return confirm == 'yes'

        elif method == '2':
            card_number = input("Enter your 16-digit card number: ")
            if len(card_number) != 16 or not card_number.isdigit():
                print("Invalid card number. Try again.")
                return self.process_payment(amount)
            expiry = input("Enter expiry date (MM/YY): ")
            cvv = input("Enter CVV (3 digits): ")
            print("Processing payment...")
            # Simulate random approval for demo purposes
            approved = random.choice([True, True, False])
            if approved:
                print("Card payment successful.")
                return True
            else:
                print("Card declined. Try again or use cash.")
                return self.process_payment(amount)
        else:
            print("Invalid payment method. Try again.")
            return self.process_payment(amount)

    def print_receipt(self, name, address, phone, room, roomtype, checkin, checkout, duration, roombill, roomservices,
                      total):
        print("\n********** PAYMENT RECEIPT **********")
        print("AFRICAN ROYALTY HOTEL")
        print("--------------------------------------")
        print(f"Guest Name   : {name}")
        print(f"Address      : {address}")
        print(f"Phone        : {phone}")
        print(f"Room Number  : {room}")
        print(f"Room Type    : {roomtype}")
        print(f"Check-in     : {checkin}")
        print(f"Check-out    : {checkout}")
        print(f"Duration     : {duration} night(s)")
        print("--------------------------------------")
        print(f"Room Charges : ${roombill}")
        print(f"Services     : ${roomservices}")
        print(f"Total Bill   : ${total}")
        print("--------------------------------------")
        print("Thank you for staying with us!")
        print("**************************************\n")

    def check_out(self, room):
            if room in self.rooms:
                check_out_date = date.today()
                check_in_date = self.rooms[room]['check_in_date']
                duration = (check_out_date - check_in_date).days
                duration = duration if duration > 0 else 1
                roomtype = self.rooms[room]['room_type']
                roombill = self.roomprice[roomtype] * duration
                roomservices = self.rooms[room]['roomservices']
                total = roombill + roomservices

                guest = self.rooms[room]
                print('------------------------------------------------------')
                print('************** AFRICAN ROYALTY HOTEL *****************')
                print(f'Guest: {guest["name"]}, {guest["address"]}, Phone: {guest["phone"]}')
                print(f'Check-in: {check_in_date}, Check-out: {check_out_date}, Duration: {duration} day(s)')
                print(f'Room Bill: ${roombill}, Services: ${roomservices}, Total: ${total}')
                print('------------------------------------------------------')

           if self.process_payment(total):
            self.print_receipt(
                guest['name'], guest['address'], guest['phone'],
                room, roomtype, check_in_date, check_out_date,
                duration, roombill, roomservices, total
            )

            if roomtype == 1:
                self.available_rooms['std'].append(room)
            elif roomtype == 2:
                self.available_rooms['delux'].append(room)
            elif roomtype == 3:
                self.available_rooms['execu'].append(room)
            elif roomtype == 4:
                self.available_rooms['suite'].append(room)
            del self.rooms[room]
        else:
            print("Payment not completed. Checkout cancelled.")
        else:
        print(f'Room {room} is AVAILABLE')

    def start_app(self):
        while True:
            print("_______________________________________")
            print("WELCOME TO THE AFRICAN ROYALTY HOTEL")
            print("_______________________________________")
            print("1. Check-in")
            print("2. Room Services")
            print("3. Occupied Rooms")
            print("4. Check-out")
            print("5. Exit")
            print("_______________________________________")

            choice = input("Enter your choice(1-5): ")
            if choice == "1":
                name = input("Enter your name: ")
                adress = input("Enter your adress: ")
                phone = int(input("Enter your phone number: "))
                self.check_in(name,adress,phone)
            elif choice == "2":
                room = int(input("Enter your room number: "))
                self.room_services(room)
            elif choice == "3":
                self.occupied_rooms()
            elif choice == "4":
                room = int(input("Enter your room number: "))
                self.check_out(room)
            elif choice == "5":
                break
            else:
                print("Invalid choice: PLEASE TRY AGAIN")


h = Hotel()
h.start_app()
